from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import State
from systemconfig.forms.state_form import *


class addState(View):
    form_class = StateForm

    def get(self, request):
        page_title = "Add New State"
        form = self.form_class
        return render(request, 'state/stateform.html', {'form': form, 'page_title': page_title})


class saveState(View):
    form_class = StateForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New State"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = State()
                obj.state_name = form.cleaned_data['state_name']
                obj.state_country_id = form.cleaned_data['country_name']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'State details saved successfully..!')
                return HttpResponseRedirect('/admin/list/state')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'state/stateform.html', {'form': form, page_title: 'page_title'})


class editState(View):
    def get(self, request, **kwargs):
        page_title = "Edit State"

        state_details = State.objects.get(id=self.kwargs['edit_id'])
        form_class = StateForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'state/stateform.html',
                      {'form': form, 'page_title': page_title, 'state_details': state_details})


class updateState(View):
    form_class = StateForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            state_name = form.cleaned_data['state_name']
            state_country_id = form.cleaned_data['country_name']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            State.objects.filter(id=id).update(state_name=state_name, state_country_id=state_country_id, status=status,
                                               updated_by=updated_by,
                                               updated_at=updated_at)
            messages.success(request, 'State details updated successfully..!')
            return HttpResponseRedirect('/admin/list/state')
        return HttpResponse("UpdateState")
