from django.db import models
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.apps import apps


def get_model_from_any_app(model_name):
    for app_config in apps.get_app_configs():
        try:
            model = app_config.get_model(model_name)
            return model
        except LookupError:
            pass
    return None

class Roles(models.Model):
    class Meta:
        db_table = '"dashboard_roles"'

    name = models.CharField(max_length=128)
    role_type = models.CharField(max_length=128)

    status = models.IntegerField(null=True, default=0)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    page_title = 'Manage Roles'
    listable = {'Name': '','Status': ''}
    columns = ['id','name','status']
    order_columns = ['id', 'name']
    max_display_length = 500
    class_view_name ='GetAjaxViewRoles'
    table_name = "dashboard_roles"
    model_name = "Roles"
    acl_key = "dashboard.admin.roles"
    parameter_array = {'acl_key': 'dashboard.admin.roles'}
    show_toolbar = {"view": "Show", "add": "Add", "edit": "Edit",
                    "publish": "Publish", "unpublish": "Unpublish",
                    "trash": "Trash", "restore": "Restore", "forcedelete": "Force Delete"}
    routes = {"add_route": "addrole", "edit_route": "editrole", "view_route": "viewrole"}
    advanced_filter = {"layout": "",
                       'filters':
                           {
                               'filter_status': 'filter_status',
                               'filter_trashed': 'filter_trashed',
                           }
                       }


class GetAjaxViewRoles(BaseDatatableView):

    def dispatch(self, request, *args, **kwargs):
        model_name = request.GET.get('model_name', '')
        self.model = get_model_from_any_app(model_name)
        self.columns = self.model.columns
        self.order_columns = self.model.order_columns
        self.max_display_length = self.model.max_display_length
        return super().dispatch(request, *args, **kwargs)


    def render_column(self, row, column):
        if column == 'id':
            return '<input type="checkbox" name="cid[]" value="%s" class="cid_checkbox flat"/>' % row.id
        elif column == 'status':
            return '<i class="fa fa-check"></i> Active' if row.status == 1 else '<i class="fa fa-times"></i> Inactive'
        else:
            return super(GetAjaxViewRoles, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)
        qs = qs.order_by('id')
        return qs