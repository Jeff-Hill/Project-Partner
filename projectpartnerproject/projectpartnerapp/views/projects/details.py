import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projectpartnerapp.models import Project
from ..connection import Connection

def create_project(cursor, row):
        _row = sqlite3.Row(cursor, row)

        project = Project()
        project.id = _row['id']
        project.name = _row['name']
        project.description = _row['description']
        project.location = _row['location']
        project.width = _row['width']
        project.length = _row['length']
        project.owner_id = _row['owner_id']
        project.completed = _row['completed']

        return project

def get_project(project_id):
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_project
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                p.id,
                p.name,
                p.description,
                p.location,
                p.width,
                p.length,
                p.completed,
                p.owner_id,
                pt.id project_tool_id,
                pt.project_id,
                pt.tool_id,
                t.id tool_id,
                t.name,
                t.manufacturer,
                t.cost,
                t.description,
                t.own,
                m.id material_id,
                m.name material_name,
                m.description material_description,
                m.cost,
                m.quantity,
                m.project_id
            FROM projectpartnerapp_project p
            JOIN projectpartnerapp_projecttool pt ON pt.project_id = p.id
            JOIN projectpartnerapp_tool t ON pt.tool_id = t.id
            JOIN projectpartnerapp_material m ON p.id = m.project_id
            JOIN projectpartnerapp_owner o ON o.id = p.owner_id
            JOIN auth_user u ON u.id = o.user_id
            WHERE p.id = ?

            """, (project_id,))

        return db_cursor.fetchone()

@login_required
def project_details(request, project_id, pk=None):
    if request.method == 'GET':
        # project = get_project(project_id)
        project = Project.objects.get(pk=project_id)
        template = 'projects/detail.html'
        context = {
            'project': project
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
                UPDATE projectpartnerapp_project
                SET name = ?,
                    description = ?,
                    location = ?,
                    width = ?,
                    length = ?,
                    completed = ?,
                    owner_id = ?
                WHERE id = ?
                """,
                (
                    form_data['name'], form_data['description'],
                    form_data['location'], form_data['width'],
                    form_data["length"], form_data['completed'], request.user.owner.id, project_id,
                ))

            return redirect(reverse('projectpartnerapp:project'))

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM projectpartnerapp_project
                    WHERE id = ?
                """, (project_id,))

            return redirect(reverse('projectpartnerapp:projects'))

