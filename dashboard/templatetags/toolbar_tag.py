from django import template
from dashboard.models import Users

register = template.Library()

@register.simple_tag
def toolbarPermissions():
    view = 1
    add = 1
    edit =1
    publish =1
    unpublish =1
    trash =1
    return {'view': view, 'add': add, 'edit' : edit,'publish' : publish,'unpublish' : unpublish,'trash' : trash}
