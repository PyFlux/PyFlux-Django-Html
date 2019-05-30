from django.db import models
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.apps import apps
from django.utils.html import escape


def get_model_from_any_app(model_name):
    for app_config in apps.get_app_configs():
        try:
            model = app_config.get_model(model_name)
            return model
        except LookupError:
            pass
    return None


class Languages(models.Model, BaseDatatableView):
    class Meta:
        db_table = '"system_config_languages"'

    # Existing fields
    firm_id = models.IntegerField(null=True)
    dept_id = models.IntegerField(null=True)
    org_id = models.IntegerField(null=True)
    language_name = models.CharField(max_length=255)
    status = models.SmallIntegerField(default=1)
    created_by = models.CharField(max_length=10, null=True)
    updated_by = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    page_title = 'Manage Languages'
    listable = {'Languages': '', 'Status': ''}
    columns = ['id', 'language_name', 'status']
    order_columns = ['id', 'created_by', 'updated_by', 'created_at', 'updated_at', 'deleted_at']
    max_display_length = 500
    max_display_length = 500
    class_view_name = 'GetAjaxViewLanguage'

    table_name = "system_config_languages"

    model_name = "Country"
    acl_key = "pyflux.admin.Languages"

    parameter_array = {'acl_key': 'dashboard.admin.languages'}
    show_toolbar = {"view": "Show", "add": "Add", "edit": "Edit",
                    "publish": "Publish", "unpublish": "Unpublish",
                    "trash": "Trash", "restore": "Restore", "forcedelete": "Force Delete"}

    routes = {"add_route": "addlanguage", "edit_route": "editlanguage", "view_route": "viewlanguage"}

    advanced_filter = {"layout": "language/advancedfilter/languageformfilter.html",
                       'filters':
                           {
                               'filter_status': 'filter_status',
                               'filter_trashed': 'filter_trashed',
                           }
                       }


class GetAjaxViewLanguage(BaseDatatableView):

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
        else:
            return super(GetAjaxViewLanguage, self).render_column(row, column)

    def filter_queryset(self, qs):
        filter_trashed = self.request.GET.get(u'filter_trashed', None)

        if (filter_trashed == '1'):
            qs = qs.filter(deleted_at__isnull=False)
        else:
            qs = qs.filter(deleted_at__isnull=True)

        # if (filter_status != '-1'):
        #     qs = qs.filter(status=int(filter_status))
        # else:
        #     qs = qs

        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(email__istartswith=search)
        return qs
