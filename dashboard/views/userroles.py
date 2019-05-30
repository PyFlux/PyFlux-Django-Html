from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from dashboard.models import UserRoles, Roles, Users
from dashboard.forms.userrole_form import *


class addUserrole(View):
    form_class = UserroleForm

    def get(self, request):
        page_title = "Assign Role to User"
        form = self.form_class
        return render(request, 'userrole/userrole_form.html',
                      {'form': form, 'page_title': page_title})


class saveUserrole(View):
    form_class = UserroleForm

    def post(self, request):
        page_title = "Assign Role to User"
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = UserRoles()
                obj.user_id = form.cleaned_data['user_id']
                obj.role_id = form.cleaned_data['role_id']
                obj.status = 1
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'Role to User assigned successfully..!')
                return HttpResponseRedirect('/admin/list/userroles')
        else:
            form = self.form_class()
        messages.error(request, 'Something went wrong..!')
        return render(request, 'userrole/userrole_form.html', {'form': form, page_title: 'page_title'})


class editUserrole(View):
    def get(self, request, **kwargs):
        page_title = "Edit Role to User"

        userrole_details = UserRoles.objects.get(id=self.kwargs['edit_id'])
        form_class = UserroleForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'userrole/userrole_form.html',
                      {'form': form, 'page_title': page_title, 'userrole_details': userrole_details})


class updateUserrole(View):
    form_class = UserroleForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            role_name = form.cleaned_data['role_name']
            role_country_id = form.cleaned_data['country_name']
            role_state_id = form.cleaned_data['state_name']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            UserRoles.objects.filter(id=id).update(role_name=role_name, role_state_id=role_state_id,
                                                   role_country_id=role_country_id, status=status,
                                                   updated_by=updated_by,
                                                   updated_at=updated_at)
            messages.success(request, 'Userrole details updated successfully..!')
            return HttpResponseRedirect('/admin/list/userroles')
        return HttpResponse("UpdateUserrole")
