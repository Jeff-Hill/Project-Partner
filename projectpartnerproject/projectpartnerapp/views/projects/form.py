import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .details import get_project
from ..connection import Connection


def get_projects():
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
            p.completed,
            p.owner_id
        from projectpartnerapp_project p
        """)

        return db_cursor.fetchall()

@login_required
def project_form(request):
    if request.method == 'GET':
        projects = get_projects()
        template = 'projects/form.html'
        context = {
            'all_projects': projects
        }

        return render(request, template, context)

@login_required
def project_edit_form(request, project_id):

    if request.method == 'GET':
        project = get_project(project_id)
        # libraries = get_libraries()

        template = 'projects/form.html'
        context = {
            'project': project,
            # 'all_projects': libraries
        }

        return render(request, template, context)