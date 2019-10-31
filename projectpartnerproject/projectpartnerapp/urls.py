from django.conf.urls import url, include
from django.urls import path
# from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token
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
    path('projects/<int:project_id>/', project_details, name='project'),
    url(r'^projects/(?P<project_id>[0-9]+)/form$', project_edit_form, name='project_edit_form'),



    url(r'^owners$', owner_list, name='owners'),

    url(r'^materials$', material_list, name='materials'),
    url(r'^material/form$', material_form, name='material_form'),
    path('materials/<int:material_id>/', material_details, name='material'),
    url(r'^materials/(?P<material_id>[0-9]+)/form$', material_edit_form, name='material_edit_form'),


    url(r'^tools$', tool_list, name='tools'),
    url(r'^new-tool/form$', new_tool_form, name='new_tool_form'),

    url(r'^project-tools$', project_tool_list, name='project_tools'),
    url(r'^project-tool/form$', project_tool_form, name='project_tool_form'),



]