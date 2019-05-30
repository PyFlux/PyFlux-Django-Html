from django import template
from dashboard.models import Users
from dashboard.models import AclPermissions

register = template.Library()


@register.simple_tag
def menuCheck():
    view = 1
    add = 1
    edit = 1
    publish = 1
    unpublish = 1
    trash = 1
    return {'view': view, 'add': add, 'edit': edit, 'publish': publish, 'unpublish': unpublish, 'trash': trash}


@register.simple_tag
def levelZero(main_menu_key, acl_key, role_id):
    main_menu_data = AclPermissions.objects.filter(acl_key=acl_key, role_id=role_id, level=0).first()
    if (main_menu_key):
        main_menu_key = main_menu_key
    else:
        main_menu_key = "No Key Set"
    return {'main_menu_key': main_menu_key}


@register.simple_tag
def levelOne(sub_menu_key, acl_key, role_id):
    main_menu_data = AclPermissions.objects.filter(acl_key=acl_key, role_id=role_id, level=1).first()
    if (sub_menu_key):
        sub_menu_key = sub_menu_key
    else:
        sub_menu_key = "No Key Set"

    return {'sub_menu_key': sub_menu_key}


@register.simple_tag
def levelTwo(acl_key, role_id):
    sub_sub_menu_data = AclPermissions.objects.filter(acl_key=acl_key, role_id=role_id, level=1).first()
    return {'sub_sub_menu_data': sub_sub_menu_data}


@register.tag(name='incrementmaincounter')
def increment_var(parser, token):
    parts = token.split_contents()
    if len(parts) < 2:
        raise template.TemplateSyntaxError("'increment' tag must be of the form:  {% increment <var_name> %}")
    return IncrementVarNode(parts[1])


register.tag('++', increment_var)


class IncrementVarNode(template.Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        try:
            value = context[self.var_name]
            context[self.var_name] = value + 1
            return u""
        except:
            raise template.TemplateSyntaxError("The variable does not exist.")


@register.tag(name='incrementsubcounter')
def increment_var(parser, token):
    parts = token.split_contents()
    if len(parts) < 2:
        raise template.TemplateSyntaxError("'increment' tag must be of the form:  {% increment <var_name> %}")
    return IncrementVarNode(parts[1])


register.tag('++', increment_var)


class IncrementVarNode(template.Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        try:
            value = context[self.var_name]
            context[self.var_name] = value + 1
            return u""
        except:
            raise template.TemplateSyntaxError("The variable does not exist.")


@register.simple_tag
def define(val=None):
    return val


@register.simple_tag


def set_local_var(local_vars, name, value):
    local_vars[name] = value
    return ''


# env.globals['set_local_var'] = set_local_var
# # ---------------------------------------------
# return env.get_template('template.html').render(items=items, local_vars=local_vars)
