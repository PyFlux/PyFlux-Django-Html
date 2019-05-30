from django.db import models


class AclPermissions(models.Model):
    class Meta:
        db_table = '"dashboard_acl_permissions"'

    role_id = models.BigIntegerField(null=True)
    menu_text = models.CharField(max_length=128)
    link = models.CharField(max_length=128)
    icon = models.CharField(max_length=128, null=True ) # Fontawesome Icon
    acl_key = models.CharField(max_length=128, null=True )
    parent_menu = models.CharField(max_length=128, null=True )
    level = models.CharField(max_length=128, null=True )
    ordering = models.CharField(max_length=128, null=True )
    add = models.CharField(max_length=128, null=True )
    edit = models.CharField(max_length=128, null=True )
    view = models.CharField(max_length=128, null=True )
    trash = models.CharField(max_length=128, null=True )
    approval_level_1 = models.CharField(max_length=128, null=True )
    approval_level_2 = models.CharField(max_length=128, null=True )

    app_name = models.CharField(max_length=128, null=True )
    model_name = models.CharField(max_length=128, null=True )

    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
