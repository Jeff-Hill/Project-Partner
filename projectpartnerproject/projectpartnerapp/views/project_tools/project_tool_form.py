import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

def get_tools():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            t.id,
            t.name,
            t.manufacturer,
            t.description,
            t.cost,
            t.own
        from projectpartnerapp_tool t
        """)

        return db_cursor.fetchall()

@login_required
def project_tool_form(request):
    if request.method == 'GET':
        projects = get_projects()
        tools = get_tools()
        template = 'project_tools/tool_select_form.html'
        context = {
            'all_projects': projects,
            'all_tools': tools
        }

        return render(request, template, context)