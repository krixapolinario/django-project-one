from django.shortcuts import render

import sys, requests, json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings

from .forms import registerClient, registerSupplier, registerVehicle
from .models import Client, Supplier, Vehicle, Product, Service, PaymentMethod, Quotation, ServiceOrder

def loginview(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/inicio/')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/inicio/')
        else:
            messages.warning(request, 'Credenciais incorretas.')
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def homeview(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    if request.method == 'POST':
        pass
    return render(request, 'home.html')

def newclientview(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    form = registerClient(data=request.POST)
    context = {
            'form' : form,
            'username' : username,
        }
    if request.method == 'POST':
        pass
    return render(request, 'newclient.html', context)

def newsupplierview(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    form = registerSupplier(data=request.POST)
    context = {
            'form' : form,
            'username' : username,
        }
    if request.method == 'POST':
        pass
    return render(request, 'newsupplier.html', context)

def newvehicleview(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    form = registerVehicle(data=request.POST)
    context = {
            'form' : form,
            'username' : username,
        }
    if request.method == 'POST':
        pass
    return render(request, 'newvehicle.html', context)

def newproductview(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    if request.method == 'POST':
        pass
    return render(request, 'newproduct.html')

def newquotationview(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    if request.method == 'POST':
        pass
    return render(request, 'newquotation.html')

def newserviceorderview(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    if request.method == 'POST':
        pass
    return render(request, 'newserviceorder.html')

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/login/')
