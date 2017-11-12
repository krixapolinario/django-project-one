from django.contrib import admin

from .models import Client, Vehicle, Product, Service, Quotation

@admin.register(Client, Vehicle, Product, Service, Quotation)

class ClientAdmin(admin.ModelAdmin):
    fields = ('cpf', 'name', 'email', 'phonenumber', 'address_street', 'address_city', 'address_state')

class VehicleAdmin(admin.ModelAdmin):
    fields = ('license_plate', 'owner', 'brand', 'model', 'year', 'kilometer', 'chassis')

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'quantity', 'state', 'description')

class ServiceAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'description')

class QuotationAdmin(admin.ModelAdmin):
    fields = ('client', 'vehicle', 'validade', 'payment', 'items', 'services', 'description')
