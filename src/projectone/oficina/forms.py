from django import forms
from .models import Client, Vehicle, Product, Service, PaymentMethod, Quotation, ServiceOrder

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, MultiField


class registerClient(forms.Form):
    cpf = forms.CharField(required=True)
    name = forms.CharField(
           max_length=120,
           label='Nome: ',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Nome Completo',
                  })
           )
    email = forms.EmailField(required=False)
    phonenumber = forms.CharField(required=True)
    addressstreet = forms.CharField(required=False)
    addresscity = forms.CharField(required=False)
    addressstate = (
                ('pernambuco','Pernambuco'),
                ('joaopessoa','Joao Pessoa'),
                ('riograndedonorte','Rio Grande do Norte'),
        )

class registerVehicle(forms.Form):
    licenceplate = forms.CharField(required=True)
    brand = forms.CharField(required=True)
    model = forms.CharField(required=True)
    year = forms.CharField(required=True)
    kilometer = forms.CharField(required=True)
    chassis = forms.CharField(required=False)

#class registerProduct(forms.Form):

#class registerServiceOrder(forms.Form):

#class registerQuotation(forms.Form):
