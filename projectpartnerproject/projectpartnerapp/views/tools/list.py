import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from projectpartnerapp.models import Tool
from ..connection import Connection
from django.http import HttpResponse
from django.http import HttpResponseRedirect

@login_required
def tool_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            user = request.user
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                t.id,
                t.name,
                t.manufacturer,
                t.description,
                t.cost,
                t.own,
                t.owner_id
            from projectpartnerapp_tool t
            where t.owner_id = ?
            """,(user.id,))

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

    elif request.method == 'POST':
        form_data = request.POST
        # next = form_data["next"]
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO projectpartnerapp_tool
            (
                name, manufacturer, description,
                cost, own, owner_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (form_data['name'], form_data['manufacturer'],
                form_data['description'], form_data['cost'],
                form_data["own"], request.user.owner.id))

        # return HttpResponseRedirect(next)

        return redirect(reverse('projectpartnerapp:tools'))