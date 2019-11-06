import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .details import get_project
from ..tools.new_tool_form import get_tools
from projectpartnerapp.models import Project, ProjectTool
from ..connection import Connection


def get_projects(request):
    with sqlite3.connect(Connection.db_path) as conn:
        user = request.user
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
        where p.owner_id = ?
        """,(user.id,))

        return db_cursor.fetchall()

@login_required
def project_form(request):
    if request.method == 'GET':
        projects = get_projects(request)
        template = 'projects/form.html'
        context = {
            'all_projects': projects
        }

        return render(request, template, context)

@login_required
def project_edit_form(request, project_id, pk=None):

    if request.method == 'GET':
        project = Project.objects.get(pk=project_id)
        tools = get_tools()

        template = 'projects/project_edit_form.html'
        context = {
            'project': project,
            'all_tools': tools,
        }

        return render(request, template, context)