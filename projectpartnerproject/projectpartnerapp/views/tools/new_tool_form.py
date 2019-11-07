import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from .details import get_tool


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
        # next = request.GET['next']
        template = 'tools/new_tool_form.html'
        context = {
            'all_tools': tools,
            # "next": next
        }

        return render(request, template, context)

@login_required
def tool_edit_form(request, tool_id):

    if request.method == 'GET':
        tool = get_tool(tool_id)

        template = 'tools/new_tool_form.html'
        context = {
            'tool': tool,
        }

        return render(request, template, context)