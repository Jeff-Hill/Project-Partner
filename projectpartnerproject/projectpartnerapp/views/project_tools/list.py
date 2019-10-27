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

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO projectpartnerapp_projecttool
            (
                project_id, tool_id
            )
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['manufacturer'],
                form_data['description'], form_data['cost'],
                form_data["own"]))

        return redirect(reverse('projectpartnerapp:tools'))