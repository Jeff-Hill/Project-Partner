import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from projectpartnerapp.models import Project
from ..connection import Connection

@login_required
def project_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                p.id,
                p.name,
                p.description,
                p.location,
                p.width,
                p.length,
                p.owner_id,
                p.completed
            from projectpartnerapp_project p
            """)

            all_projects = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                project = Project()
                project.id = row['id']
                project.name = row['name']
                project.description = row['description']
                project.location = row['location']
                project.width = row['width']
                project.length = row['length']
                project.owner_id = row['owner_id']
                project.completed = row['completed']

                all_projects.append(project)

        template = 'projects/list.html'
        context = {
            'all_projects': all_projects
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO projectpartnerapp_project
            (
                name, description, location,
                width, length, owner_id, completed
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (form_data['name'], form_data['description'],
            form_data['location'], form_data['width'], form_data['length'],
            request.user.owner.id, form_data['completed']))

        return redirect(reverse('projectpartnerapp:projects'))