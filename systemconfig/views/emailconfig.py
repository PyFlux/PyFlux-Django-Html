from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import EmailConfig
from systemconfig.forms.emailconfig_form import *


class addEmailConfig(View):
    form_class = EmailConfigForm

    def get(self, request):
        page_title = "Add New Email Config"
        form = self.form_class
        return render(request, 'emailconfig/emailconfigform.html', {'form': form, 'page_title': page_title})


class saveEmailConfig(View):
    form_class = EmailConfigForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Email Config"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = EmailConfig()
                obj.per_day = form.cleaned_data['per_day']
                obj.per_month = form.cleaned_data['per_month']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'Email Config details saved successfully..!')
                return HttpResponseRedirect('/admin/list/emailconfig')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'emailconfig/emailconfigform.html', {'form': form, page_title: 'page_title'})


class editEmailConfig(View):
    def get(self, request, **kwargs):
        page_title = "Edit Email Config"

        emailconfig_details = EmailConfig.objects.get(id=self.kwargs['edit_id'])
        form_class = EmailConfigForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'emailconfig/emailconfigform.html',
                      {'form': form, 'page_title': page_title, 'emailconfig_details': emailconfig_details})


class updateEmailConfig(View):
    form_class = EmailConfigForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            per_day = form.cleaned_data['per_day']
            per_month = form.cleaned_data['per_month']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            EmailConfig.objects.filter(id=id).update(per_day=per_day, per_month=per_month, status=status,
                                                     updated_by=updated_by,
                                                     updated_at=updated_at)
            messages.success(request, 'EmailConfig details updated successfully..!')
            return HttpResponseRedirect('/admin/list/emailconfig')
        return HttpResponse("UpdateEmailConfig")
