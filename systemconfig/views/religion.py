from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import Religion
from systemconfig.forms.religion_form import *


class addReligion(View):
    form_class = ReligionForm

    def get(self, request):
        page_title = "Add New Religion"
        form = self.form_class
        return render(request, 'religion/religionform.html', {'form': form, 'page_title': page_title})


class saveReligion(View):
    form_class = ReligionForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Religion"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = Religion()
                obj.student_religion = form.cleaned_data['student_religion']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'Religion details saved successfully..!')
                return HttpResponseRedirect('/admin/list/religion')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'religion/religionform.html', {'form': form, page_title: 'page_title'})


class editReligion(View):
    def get(self, request, **kwargs):
        page_title = "Edit Religion"

        religion_details = Religion.objects.get(id=self.kwargs['edit_id'])
        form_class = ReligionForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'religion/religionform.html',
                      {'form': form, 'page_title': page_title, 'religion_details': religion_details})


class updateReligion(View):
    form_class = ReligionForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            student_religion = form.cleaned_data['student_religion']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            Religion.objects.filter(id=id).update(student_religion=student_religion, status=status,
                                                  updated_by=updated_by,
                                                  updated_at=updated_at)
            messages.success(request, 'Religion details updated successfully..!')
            return HttpResponseRedirect('/admin/list/religion')
        return HttpResponse("UpdateReligion")
