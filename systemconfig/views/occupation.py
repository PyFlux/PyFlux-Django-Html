from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import Occupation
from systemconfig.forms.occupation_form import *


class addOccupation(View):
    form_class = OccupationForm

    def get(self, request):
        page_title = "Add New Occupation"
        form = self.form_class
        return render(request, 'occupation/occupationform.html', {'form': form, 'page_title': page_title})


class saveOccupation(View):
    form_class = OccupationForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Occupation"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = Occupation()
                obj.occupation = form.cleaned_data['occupation']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'occupation details saved successfully..!')
                return HttpResponseRedirect('/admin/list/occupation')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'occupation/occupationform.html', {'form': form, page_title: 'page_title'})


class editOccupation(View):
    def get(self, request, **kwargs):
        page_title = "Edit Occupation"

        occupation_details = Occupation.objects.get(id=self.kwargs['edit_id'])
        form_class = OccupationForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'occupation/occupationform.html',
                      {'form': form, 'page_title': page_title, 'occupation_details': occupation_details})


class updateOccupation(View):
    form_class = OccupationForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            occupation = form.cleaned_data['occupation']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            Occupation.objects.filter(id=id).update(occupation=occupation, status=status,
                                                    updated_by=updated_by,
                                                    updated_at=updated_at)
            messages.success(request, 'Occupation details updated successfully..!')
            return HttpResponseRedirect('/admin/list/occupation')
        return HttpResponse("UpdateOccupation")
