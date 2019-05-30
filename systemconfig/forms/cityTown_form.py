from django import forms
from django.db import connection
from systemconfig.models import Country, State


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


class CityTownForm(forms.Form):
    city_name = forms.CharField(label='City/Town', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))

    cursor = connection.cursor()
    cursor.execute(
        "SELECT EXISTS ( "
        " SELECT 1 " +
        " FROM   information_schema.tables " +
        " WHERE  table_schema = 'public' " +
        " AND    table_name = 'system_config_country' " +
        " ) "
    )
    table_status = cursor.fetchone()
    if (str(table_status[0]) == "True"):
        country_name = forms.ChoiceField(label='Country', required="required",
                                         choices=[(e.id, e.country_name) for e in
                                                  Country.objects.filter()])
    else:
        print("Country Table Not exist...")

    cursor = connection.cursor()
    cursor.execute(
        "SELECT EXISTS ( "
        " SELECT 1 " +
        " FROM   information_schema.tables " +
        " WHERE  table_schema = 'public' " +
        " AND    table_name = 'system_config_state' " +
        " ) "
    )
    table_status = cursor.fetchone()
    if (str(table_status[0]) == "True"):
        state_name = forms.ChoiceField(label='State', required="required",
                                       choices=[(e.id, e.state_name) for e in
                                                State.objects.filter()])
    else:
        print("State Table Not exist...")
