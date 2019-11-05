import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .details import get_material
from ..projects.form import get_projects
from ..connection import Connection


def get_materials(request):
    with sqlite3.connect(Connection.db_path) as conn:
        user = request.user
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            m.id,
            m.name,
            m.description,
            m.cost,
            m.quantity,
            m.project_id,
            m.owner_id
        from projectpartnerapp_material m
        where m.owner_id = ?
        """,(user.id,))

        return db_cursor.fetchall()

@login_required
def material_form(request):
    if request.method == 'GET':
        materials = get_materials(request)
        projects = get_projects(request)
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
        projects = get_projects(request)
        next = request.GET['next']


        template = 'materials/material_edit_form.html'
        context = {
            'material': material,
            'all_projects': projects,
            "material_id": material_id,
            "next": next
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

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
                    form_data['name'] or None, form_data['description'] or None,
                    form_data['cost'] or None, form_data['quantity'] or None,
                    form_data['project_id'] or None, material_id
                ))

            return redirect(reverse('projectpartnerapp:materials'))

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