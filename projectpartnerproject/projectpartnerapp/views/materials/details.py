import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from django.http import HttpResponse
from django.http import HttpResponseRedirect



def get_material(material_id):
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                m.id material_id,
                m.name,
                m.description,
                m.cost,
                m.quantity,
                m.project_id
            FROM projectpartnerapp_material m
            WHERE m.id = ?

            """, (material_id,))

        return db_cursor.fetchone()

@login_required
def material_details(request, material_id):
    if request.method == 'GET':
        material = get_material(material_id)
        template = 'materials/detail.html'
        context = {
            'material': material
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            next = form_data["next"]
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE projectpartnerapp_material
                SET name = ?,
                    description = ?,
                    cost = ?,
                    quantity = ?,
                    project_id = ?
                WHERE id = ?
                """,
                (
                    form_data['name'] or None, form_data['description'] or None,
                    form_data['cost'] or None, form_data['quantity'] or None,
                    form_data['project_id'], material_id
                ))

            # return redirect(reverse(next))
            return HttpResponseRedirect(next)

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM projectpartnerapp_material
                    WHERE id = ?
                """, (material_id,))

            return redirect(reverse('projectpartnerapp:projects'))

