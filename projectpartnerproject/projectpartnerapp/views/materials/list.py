import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from projectpartnerapp.models import Material
from ..connection import Connection

@login_required
def material_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            user = request.user
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                m.id,
                m.project_id,
                m.name,
                m.description,
                m.cost,
                m.quantity,
                m.owner_id
            from projectpartnerapp_material m
            where m.owner_id = ?
            """,(user.id,))

            all_materials = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                material = Material()
                material.id = row['id']
                material.name = row['name']
                material.description = row['description']
                material.cost = row['cost']
                material.quantity = row['quantity']
                material.project_id = row['project_id']

                all_materials.append(material)

        template = 'materials/list.html'
        context = {
            'all_materials': all_materials
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        # This gets all the materials that were added in the project creation step as an array that can be iterated over
        # to insert individual instances into the database table
        list_materials = request.POST.getlist('name[]')


        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
        # Looping over the array of materials for this project and inserting it into the database
            for material in list_materials:
                db_cursor.execute("""
                INSERT INTO projectpartnerapp_material
                (
                    name, project_id, owner_id
                )
                VALUES (?, ?, ?)
                """,
                (material,
                form_data['project_id'], request.user.owner.id))

        return redirect(reverse('projectpartnerapp:home'))

