import sqlite3
from django.shortcuts import render
from projectpartnerapp.models import Project
from ..connection import Connection


def project_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                p.id,
                p.owner_id,
                p.name,
                p.description,
                p.location,
                p.length,
                p.width,
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