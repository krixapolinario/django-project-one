from django.contrib import admin

from .models import Client, Vehicle, Product, Service, PaymentMethod, Quotation, ServiceOrder

#@admin.register(Client, Vehicle, Product, Service, Quotation)

class ClientAdmin(admin.ModelAdmin):
    fields = ['cpf', 'name', 'email', 'phonenumber', 'address_street', 'address_city', 'address_state']

admin.site.register(Client, ClientAdmin)

class VehicleAdmin(admin.ModelAdmin):
    fields = ['license_plate', 'owner', 'brand', 'model', 'year', 'kilometer', 'chassis']

admin.site.register(Vehicle, VehicleAdmin)

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'quantity', 'state', 'description']

admin.site.register(Product, ProductAdmin)

class ServiceAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'description']

admin.site.register(Service, ServiceAdmin)

class PaymentMethodAdmin(admin.ModelAdmin):
    fields = ['method', 'description']

admin.site.register(PaymentMethod, PaymentMethodAdmin)

class QuotationAdmin(admin.ModelAdmin):
    fields = ['client', 'vehicle', 'validity', 'payment', 'items', 'services', 'description', 'state']

admin.site.register(Quotation, QuotationAdmin)

class ServiceOrderAdmin(admin.ModelAdmin):
    fields = ['description', 'state']

admin.site.register(ServiceOrder, ServiceOrderAdmin)
