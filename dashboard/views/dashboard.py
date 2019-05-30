from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.contrib import auth, messages
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.apps import apps
from django.shortcuts import render
from django.utils.html import escape
import datetime
import json
from django.template import Context, RequestContext

# App Imports
from dashboard.dashboardmenu import DashboardMenu
from dashboard.models import *
from systemconfig.models import *


def get_model_from_any_app(model_name):
    for app_config in apps.get_app_configs():
        try:
            model = app_config.get_model(model_name)
            return model
        except LookupError:
            pass
    return None


def appRoot(request):
    # return HttpResponse("App Root - Nothing here...!<br> Goto Login : <a href=\"/admin/login\">Login</a> ")
    return render(request, 'dashboard/home.html')


def getHome(request):
    return render(request, 'home.html')


def logIn(request):
    return render(request, 'dashboard/login.html')


def Test(request):
    return render(request, 'dashboard/testing.html')


def authView(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/admin/dashboard')
    else:
        return render(request, 'dashboard/login.html', {'message': 'Invalid Username or Password ...!'})


def getDashboard(request):
    return render(request, 'dashboard.jinja.html', )


def logOut(request):
    auth.logout(request)
    return render(request, 'login.html', {'message': 'You have logged out...!'})


def getBasicView(request, model_name):
    # model_name = apps.get_model('Dashboard', model_name)
    # return HttpResponse(request.path)
    model = get_model_from_any_app(model_name)
    page_title = model.page_title
    listable = model.listable
    show_toolbar = model.show_toolbar
    routes = model.routes
    return render(request, 'datatable.jinja.html',
                  {'listable': listable, 'show_toolbar': show_toolbar, 'routes': routes, 'page_title': page_title,
                   'model_name': model_name, 'model': model, 'toolbarPermissions': toolbarPermissions, })


def AjaxView(request):
    model_name = request.GET.get('model_name', '')
    model = get_model_from_any_app(model_name)
    class_name = model.class_view_name
    # return HttpResponse(class_name)
    if class_name != " ":
        return eval(class_name).as_view()(request)
    else:
        return HttpResponse("Class Not Found...!")


def getCommonAction(request):
    cid = request.POST.getlist('cid[]')
    action_type = request.POST.get('action_type')
    table_name = request.POST.get('table_name')
    acl_key = request.POST.get('acl_key')
    model_name = request.POST.get('model_name')
    model = get_model_from_any_app(model_name)
    return_url = request.POST.get('return_url')
    message = "Please select an actions to perform...!"

    textval = checkACLPermission('1', '2')
    i = 0
    while i < len(cid):
        textval += cid[i]
        i += 1
    # return HttpResponse(textval)

    if (len(cid) > 0) and (table_name in connection.introspection.table_names()):
        acl_status = 1
        # if action_type == "enable" or action_type == "disable":
        #     acl_status = checkACLPermission(acl_key,'edit')
        # else:
        #     acl_status = checkACLPermission(acl_key,'trash')
        #
        # if acl_status == 0:
        #     messages.error(request, 'Access Permission Denied..!')
        #     return HttpResponseRedirect(return_url)

        if action_type == "enable":
            model.objects.filter(id__in=cid).update(status=1)
            messages.success(request, 'Records Published successfully..!')
            return HttpResponseRedirect(return_url)
            # return HttpResponse(return_url)
        elif action_type == "disable":
            model.objects.filter(id__in=cid).update(status=0)
            messages.success(request, 'Records Unpublished successfully..!')
            return HttpResponseRedirect(return_url)
        elif action_type == "remove":
            model.objects.filter(id__in=cid).update(deleted_at=datetime.datetime.now())
            messages.success(request, 'Records Trashed successfully..!')
            return HttpResponseRedirect(return_url)
        elif action_type == "restore":
            model.objects.filter(id__in=cid).update(deleted_at=None)
            messages.success(request, 'Records Restored successfully..!')
            return HttpResponseRedirect(return_url)
        elif action_type == "forcedelete":
            model.objects.filter(id__in=cid).delete()
            messages.success(request, 'Records Deleted successfully..!')
            return HttpResponseRedirect(return_url)
        elif action_type == "view":
            # Perform Action
            messages.success(request, 'Records Viewed successfully..!')
            return HttpResponseRedirect(return_url)
        else:
            messages.info(request, 'Nothing Happened ..!')
            return HttpResponseRedirect(return_url)

    else:
        messages.error(request, 'Unauthorized action detected ..!')
        return HttpResponseRedirect(return_url)


def checkACLPermission(acl_key, action):
    return "test"


def getACLpermissions(request):
    # template = Template("Hello {{ calcName('Gandalf', 2) }}")
    # return HttpResponse(template.render({'calcName': calcName}))
    page_title = "Manage User Role Privileges"
    roles = Roles.objects.all()
    role_id = 1
    # role_id = request.GET['id']
    # role_id = request.GET.get('id',0)
    # if 'id' not in request.GET:
    #     role_id = 0
    # else:
    #     role_id = request.GET['id']
    # print(role_id)
    result = AclPermissions.objects.filter(role_id__exact=role_id).all()
    menugroups = DashboardMenu.menu_items;
    mydict = {"key1": "value1", "key2": "value2"}
    # return render_to_response('aclform.html', {'menugroups': menugroups, 'page_title': page_title, 'mydict': mydict,
    #                                            'calcName': calcName,'levelZero': levelZero,'levelOne': levelOne,'levelTwo': levelTwo,
    #                                            })
    return render(request, 'aclform.jinja.html', {'menugroups': menugroups,
                                                  'page_title': page_title,
                                                  'mydict': mydict,
                                                  'roles' : roles,
                                                  'levelZero': levelZero, 'levelOne': levelOne, 'levelTwo': levelTwo,
                                                  })


def levelZero(main_menu_key, acl_key, role_id):
    main_menu_data = AclPermissions.objects.filter(acl_key=acl_key, role_id=role_id, level=0).first()
    if (main_menu_key):
        main_menu_key = main_menu_key
    else:
        main_menu_key = "No Key Set"
    return {'main_menu_key': main_menu_key, 'main_menu_data': main_menu_data}


def levelOne(sub_menu_key, acl_key, role_id):
    sub_menu_data = AclPermissions.objects.filter(acl_key=acl_key, role_id=role_id, level=1).first()
    # if (sub_menu_key):
    #     sub_menu_key = sub_menu_key
    # else:
    #     sub_menu_key = "No Key Set"

    return {'sub_menu_data': sub_menu_data}


def levelTwo(acl_key, role_id):
    sub_sub_menu_data = AclPermissions.objects.filter(acl_key=acl_key, role_id=role_id, level=2).first()
    return {'sub_sub_menu_data': sub_sub_menu_data}


def setPermission(request):
    role_id = request.POST.get('role_id')
    if role_id == "0":
        messages.error(request, 'Please select a User Roles ..!')
        return HttpResponseRedirect('/admin/aclmanager/')

    AclPermissions.objects.filter(role_id=role_id).delete()

    main_menu_text = request.POST.getlist('main_menu_text[]')
    main_menu_icon = request.POST.getlist('main_menu_icon[]')
    main_menu_acl_key = request.POST.getlist('main_menu_acl_key[]')
    main_menu_order = request.POST.getlist('main_menu_order[]')

    objs = []
    i = 0
    while i < len(main_menu_text):
        main_menu_item = 1 if request.POST.get("main_menu_view_%s" % i) == 'on' else 0
        objs.extend([
            AclPermissions(
                role_id=role_id,
                link='#',
                icon=main_menu_icon[i],
                menu_text=main_menu_text[i],
                acl_key=main_menu_acl_key[i],
                level='0',
                ordering=main_menu_order[i],
                parent_menu='0',
                view=main_menu_item,
            )
        ])
        i += 1

    msg = AclPermissions.objects.bulk_create(objs)

    # ++++++++++++++++++++++++++++++++++ Main Menu Privilege's ++++++++++++++++++++++++++++++++++

    sub_menu_text = request.POST.getlist('sub_menu_text[]')
    sub_menu_icon = request.POST.getlist('sub_menu_icon[]')
    sub_menu_acl_key = request.POST.getlist('sub_menu_acl_key[]')
    sub_menu_order = request.POST.getlist('sub_menu_order[]')
    sub_menu_parent_acl_key = request.POST.getlist('sub_menu_parent_acl_key[]')

    objs = []
    i = 0
    while i < len(sub_menu_text):
        sub_menu_item = 1 if request.POST.get("sub_menu_view_%s" % i) == 'on' else 0
        parent_menu = AclPermissions.objects.filter(role_id=role_id, acl_key=sub_menu_parent_acl_key[i]).first()
        objs.extend([
            AclPermissions(
                role_id=role_id,
                link='#',
                icon=sub_menu_icon[i],
                menu_text=sub_menu_text[i],
                acl_key=sub_menu_acl_key[i],
                level='1',
                ordering=sub_menu_order[i],
                parent_menu=parent_menu.id,
                view=sub_menu_item,
            )
        ])
        i += 1

    msg = AclPermissions.objects.bulk_create(objs)

    # ++++++++++++++++++++++++++++++++++ Sub Sub Menu Privilege's ++++++++++++++++++++++++++++++++++

    sub_sub_menu_text = request.POST.getlist('sub_sub_menu_text[]')
    sub_sub_menu_link = request.POST.getlist('sub_sub_menu_link[]')
    sub_sub_menu_order = request.POST.getlist('sub_sub_menu_order[]')
    sub_sub_menu_acl_key = request.POST.getlist('sub_sub_menu_acl_key[]')
    sub_sub_menu_parent_acl_key = request.POST.getlist('sub_sub_menu_parent_acl_key[]')

    sub_sub_menu_app_name = request.POST.getlist('sub_sub_menu_app_name[]')
    sub_sub_menu_model_name = request.POST.getlist('sub_sub_menu_model_name[]')

    objs = []
    i = 0
    while i < len(sub_sub_menu_text):
        sub_sub_menu_views = 1 if request.POST.get("sub_sub_menu_view_%s" % i) == 'on' else 0
        sub_sub_menu_adds = 1 if request.POST.get("sub_sub_menu_add_%s" % i) == 'on' else 0
        sub_sub_menu_edits = 1 if request.POST.get("sub_sub_menu_edit_%s" % i) == 'on' else 0
        sub_sub_menu_deleted = 1 if request.POST.get("sub_sub_menu_delete_%s" % i) == 'on' else 0

        parent_menu = AclPermissions.objects.filter(role_id=role_id, acl_key=sub_sub_menu_parent_acl_key[i]).first()

        objs.extend([
            AclPermissions(
                role_id=role_id,
                link=sub_sub_menu_link[i],
                icon='',
                menu_text=sub_sub_menu_text[i],
                acl_key=sub_sub_menu_acl_key[i],
                level='2',
                ordering=sub_sub_menu_order[i],
                parent_menu=parent_menu.id,
                view=sub_sub_menu_views,
                add=sub_sub_menu_adds,
                edit=sub_sub_menu_edits,
                trash=sub_sub_menu_deleted,
                app_name=sub_sub_menu_app_name[i],
                model_name=sub_sub_menu_model_name[i],
            )
        ])
        i += 1

    msg = AclPermissions.objects.bulk_create(objs)

    messages.success(request, "Permission's set successfully...!")

    return HttpResponseRedirect('/admin/aclmanager?id=%s' % role_id)


def toolbarPermissions(user_id, acl_key):
    user_id = user_id
    acl_key = acl_key
    user_roles = UserRoles.objects.filter(user_id=user_id).all()
    acl_permission = AclPermissions.objects.filter(role_id__in=user_roles, acl_key=acl_key).first()
    return {'view': int(acl_permission.view) if acl_permission else 0, 'add': int(acl_permission.add) if acl_permission else 0, 'edit': int(acl_permission.edit) if acl_permission else 0,
            'publish': int(acl_permission.edit) if acl_permission else 0, 'unpublish': int(acl_permission.edit) if acl_permission else 0,
            'trash': int(acl_permission.trash) if acl_permission else 0}

    # return {'view': int(acl_permission.add) if acl_permission else 0, 'add': 1 if acl_permission else 0, 'edit': 1 if acl_permission else 0,
    #         'publish': 1 if acl_permission else 0, 'unpublish': 1 if acl_permission else 0,
    #         'trash': 1 if acl_permission else 0}


def signalTest(request):
    # return HttpResponse("signsl")
    # test = my_signal.send(sender="my_signal_receiver",my_signal_arg1="something", my_signal_arg_2="something else")
    # return HttpResponse(test)
    custom_data = request.META.get('CUSTOM_DATA_TO_VIEW')
    return HttpResponse(custom_data)


# Sidebar menu Population Methods
def getUserroles(user_id):
    user_roles = UserRoles.objects.filter(user_id=user_id).get()
    return {'user_roles': user_roles}
