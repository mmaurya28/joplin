from django import template
from django.contrib.auth.models import Group
from groups.models import Department, AdditionalGroup

register = template.Library()


# Get the groups for a user
@register.filter(name='get_user_groups')
def get_user_groups(form):
    user_groups = form['groups'].value() or []
    roles = [g for g in list(Group.objects.filter(name__in=["Moderators", "Editors"]).values_list('id', flat=True)) if g in user_groups]
    department_groups = list(Department.objects.filter(pk__in=user_groups).values_list('id', flat=True))
    additional_groups = list(AdditionalGroup.objects.filter(pk__in=user_groups).values_list('id', flat=True))
    return {
        "roles": roles,
        "department_groups": department_groups,
        "additional_groups": additional_groups,
    }


# Get custom validation errors from our "department" and "roles" fields.
@register.filter(name='get_user_errors')
def get_user_errors(form):
    error_messages = {}
    if hasattr(form, "_errors") and form._errors:
        form_errors = form._errors
        if form_errors:
            department_errors = form_errors.get('department')
            if department_errors:
                error_messages["department"] = department_errors.data[0].message
            role_errors = form_errors.get('roles')
            if role_errors:
                error_messages["roles"] = role_errors.data[0].message
    return error_messages
