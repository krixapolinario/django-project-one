from django.shortcuts import render

import sys, requests, json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from .models import Client, Vehicle, Product, Service, PaymentMethod, Quotation, ServiceOrder

def loginview(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/oficina/')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/oficina/')
        else:
            messages.warning(request, 'Credenciais incorretas.')
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def oficinaview(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    if request.method == 'POST':
        return render(request, 'oficina.html', username)
    return render(request, 'login.html', {})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/login/')
