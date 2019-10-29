import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..connection import Connection


def get_project(project_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.name,
            p.description,
            p.location,
            p.width,
            p.length,
            p.completed,
            p.owner_id,
            pt.id project_tool_id,
            pt.project_id,
            pt.tool_id,
            t.id tool_id,
            t.name,
            t.manufacturer,
            t.cost,
            t.description,
            t.own,
            m.id material_id,
            m.name,
            m.description,
            m.cost,
            m.quantity,
            m.project_id
        FROM projectpartnerapp_project p
        JOIN projectpartnerapp_projecttool pt ON pt.project_id = p.id
        JOIN projectpartnerapp_tool t ON pt.tool_id = t.id
        JOIN projectpartnerapp_material m ON p.id = m.project_id
        JOIN projectpartnerapp_owner o ON o.id = p.owner_id
        JOIN auth_user u ON u.id = o.user_id
        WHERE p.id = ?

        """, (project_id,))

        return db_cursor.fetchone()

@login_required
def project_details(request, project_id):
    if request.method == 'GET':
        project = get_project(project_id)

        template = 'projects/detail.html'
        context = {
            'project': project
        }

        return render(request, template, context)