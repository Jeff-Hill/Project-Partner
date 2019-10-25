import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projectpartnerapp.models import Tool
from ..connection import Connection

@login_required
def tool_list(request):
    if request.method == 'GET':
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

            all_tools = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                tool = Tool()
                tool.id = row['id']
                tool.name = row['name']
                tool.manufacturer = row['manufacturer']
                tool.description = row['description']
                tool.cost = row['cost']
                tool.own = row['own']

                all_tools.append(tool)

        template = 'tools/list.html'
        context = {
            'all_tools': all_tools
        }

        return render(request, template, context)