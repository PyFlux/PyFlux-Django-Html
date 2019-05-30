from django import forms
from django.db import connection
from dashboard.models import Roles


def db_table_exists(table, cursor=None):
    try:
        if not cursor:
            from django.db import connection
            cursor = connection.cursor()
        if not cursor:
            raise Exception
        table_names = connection.introspection.get_table_list(cursor)
    except:
        raise Exception("unable to determine if the table '%s' exists" % table)
    else:
        return table in table_names


class RoleForm(forms.Form):
    role_name = forms.CharField(label='Role', required="required", max_length=254)
    # role_type = forms.CharField(label='Role Type', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required",choices=((1,'Publish'),(0,'Unpublish')))

    cursor = connection.cursor()
    cursor.execute(
        "SELECT EXISTS ( "
        " SELECT 1 " +
        " FROM   information_schema.tables " +
        " WHERE  table_schema = 'public' " +
        " AND    table_name = 'dashboard_roles' " +
        " ) "
    )

    # table_status = cursor.fetchone()
    # if (str(table_status[0]) == "True"):
    #     country_name = forms.ChoiceField(label='Country', required="required",
    #                                      choices=[(e.id, e.country_name) for e in
    #                                               Country.objects.filter()])
    # else:
    #     print("Roles Table Not exist...")

    # cursor = connection.cursor()
    # cursor.execute(
    #     "SELECT EXISTS ( "
    #     " SELECT 1 " +
    #     " FROM   information_schema.tables " +
    #     " WHERE  table_schema = 'public' " +
    #     " AND    table_name = 'dashboard_roles' " +
    #     " ) "
    # )
    # table_status = cursor.fetchone()
    # if (str(table_status[0]) == "True"):
    #     state_name = forms.ChoiceField(label='State', required="required",
    #                                    choices=[(e.id, e.state_name) for e in
    #                                             State.objects.filter()])
    # else:
    #     print("Roles Table Not exist...")
