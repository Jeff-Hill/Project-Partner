import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection

@login_required
def project_tool_list(request):
    if request.method == 'POST':
        form_data = request.POST
        tool_id = request.POST.getlist('multicheckbox[]')


        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            for id in tool_id:
                db_cursor.execute("""
                INSERT INTO projectpartnerapp_projecttool
                (
                    project_id, tool_id
                )
                VALUES (?, ?)
                """,
                (form_data['project_id'], id,)
                )

        return redirect(reverse('projectpartnerapp:material_form'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM projectpartnerapp_projecttool
                WHERE id = ?
                """, (projecttool_id,))

            return redirect(reverse('libraryapp:books'))