from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from dashboard.forms import addUserForm
from django.contrib.auth.models import User
from dashboard.models import Users
from django.contrib import messages
from django.views import View
from datetime import datetime


class addUser(View):
    form_class = addUserForm

    def get(self, request):
        page_title = "Add User"
        form = self.form_class
        return render(request, 'users/usersform.html', {'form': form, 'page_title': page_title})


class saveUser(View):
    form_class = addUserForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add User"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = User()
                obj.username = form.cleaned_data['username']
                obj.first_name = form.cleaned_data['first_name']
                obj.last_name = form.cleaned_data['last_name']
                obj.email = form.cleaned_data['email']
                obj.status = 1
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'User details saved successfully..!')
                return HttpResponseRedirect('/admin/list/users')
        else:
            form = self.form_class()
        messages.error(request, 'Something went wrong..!')
        return render(request, 'users/usersform.html', {'form': form, page_title: 'page_title'})


class editUser(View):
    def get(self, request, **kwargs):
        page_title = "Edit User"

        user_details = Users.objects.get(id=self.kwargs['edit_id'])
        form_class = addUserForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'users/usersform.html',
                      {'form': form, 'page_title': page_title, 'user_details': user_details})


class updateUser(View):
    form_class = addUserForm

    def post(self, request, **kwargs):
        user_id = request.POST.get('user_id')
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            updated_by = request.user.id
            updated_at = datetime.now()
            Users.objects.filter(id=user_id).update(username=username, first_name=first_name, last_name=last_name,
                                              email=email, updated_by=updated_by,
                                              updated_at=updated_at)
            messages.success(request, 'User details updated successfully..!')
            return HttpResponseRedirect('/admin/list/users')
        else:
            form = self.form_class()
            page_title = "Edit User"
            messages.error(request, 'Something went wrong..!')
            user_details = Users.objects.get(id=user_id)
            return render(request, 'users/usersform.html',
                      {'form': form, 'page_title': page_title, 'user_details': user_details})
