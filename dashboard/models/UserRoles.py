from django.db import models
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.apps import apps
from dashboard.models import Users, Roles
from django.db import connection, transaction


def get_model_from_any_app(model_name):
    for app_config in apps.get_app_configs():
        try:
            model = app_config.get_model(model_name)
            return model
        except LookupError:
            pass
    return None


class UserRoles(models.Model):
    class Meta:
        db_table = '"dashboard_user_roles"'

    user_id = models.BigIntegerField(null=True)
    role_id = models.BigIntegerField(null=True)

    status = models.IntegerField(null=True, default=0)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    page_title = 'Manage User Roles'
    listable = {'User': '', 'Roles': ''}
    columns = ['id', 'user_id', 'role_id']
    order_columns = ['id', 'user_id', 'role_id']
    max_display_length = 500
    class_view_name = 'GetAjaxViewUserRoles'
    table_name = "dashboard_user_roles"
    model_name = "UserRoles"
    acl_key = "dashboard.admin.userroles"
    parameter_array = {'acl_key': 'dashboard.admin.userroles'}
    show_toolbar = {"view": "Show", "add": "Add", "edit": "Edit",
                    "publish": "Publish", "unpublish": "Unpublish",
                    "trash": "Trash", "restore": "Restore", "forcedelete": "Force Delete"}

    routes = {"add_route": "adduserrole", "edit_route": "edituserrole", "view_route": "viewuserrole"}
    advanced_filter = {"layout": "",
                       'filters':
                           {
                               'filter_status': 'filter_status',
                               'filter_trashed': 'filter_trashed',
                           }
                       }

class GetAjaxViewUserRoles(BaseDatatableView):

    def dispatch(self, request, *args, **kwargs):
        model_name = request.GET.get('model_name', '')
        self.model = get_model_from_any_app(model_name)
        self.columns = self.model.columns
        self.order_columns = self.model.order_columns
        self.max_display_length = self.model.max_display_length
        return super().dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        return UserRoles.objects.distinct('user_id')

    def render_column(self, row, column):
        if column == 'id':
            return '<input type="checkbox" name="cid[]" value="%s" class="cid_checkbox flat"/>' % row.id
        elif column == 'user_id':
            user_details = Users.objects.filter(id=row.user_id).first()
            user_name = str(user_details.first_name) + " " + str(user_details.last_name)
            return user_name
        elif column == 'role_id':
            cursor = connection.cursor()
            cursor.execute(
            " select STRING_AGG(name, ', ') as role_names "+
            " from ( "+
                    " select r.name from dashboard_user_roles ur "+
                    " left join dashboard_roles r on r.id = ur.role_id "+
                    " left join auth_user u on u.id = ur.user_id "+
                    " where ur.user_id = %s group by r.id order by r.id asc"+
                ") as roles",
                [row.user_id]
            )
            roles = cursor.fetchone()
            return roles
        else:
            return super(GetAjaxViewUserRoles, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(email__istartswith=search)
        return qs
