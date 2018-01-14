from django import forms
from .models import Client, Supplier, Vehicle, Product, Service, PaymentMethod, Quotation, ServiceOrder

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, MultiField


class registerClient(forms.Form):
    cpf = forms.CharField(
           max_length=20,
           label='CPF',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* CPF',
                  })
           )
    name = forms.CharField(
           max_length=120,
           label='Nome Completo',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Nome Completo',
                  })
           )
    email = forms.EmailField(
           max_length=120,
           label='Nome Completo',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* E-Mail',
                  })
           )
    phone_number_1 = forms.CharField(
           max_length=20,
           label='Telefone 1',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Telefone 1',
                  })
           )
    phone_number_2 = forms.CharField(
           max_length=20,
           label='Telefone 2',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'Telefone 2',
                  })
           )
    address = forms.CharField(
           max_length=120,
           label='Endereco',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'Endereco',
                  })
           )
    neighborhood = forms.CharField(
           max_length=50,
           label='Bairro',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'Bairro',
                  })
           )
    city = forms.CharField(
           max_length=50,
           label='Cidade',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Cidade',
                  })
           )
    zipcode = forms.CharField(
           max_length=10,
           label='CEP',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'CEP',
                  })
           )
    state = forms.CharField(
           max_length=50,
           label='Estado',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Estado',
                  })
           )

class registerSupplier(forms.Form):
    cpf_cnpj = forms.CharField(
           max_length=40,
           label='CPF/CNPJ',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* CPF ou CNPJ',
                  })
           )
    name = forms.CharField(
           max_length=120,
           label='Nome',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Nome',
                  })
           )
    email = forms.EmailField(
           max_length=120,
           label='Nome Completo',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* E-Mail',
                  })
           )
    phone_number_1 = forms.CharField(
           max_length=20,
           label='Telefone 1',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Telefone 1',
                  })
           )
    phone_number_2 = forms.CharField(
           max_length=20,
           label='Telefone 2',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'Telefone 2',
                  })
           )
    address = forms.CharField(
           max_length=120,
           label='Endereco',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'Endereco',
                  })
           )
    neighborhood = forms.CharField(
           max_length=50,
           label='Bairro',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'Bairro',
                  })
           )
    city = forms.CharField(
           max_length=50,
           label='Cidade',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'Cidade',
                  })
           )
    zipcode = forms.CharField(
           max_length=50,
           label='CEP',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'CEP',
                  })
           )
    state = forms.CharField(
           max_length=50,
           label='Estado',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Estado',
                  })
           )

class registerVehicle(forms.Form):
    licenceplate = forms.CharField(
           max_length=10,
           label='Placa',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Placa',
                  })
           )
    brand = forms.CharField(
           max_length=50,
           label='Marca',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Marca',
                  })
           )
    model = forms.CharField(
           max_length=50,
           label='Modelo',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Modelo',
                  })
           )
    year = forms.CharField(
           max_length=4,
           label='Ano',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Ano',
                  })
           )
    kilometer = forms.CharField(
           max_length=50,
           label='Kilometragem',
           required=True,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Kilometragem',
                  })
           )
    chassis = forms.CharField(
           max_length=50,
           label='Chassis',
           required=False,
           widget=forms.TextInput(attrs={
                  'class':'textinput textInput form-control',
                  'placeholder':'* Chassis',
                  })
           )

#class registerProduct(forms.Form):

#class registerServiceOrder(forms.Form):

#class registerQuotation(forms.Form):
