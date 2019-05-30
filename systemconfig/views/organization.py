from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import Organization
from systemconfig.forms.organization_form import *


class addOrganization(View):
    form_class = OrganizationForm

    def get(self, request):
        page_title = "Add New Organization"
        form = self.form_class
        return render(request, 'organization/organizationform.html', {'form': form, 'page_title': page_title})


class saveOrganization(View):
    form_class = OrganizationForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Organization"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = Organization()
                obj.org_name = form.cleaned_data['org_name']
                obj.org_alias = form.cleaned_data['org_alias']
                obj.org_address_line1 = form.cleaned_data['org_address_line1']
                obj.org_address_line2 = form.cleaned_data['org_address_line2']
                obj.org_phone = form.cleaned_data['org_phone']
                obj.org_email = form.cleaned_data['org_email']
                obj.org_website = form.cleaned_data['org_website']
                obj.org_logo = form.cleaned_data['org_logo']
                obj.org_logo_type = form.cleaned_data['org_logo_type']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'Organization details saved successfully..!')
                return HttpResponseRedirect('/admin/list/organization')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'organization/organizationform.html', {'form': form, page_title: 'page_title'})


class editOrganization(View):
    def get(self, request, **kwargs):
        page_title = "Edit Organization"

        organization_details = Organization.objects.get(id=self.kwargs['edit_id'])
        form_class = OrganizationForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'organization/organizationform.html',
                      {'form': form, 'page_title': page_title, 'organization_details': organization_details})


class updateOrganization(View):
    form_class = OrganizationForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                org_name = form.cleaned_data['org_name']
                org_alias = form.cleaned_data['org_alias']
                org_address_line1 = form.cleaned_data['org_address_line1']
                org_address_line2 = form.cleaned_data['org_address_line2']
                org_phone = form.cleaned_data['org_phone']
                org_email = form.cleaned_data['org_email']
                org_website = form.cleaned_data['org_website']
                org_logo = form.cleaned_data['org_logo']
                org_logo_type = form.cleaned_data['org_logo_type']
                status = form.cleaned_data['status']
                updated_by = request.user.id
                updated_at = datetime.now()
                Organization.objects.filter(id=id).update(org_name=org_name, org_alias=org_alias,
                                                          org_address_line1=org_address_line1, org_phone=org_phone,
                                                          org_email=org_email, org_website=org_website,
                                                          org_address_line2=org_address_line2, status=status,
                                                          org_logo=org_logo, org_logo_type=org_logo_type,
                                                          updated_by=updated_by,
                                                          updated_at=updated_at)
                messages.success(request, 'Organization details updated successfully..!')
                return HttpResponseRedirect('/admin/list/country')
            return HttpResponse("UpdateOrganization")
