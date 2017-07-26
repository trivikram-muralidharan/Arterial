from django.conf.urls import url

from . import views
app_name = 'attendance'

urlpatterns = [
    url(r'^loginbloodbank/$', views.loginbloodbank, name='loginbloodbank'),
    url(r'^loginhospital/$', views.loginhospital, name='loginhospital'),
    url(r'^logindonor/$', views.logindonor, name='logindonor'),
    url(r'^indexhospital/$', views.indexhospital, name='indexhospital'),
    url(r'^indexbloodbank/$', views.indexbloodbank, name='indexbloodbank'),
    url(r'^indexdonor/$', views.indexdonor, name='indexdonor'),

    ]
