from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import SmsConfig
from systemconfig.forms.smsconfig_form import *


class addSmsConfig(View):
    form_class = SmsConfigForm

    def get(self, request):
        page_title = "Add New Sms Config"
        form = self.form_class
        return render(request, 'smsconfig/smsconfigform.html', {'form': form, 'page_title': page_title})


class saveSmsConfig(View):
    form_class = SmsConfigForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Sms Config"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = SmsConfig()
                obj.sms_count = form.cleaned_data['sms_count']
                obj.api_key = form.cleaned_data['api_key']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'Email Config details saved successfully..!')
                return HttpResponseRedirect('/admin/list/smsconfig')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'smsconfig/smsconfigform.html', {'form': form, page_title: 'page_title'})


class editSmsConfig(View):
    def get(self, request, **kwargs):
        page_title = "Edit Sms Config"

        smsconfig_details = SmsConfig.objects.get(id=self.kwargs['edit_id'])
        form_class = SmsConfigForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'smsconfig/smsconfigform.html',
                      {'form': form, 'page_title': page_title, 'smsconfig_details': smsconfig_details})


class updateSmsConfig(View):
    form_class = SmsConfigForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            sms_count = form.cleaned_data['sms_count']
            api_key = form.cleaned_data['api_key']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            SmsConfig.objects.filter(id=id).update(sms_count=sms_count, api_key=api_key,
                                                   status=status,
                                                   updated_by=updated_by,
                                                   updated_at=updated_at)
            messages.success(request, 'Sms Config details updated successfully..!')
            return HttpResponseRedirect('/admin/list/smsconfig')
        return HttpResponse("UpdateSmsConfig")
