from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from dashboard.models import Roles
from dashboard.forms.role_form import *


class addRole(View):
    form_class = RoleForm

    def get(self, request):
        page_title = "Add New Role"
        form = self.form_class
        return render(request, 'roles/roleform.html', {'form': form, 'page_title': page_title})


class saveRole(View):
    form_class = RoleForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Role"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = Roles()
                obj.name = form.cleaned_data['role_name']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'Role details saved successfully..!')
                return HttpResponseRedirect('/admin/list/roles')
        else:
            form = self.form_class()
        messages.error(request, 'Something went wrong..!')
        return render(request, 'roles/roleform.html', {'form': form, page_title: 'page_title'})


class editRole(View):
    def get(self, request, **kwargs):
        page_title = "Edit Role"
        role_details = Roles.objects.get(id=self.kwargs['edit_id'])
        form_class = RoleForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'roles/roleform.html',
                      {'form': form, 'page_title': page_title, 'role_details': role_details})


class updateRole(View):
    form_class = RoleForm

    def post(self, request, **kwargs):
        role_id = request.POST.get('role_id')
        form = self.form_class(request.POST)
        if form.is_valid():
            role_name = form.cleaned_data['role_name']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            Roles.objects.filter(id=role_id).update(name=role_name, status=status, updated_by=updated_by,
                                                         updated_at=updated_at)
            messages.success(request, 'Role details updated successfully..!')
            return HttpResponseRedirect('/admin/list/roles')
        else:
            form = self.form_class()
            page_title = "Edit Role"
            messages.error(request, 'Something went wrong..!')
            role_details = Roles.objects.get(id=role_id)
            return render(request, 'roles/roleform.html',
                      {'form': form, 'page_title': page_title, 'role_details': role_details})
