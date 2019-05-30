from django.db import models
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.apps import apps
from django.utils.html import escape
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import UserManager
import datetime
from django.utils import timezone


def get_model_from_any_app(model_name):
    for app_config in apps.get_app_configs():
        try:
            model = app_config.get_model(model_name)
            return model
        except LookupError:
            pass
    return None


class Users(AbstractBaseUser):
    class Meta:
        db_table = '"auth_user"'

    username = models.CharField(max_length=128, null=True, unique=True, )
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # notice the absence of a "Password field", that's built in.
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Added fields
    status = models.IntegerField(null=True, default=0)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Email & Password are required by default.

    objects = UserManager()

    page_title = 'Manage Users'
    listable = {'Name': '', 'Username': '', 'Email': '', 'Status': ''}
    columns = ['id', 'first_name', 'username', 'email', 'status']
    order_columns = ['id', 'username', 'first_name', 'last_name', 'email', 'status']
    max_display_length = 500
    class_view_name = 'GetAjaxViewUser'
    table_name = "auth_user"
    model_name = "Users"
    acl_key = "dashboard.admin.users"
    parameter_array = {'acl_key': 'dashboard.admin.users'}
    show_toolbar = {"view": "Show", "add": "Add", "edit": "Edit",
                    "publish": "Publish", "unpublish": "Unpublish",
                    "trash": "Trash", "restore": "Restore", "forcedelete": "Force Delete"}
    routes = {"add_route": "adduser", "edit_route": "edituser", "view_route": "viewuser"}
    advanced_filter = {"layout": "users/advancedfilters/userfilter.html",
                       'filters':
                           {
                               'filter_status': 'filter_status',
                               'filter_trashed': 'filter_trashed',
                           }
                       }


class GetAjaxViewUser(BaseDatatableView):
    # model = Roles
    # columns = model.columns
    # order_columns = model.order_columns
    # max_display_length = model.max_display_length

    def dispatch(self, request, *args, **kwargs):
        model_name = request.GET.get('model_name', '')
        # self.model = apps.get_model(
        #     app_label= 'Dashboard', #request.GET.get('app_label', ''),
        #     model_name=request.GET.get('model_name', ''))
        self.model = get_model_from_any_app(model_name)
        self.columns = self.model.columns
        self.order_columns = self.model.order_columns
        self.max_display_length = self.model.max_display_length
        return super().dispatch(request, *args, **kwargs)

    # def get_initial_queryset(self):
    #     model_name = self.request.GET['model_name']
    #     model = get_model_from_any_app(model_name)
    #     columns = model.columns
    #     order_columns = model.order_columns
    #     max_display_length = model.max_display_length
    #     return model.objects.all()

    def render_column(self, row, column):
        if column == 'id':
            return '<input type="checkbox" name="cid[]" value="%s" class="cid_checkbox flat"/>' % row.id
        elif column == 'first_name':
            return str(row.first_name) + ' ' + str(row.last_name)
        elif column == 'status':
            return '<i class="fa fa-check"></i> Active' if row.status == 1 else '<i class="fa fa-times"></i> Inactive'
        else:
            return super(GetAjaxViewUser, self).render_column(row, column)

    def filter_queryset(self, qs):
        filter_trashed = self.request.GET.get(u'filter_trashed', None)
        filter_status = self.request.GET.get(u'filter_status', None)
        ''' Trash Filter '''
        if (filter_trashed == '1'):
            qs = qs.filter(deleted_at__isnull=False)
        else:
            qs = qs.filter(deleted_at__isnull=True)
        ''' Status Filter '''
        if (filter_status == '1'):
            qs = qs.filter(status=int(filter_status))
        if (filter_status == '0'):
            qs = qs.filter(status=int(filter_status))
        ''' Search Query Filter '''
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(email__istartswith=search)
        return qs

    # def prepare_results(self, qs):
    #     json_data = []
    #     for item in qs:
    #         json_data.append([
    #             escape(item.id),
    #             escape(item.username),
    #             escape(item.first_name),
    #             escape(item.last_name),
    #             escape(item.email),
    #         ])
    #     return json_data
