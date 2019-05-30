from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views import View
from systemconfig.models import Relationship
from systemconfig.forms.relationship_form import *


class addRelationship(View):
    form_class = RelationshipForm

    def get(self, request):
        page_title = "Add New Relationship"
        form = self.form_class
        return render(request, 'relationship/relationshipform.html', {'form': form, 'page_title': page_title})


class saveRelationship(View):
    form_class = RelationshipForm

    def post(self, request):
        if request.method == 'POST':
            page_title = "Add New Relationship"
            form = self.form_class(request.POST)
            if form.is_valid():
                obj = Relationship()
                obj.name = form.cleaned_data['name']
                obj.status = form.cleaned_data['status']
                obj.created_by = request.user.id
                obj.created_at = datetime.now()
                obj.save()
                messages.success(request, 'Relationship details saved successfully..!')
                return HttpResponseRedirect('/admin/list/relationship')

        else:
            form = self.form_class()
        messages.error(request, 'Error..!')
        return render(request, 'relationship/relationshipform.html', {'form': form, page_title: 'page_title'})


class editRelationship(View):
    def get(self, request, **kwargs):
        page_title = "Edit Relationship"

        relationship_details = Relationship.objects.get(id=self.kwargs['edit_id'])
        form_class = RelationshipForm
        if request.method == 'POST':
            form = form_class(request.POST)
        else:
            form = form_class()
        return render(request, 'relationship/relationshipform.html',
                      {'form': form, 'page_title': page_title, 'relationship_details': relationship_details})


class updateRelationship(View):
    form_class = RelationshipForm

    def post(self, request, **kwargs):
        id = request.POST.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            status = form.cleaned_data['status']
            updated_by = request.user.id
            updated_at = datetime.now()
            Relationship.objects.filter(id=id).update(name=name, status=status,
                                                      updated_by=updated_by,
                                                      updated_at=updated_at)
            messages.success(request, 'Relationship details updated successfully..!')
            return HttpResponseRedirect('/admin/list/relationship')
        return HttpResponse("UpdateRelationship")
