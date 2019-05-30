"""Dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from dashboard.views import *
from django.conf.urls.static import static


# from dashboard.views import GetAjaxViewDash


app_name = 'dashboard'

urlpatterns = [

    # url(r'^$', views.getHome),
    # url(r'^$', views.appRoot, name="dashboard.root"),

    url(r'^admin/', include([

        url(r'^$', views.getHome),
        # Inbuilt URL's
        # url(r'^login/$', auth_views.login, name='login'),
        # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='dashboard.admin.login'),
        # url(r'^logout/$', auth_views.logout, name='logout'),
        # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='dashboard.admin.logout'),
        url(r'^login/$', views.logIn, name="dashboard.admin.login"),
        url(r'^auth/$', views.authView, name="dashboard.admin.authview"),
        url(r'^logout/$', views.logOut, name="dashboard.admin.logout"),
        url(r'^admin/', admin.site.urls, name='admin'),

        # Dashboard URL's

        url(r'^dashboard$', views.getDashboard, name="dashboard.admin.dashboard"),
        url(r'^list/(?P<model_name>.+)', views.getBasicView, name="dashboard.admin.list"),
        url(r'^ajaxview/', views.AjaxView, name='dashboard.admin.ajaxview'),
        url(r'^actions/', views.getCommonAction, name='dashboard.admin.actions'),

        # ACL Management
        url(r'^aclmanager/', views.getACLpermissions, name="dashboard.admin.getaclpermissions"),
        url(r'^setpermission', views.setPermission, name="dashboard.admin.setpermission"),

        # Signals Test
        url(r'^signaltest', views.signalTest, name='dashboard.admin.signaltest'),
        url(r'^test', views.Test, name='dashboard.admin.test'),

        # User
        url(r'^adduser/', users.addUser.as_view(), name='dashboard.admin.adduser'),
        url(r'^saveuser/', users.saveUser.as_view(), name='dashboard.admin.saveuser'),
        url(r'^edituser/(?P<edit_id>.+)', users.editUser.as_view(), name='dashboard.admin.edituser'),
        url(r'^updateuser', users.updateUser.as_view(), name='dashboard.admin.updateuser'),

        # Role
        url(r'^addrole/', role.addRole.as_view(), name='dashboard.admin.addrole'),
        url(r'^saverole/', role.saveRole.as_view(), name='dashboard.admin.saverole'),
        url(r'^editrole/(?P<edit_id>.+)', role.editRole.as_view(), name='dashboard.admin.editrole'),
        url(r'^updaterole/', role.updateRole.as_view(), name='dashboard.admin.updaterole'),

        # User Role
        url(r'^adduserrole/', userroles.addUserrole.as_view(), name='dashboard.admin.adduserrole'),
        url(r'^saveuserrole/', userroles.saveUserrole.as_view(), name='dashboard.admin.saveuserrole'),
        url(r'^edituserrole/(?P<edit_id>.+)', userroles.editUserrole.as_view(), name='dashboard.admin.edituserrole'),
        url(r'^updateuserrole/', userroles.updateUserrole.as_view(), name='dashboard.admin.updateuserrole'),

    ])),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
