from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from .views import register_user
from .views import register_form

app_name = "projectpartnerapp"

urlpatterns = [
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^register$', register_user, name='register'),
    url(r'^register/form$', register_form, name='registerform'),


    url(r'^$', home, name='home'),
    url(r'^projects$', project_list, name='projects'),
    url(r'^project/form$', project_form, name='project_form'),

    url(r'^owners$', owner_list, name='owners'),
    url(r'^materials$', material_list, name='materials'),
    url(r'^tools$', tool_list, name='tools'),


]