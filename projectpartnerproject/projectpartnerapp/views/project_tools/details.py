import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection


def get_project_tool(projecttool_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.tool_id,
            pt.project_id,
            t.id,
            t.name,
            t.manufacturer,
            t.description,
            t.cost,
            t.own
        FROM projectpartnerapp_projecttool pt
        JOIN projectpartnerapp_tool t ON pt.tool_id = t.id
        WHERE pt.id = ?
        """, (projecttool_id,))

        return db_cursor.fetchone()

@login_required
def project_tool_details(request, projecttool_id):
    if request.method == 'GET':
        projecttool = get_project_tool(projecttool_id)

        template = 'project_tools/detail.html'
        context = {
            'projecttool': projecttool
        }

        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST


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

            return redirect(reverse('projectpartnerapp:projects'))