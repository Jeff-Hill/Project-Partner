import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projectpartnerapp.models import Owner
from ..connection import Connection

@login_required
def owner_list(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            o.id,
            o.user_id,
            u.first_name,
            u.last_name,
            u.email
        from projectpartnerapp_owner o
        join auth_user u on o.user_id = u.id
        """)

        all_owners = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            owner = Owner()
            owner.id = row["id"]
            owner.user_id = row["user_id"]
            owner.first_name = row["first_name"]
            owner.last_name = row["last_name"]
            owner.email = row["email"]

            all_owners.append(owner)

    template_name = 'owners/list.html'

    context = {
        'all_owners': all_owners
    }

    return render(request, template_name, context)