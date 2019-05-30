from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import CityTown
from systemconfig.forms.cityTown_form import *


class addCityTown(View):
    form_class = CityTownForm

    def get(self, request):
        page_title = "Add New City/Town"
        form = self.form_class
        return render(request, 'city/cityform.html', {'form': form, 'page_title': page_title})


class saveCityTown(View):
    form_class = CityTownForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New CityTown"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = CityTown()
                obj.city_name = form.cleaned_data['city_name']
                obj.city_country_id = form.cleaned_data['country_name']
                obj.city_state_id = form.cleaned_data['state_name']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'City/Town details saved successfully..!')
                return HttpResponseRedirect('/admin/list/citytown')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'city/cityform.html', {'form': form, page_title: 'page_title'})


class editCityTown(View):
    def get(self, request, **kwargs):
        page_title = "Edit CityTown"

        city_details = CityTown.objects.get(id=self.kwargs['edit_id'])
        form_class = CityTownForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'city/cityform.html',
                      {'form': form, 'page_title': page_title, 'city_details': city_details})


class updateCityTown(View):
    form_class = CityTownForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            city_country_id = form.cleaned_data['country_name']
            city_state_id = form.cleaned_data['state_name']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            CityTown.objects.filter(id=id).update(city_name=city_name, city_state_id=city_state_id,
                                                  city_country_id=city_country_id, status=status, updated_by=updated_by,
                                                  updated_at=updated_at)
            messages.success(request, 'CityTown details updated successfully..!')
            return HttpResponseRedirect('/admin/list/citytown')
        return HttpResponse("UpdateCityTown")
