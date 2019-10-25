from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from .views import register_user

app_name = "projectpartnerapp"

urlpatterns = [
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),


    url(r'^$', home, name='home'),
    url(r'^projects$', project_list, name='projects'),
    url(r'^owners$', owner_list, name='owners'),
    url(r'^materials$', material_list, name='materials'),
    url(r'^tools$', tool_list, name='tools'),

    url(r'^register$', register_user),
    # url(r'^login$', login_user),
    url(r'^api-token-auth$', obtain_auth_token),
    url(r'^api-auth$', include('rest_framework.urls', namespace='rest_framework')),
]