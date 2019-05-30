from django.db import models


class UserProfiles(models.Model):
    class Meta:
        db_table = '"dashboard_user_profiles"'

    user_id = models.BigIntegerField(null=True)
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    address = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=128, null=True)
    zip = models.CharField(max_length=128, null=True)
    media = models.CharField(max_length=255, null=True, default='test')

    status = models.IntegerField(null=True, default=0)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
