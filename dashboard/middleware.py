from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated:
            return render(request, 'dashboard/login.html', {'message': 'Authentication failed. Please login again...!'})

        # Code to be executed for each request/response after
        # the view is called.

        return response
