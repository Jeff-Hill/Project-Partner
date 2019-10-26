import sqlite3
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from projectpartnerapp.models import Owner
from ..connection import Connection


@csrf_exempt
def register_user(request):

    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''
    if request.method == 'POST':

        form_data = request.POST
        # Create a new user by invoking the `create_user` helper method
        # on Django's built-in User model
        new_user = User.objects.create_user(
            username=form_data['username'],
            email=form_data['email'],
            password=form_data['password'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name']
        )

        owner = Owner.objects.create(
            user=new_user
        )

        return redirect(reverse('projectpartnerapp:/'))

        # Commit the user to the database by saving it
        # owner.save()

        # data = form_data(owner)

        # return render(data, request, content_type='application/json')