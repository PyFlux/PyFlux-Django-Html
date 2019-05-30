from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import Country
from systemconfig.forms.country_form import *


class addCountry(View):
    form_class = CountryForm

    def get(self, request):
        page_title = "Add New Country"
        form = self.form_class
        return render(request, 'country/countryform.html', {'form': form, 'page_title': page_title})


class saveCountry(View):
    form_class = CountryForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Country"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = Country()
                obj.country_name = form.cleaned_data['country_name']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'Country details saved successfully..!')
                return HttpResponseRedirect('/admin/list/country')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'country/countryform.html', {'form': form, page_title: 'page_title'})


class editCountry(View):
    def get(self, request, **kwargs):
        page_title = "Edit Country"

        country_details = Country.objects.get(id=self.kwargs['edit_id'])
        form_class = CountryForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'country/countryform.html',
                      {'form': form, 'page_title': page_title, 'country_details': country_details})


class updateCountry(View):
    form_class = CountryForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            country_name = form.cleaned_data['country_name']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            Country.objects.filter(id=id).update(country_name=country_name, status=status, updated_by=updated_by,
                                                 updated_at=updated_at)
            messages.success(request, 'Country details updated successfully..!')
            return HttpResponseRedirect('/admin/list/country')
        return HttpResponse("UpdateCountry")
