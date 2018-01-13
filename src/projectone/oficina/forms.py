from django import forms
from .models import Client, Vehicle, Product, Service, PaymentMethod, Quotation, ServiceOrder

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, MultiField


class registerClient(forms.Form):
    cpf = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    phonenumber = forms.CharField()
    addressstreet = forms.CharField()
    addresscity = forms.CharField()
    addressstate = forms.CharField()

class registerVehicle(forms.Form):
    licenceplate = forms.CharField()
    brand = forms.CharField()
    model = forms.CharField()
    year = forms.CharField()
    kilometer = forms.CharField()
    chassis = forms.CharField()

#class registerProduct(forms.Form):

#class registerServiceOrder(forms.Form):

#class registerQuotation(forms.Form):
