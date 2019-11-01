import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .details import get_material
from ..projects.form import get_projects
from ..connection import Connection


def get_materials():
    with sqlite3.connect(Connection.db_path) as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            m.id,
            m.name,
            m.description,
            m.cost,
            m.quantity,
            m.project_id
        from projectpartnerapp_material m
        """)

        return db_cursor.fetchall()

@login_required
def material_form(request):
    if request.method == 'GET':
        materials = get_materials()
        projects = get_projects()
        template = 'materials/form.html'
        context = {
            'all_materials': materials,
            'all_projects': projects
        }

        return render(request, template, context)

@login_required
def material_edit_form(request, material_id):

    if request.method == 'GET':
        material = get_material(material_id)
        projects = get_projects()

        template = 'materials/material_edit_form.html'
        context = {
            'material': material,
            'all_projects': projects,
            "material_id": material_id
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE projectpartnerapp_material
                SET name = ?,
                    description = ?,
                    cost = ?,
                    quantity = ?,
                    project_id = ?
                WHERE id = ?
                """,
                (
                    form_data['name'], form_data['description'],
                    form_data['cost'], form_data['quantity'],
                    form_data['project_id'], material_id
                ))

            return redirect(reverse('projectpartnerapp:material'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM projectpartnerapp_material
                    WHERE id = ?
                """, (material_id,))

            return redirect(reverse('projectpartnerapp:materials'))