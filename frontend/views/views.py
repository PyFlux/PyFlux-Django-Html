from django.shortcuts import render
from frontend.forms.user_register import *
from frontend.forms.user_login import *
from frontend.forms.user_telethonapi import *
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from frontend.models import *
from dashboard.models import *
from django.http import HttpResponse
from telethon import TelegramClient, events, sync
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from django.views import View
from django.contrib.auth import authenticate, login
import os
import os.path
from django.conf import settings
import csv


class websiteroot(View):
    def get(self, request):
        return render(request, 'website/website_root.jinja.html')


class userregister(View):
    form_class = userRegister

    def get(self, request):
        page_title = "Add New User"
        form = self.form_class
        return render(request, 'userregistration/userregistrationform.jinja.html',
                      {'form': form, 'registerForm': userRegister(), 'page_title': page_title})


class userregisteraction(View):
    form_class = userRegister

    def post(self, request):
        page_title = "Add New User"
        if request.method == 'POST':
            form = self.form_class(request.POST)
            print("Form post data")
            if form.is_valid():
                print("Form is valid now")
                obj = User()
                obj.username = form.cleaned_data['username']
                obj.first_name = form.cleaned_data['full_name']
                obj.email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                obj.status = 0
                obj.set_password(password)
                obj.save()
                messages.success(request, 'User details saved successfully..!')
                return render(request, 'userlogin/userloginform.jinja.html',
                              {'form': form, 'registerForm': userRegister(), 'page_title': page_title,
                               'message': 'User saved successfully'})
            else:
                print(form)
                return render(request, 'userregistration/userregistrationform.jinja.html',
                              {'form': form, 'registerForm': userRegister(), 'page_title': page_title,
                               'message': 'Error in form..!'})
        else:
            form = self.form_class()
        return render(request, 'userregistration/userregistrationform.jinja.html',
                      {'form': form, 'registerForm': userRegister(), 'page_title': page_title,
                       'message': 'Errors in the form...!'})


class userlogin(View):
    form_class = userLogin

    def get(self, request):
        page_title = "Login"
        message = ""
        form = self.form_class
        if request.user.is_authenticated:
            return HttpResponseRedirect('/userdashboard')
        else:
            return render(request, 'userlogin/userloginform.jinja.html',
                      {'form': form, 'page_title': page_title, 'message': message})


class usertelegramapi(View):
    form_class = userTelethonapi

    def get(self, request):
        page_title = "Add API details"
        print(request.user)
        form = self.form_class
        return render(request, 'usertelethonapi/usertelethonapiform.jinja.html',
                      {'form': form, 'telethonapiForm': userTelethonapi(), 'page_title': page_title})




def userloginCheck(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/userdashboard')
    else:
        return render(request, 'userlogin/userloginform.jinja.html', {'message': 'Invalid Username or Password ...!'})


def groupUsers(request):
    group_link = request.GET.get('group_link', '')
    return HttpResponse(group_link)




class userdashboard(View):
    def get(self, request):
        user_session_folder = settings.BASE_DIR + '/media/user_sessions/' + str(request.user.id)
        if not os.path.exists(user_session_folder):
            os.makedirs(user_session_folder)
        message = "Authorized already. You are good to go..!"
        authorization_status = 1
        return render(request, 'userdashboard/userdashboard.jinja.html',
                          {'message': message, 'authorization_status': authorization_status})

def userLogout(request):
    auth.logout(request)
    return HttpResponseRedirect('/userlogin')
