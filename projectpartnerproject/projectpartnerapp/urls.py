from django.conf.urls import url
from .views import *

app_name = "projectpartnerapp"

urlpatterns = [
    url(r'^$', project_list, name='home'),
    url(r'^projects$', project_list, name='projects'),
    url(r'^owners$', owner_list, name='owners'),
    url(r'^materials$', material_list, name='materials'),
    url(r'^tools$', tool_list, name='tools'),
]