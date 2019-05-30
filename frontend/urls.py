from django.conf.urls import url
from frontend.views import *

app_name = 'frontend'

urlpatterns = [
    url(r'^$', websiteroot.as_view(), ),
    url(r'^userregister/', userregister.as_view(), name='frontend.admin.userregister'),
    url(r'^userregisteraction/', userregisteraction.as_view(), name='frontend.admin.userregisteraction'),
    url(r'^userlogin/', userlogin.as_view(), name='frontend.admin.userlogin'),
    url(r'^userlogincheck/', views.userloginCheck, name="frontend.admin.userlogincheck"),
    url(r'^userdashboard/', userdashboard.as_view(), name='frontend.admin.userdashboard'),
    url(r'^userlogout/', views.userLogout, name='frontend.admin.userlogout'),
]
