import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection


def get_tool(tool_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
           t.id,
           t.name,
           t.manufacturer,
           t.description,
           t.cost,
           t.own,
           t.owner_id
        FROM projectpartnerapp_tool t
        WHERE t.id = ?
        """, (tool_id,))

        return db_cursor.fetchone()

@login_required
def tool_details(request, tool_id):
    if request.method == 'GET':
        tool = get_tool(tool_id)

        template = 'tools/detail.html'
        context = {
            'tool': tool
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE projectpartnerapp_tool
                SET name = ?,
                    manufacturer = ?,
                    description = ?,
                    cost = ?,
                    own = ?,
                    owner_id = ?
                WHERE id = ?
                """,
                (
                    form_data['name'], form_data['manufacturer'],
                    form_data['description'], form_data['cost'],
                    form_data["own"], request.user.owner.id, tool_id,
                ))

            return redirect(reverse('projectpartnerapp:tools'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM projectpartnerapp_tool
                WHERE id = ?
                """, (tool_id,))

            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM projectpartnerapp_projecttool
                WHERE tool_id = ?
                """, (tool_id,))

            return redirect(reverse('projectpartnerapp:tools'))