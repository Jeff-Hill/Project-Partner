import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..connection import Connection


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
def new_tool_form(request):
    if request.method == 'GET':
        tools = get_tools()
        template = 'tools/new_tool_form.html'
        context = {
            'all_tools': tools
        }

        return render(request, template, context)