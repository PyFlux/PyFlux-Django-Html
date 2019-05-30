from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import Languages
from systemconfig.forms.language_form import *


class addLanguage(View):
    form_class = LanguageForm

    def get(self, request):
        page_title = "Add New Languages"
        form = self.form_class
        return render(request, 'language/languageform.html', {'form': form, 'page_title': page_title})


class saveLanguage(View):
    form_class = LanguageForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Languages"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = Languages()
                obj.language_name = form.cleaned_data['language_name']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'language details saved successfully..!')
                return HttpResponseRedirect('/admin/list/languages')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'language/languageform.html', {'form': form, page_title: 'page_title'})


class editLanguage(View):
    def get(self, request, **kwargs):
        page_title = "Edit Languages"

        language_details = Languages.objects.get(id=self.kwargs['edit_id'])
        form_class = LanguageForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'language/languageform.html',
                      {'form': form, 'page_title': page_title, 'language_details': language_details})


class updateLanguage(View):
    form_class = LanguageForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            language_name = form.cleaned_data['language_name']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            Languages.objects.filter(id=id).update(language_name=language_name, status=status, updated_by=updated_by,
                                                   updated_at=updated_at)
            messages.success(request, 'Language details updated successfully..!')
            return HttpResponseRedirect('/admin/list/languages')
        return HttpResponse("UpdateLanguage")
