from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import Nationality
from systemconfig.forms.nationality_form import *


class addNationality(View):
    form_class = NationalityForm

    def get(self, request):
        page_title = "Add New Nationality"
        form = self.form_class
        return render(request, 'nationality/nationalityform.html', {'form': form, 'page_title': page_title})


class saveNationality(View):
    form_class = NationalityForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Nationality"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = Nationality()
                obj.nationality_name = form.cleaned_data['nationality_name']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'language details saved successfully..!')
                return HttpResponseRedirect('/admin/list/nationality')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'nationality/nationalityform.html', {'form': form, page_title: 'page_title'})


class editNationality(View):
    def get(self, request, **kwargs):
        page_title = "Edit Nationality"

        nationality_details = Nationality.objects.get(id=self.kwargs['edit_id'])
        form_class = NationalityForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'nationality/nationalityform.html',
                      {'form': form, 'page_title': page_title, 'nationality_details': nationality_details})


class updateNationality(View):
    form_class = NationalityForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            nationality_name = form.cleaned_data['nationality_name']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            Nationality.objects.filter(id=id).update(nationality_name=nationality_name, status=status,
                                                     updated_by=updated_by,
                                                     updated_at=updated_at)
            messages.success(request, 'Nationality details updated successfully..!')
            return HttpResponseRedirect('/admin/list/nationality')
        return HttpResponse("UpdateNationality")
