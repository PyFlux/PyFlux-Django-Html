from dashboard.models import UserRoles
from dashboard.models import AclPermissions
from django.db import connection

def sidebar_menu(request):

    if(request.user.id):
        user_id = request.user.id
        user_roles = list(UserRoles.objects.filter(user_id=user_id).values_list("role_id", flat=True))

        # user_roles = UserRoles.objects.raw("SELECT * FROM dashboard_user_roles where user_id=1;")

        # cursor = connection.cursor()
        # cursor.execute("SELECT role_id FROM dashboard_user_roles where user_id=1")
        # row = list(cursor.fetchall())

        main_parent_menu = []
        sub_parent_menu = []
        sub_sub_parent_menu = []

        main_menu = AclPermissions.objects.filter(role_id__in=user_roles,view=1,level=0).order_by('ordering')

        for key in main_menu:
            main_parent_menu.append(key.id)

        sub_menu = AclPermissions.objects.filter(role_id__in=user_roles,parent_menu__in=main_parent_menu,view=1,level=1).order_by('ordering')

        for sub_key in sub_menu:
            sub_parent_menu.append(sub_key.id)

        sub_sub_menu = AclPermissions.objects.filter(role_id__in=user_roles,parent_menu__in=sub_parent_menu,view=1,level=2).order_by('ordering')

        for sub_sub_key in sub_sub_menu:
            sub_sub_parent_menu.append(sub_sub_key.id)

        return {
            'main_menu' : main_menu,
            'sub_menu' : sub_menu,
            'sub_sub_menu' : sub_sub_menu,
            'main_parent_menu': main_parent_menu,
            'sub_parent_menu': sub_parent_menu,
            'sub_sub_parent_menu': sub_sub_parent_menu,
        }

    else:
        return {
            'sidebar_menu': "User is not Logged In..!",

        }

