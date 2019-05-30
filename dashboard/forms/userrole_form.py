from django import forms
from django.db import connection
from dashboard.models import Roles, Users


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


class UserroleForm(forms.Form):

    def db_table_exists(auth_user):
        user_id = forms.ChoiceField(label='Users', required="required",
                                    choices=[(role.id, str(role.first_name) + ' ' + str(role.last_name)) for role in
                                             Users.objects.filter(status=1).order_by('id')])

    def db_table_exists(dashboard_roles):
        role_id = forms.ChoiceField(label='Roles', required="required",
                                    choices=[(role.id, str(role.name)) for role in
                                             Roles.objects.filter(status=1).order_by('id')])

    def clean(self):
        cleaned_data = super(UserroleForm, self).clean()
        user_id = cleaned_data.get('user_id')
        role_id = cleaned_data.get('role_id')
        if not user_id and not role_id:
            raise forms.ValidationError('There are errors in the fields...!')
