from django.db import models
from django.core.validators import MaxValueValidator

class Client(models.Model):
  name = models.CharField(max_length=120)
  email = models.EmailField()
  cpf = models.CharField(max_length=20)
  phone_number1 = models.CharField(max_length=20)
  phone_number2 = models.CharField(blank=True, max_length=20)
  address = models.CharField(blank=True, max_length=120)
  neighborhood = models.CharField(blank=True, max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  zipcode = models.CharField(blank=True, max_length=10)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Supplier(models.Model):
  name = models.CharField(max_length=120)
  email = models.EmailField()
  cpf_cnpj = models.CharField(max_length=20)
  phone_number1 = models.CharField(max_length=20)
  phone_number2 = models.CharField(blank=True, max_length=20)
  address = models.CharField(blank=True, max_length=120)
  neighborhood = models.CharField(blank=True, max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  zipcode = models.CharField(blank=True, max_length=10)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Vehicle(models.Model):
  owner = models.ForeignKey(Client, on_delete=models.CASCADE)
  brand = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  year = models.CharField(max_length=4)
  license_plate = models.CharField(max_length=10)
  chassis = models.CharField(max_length=50)
  kilometer = models.CharField(max_length=6)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.license_plate

class Product(models.Model):
  STATE=(
        ('NEW', 'Novo'),
        ('USED', 'Usado'),
  )
  name = models.CharField(max_length=50)
  price = models.CharField(max_length=10)
  quantity = models.CharField(max_length=4)
  state = models.CharField(max_length=5, choices=STATE)
  description = models.TextField(max_length=200, blank=True)

  def __str__(self):
    return self.name

class Service(models.Model):
  name = models.CharField(max_length=50)
  price = models.CharField(max_length=10)
  description = models.TextField(max_length=200, blank=True)

  def __str__(self):
    return self.name

class PaymentMethod(models.Model):
  method = models.CharField(max_length=50)
  description = models.TextField(max_length=200, blank=True)

  def __str__(self):
    return self.method

class Quotation(models.Model):
  STATE=(
        ('APPROVED', 'Aprovado'),
        ('REJECTED', 'Rejeitado'),
        ('WAITING', 'Aguardando'),
  )
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
  items = models.ManyToManyField(Product)
  services = models.ManyToManyField(Service)
  validity = models.PositiveIntegerField(default='2', validators=[MaxValueValidator(2)])
  payment = models.ManyToManyField(PaymentMethod)
  description = models.TextField(max_length=200, blank=True)
  date = models.DateTimeField(auto_now_add=True)
  token = models.CharField(max_length=20)
  state = models.CharField(max_length=11, choices=STATE, default='WAITING')

  def __str__(self):
    return str(self.date).split('.')[0]

class ServiceOrder(models.Model):
  STATE=(
        ('PAYED', 'pago'),
        ('UNPAYED', 'nao pago'),
  )
  date = models.DateTimeField(auto_now_add=True)
  description = models.TextField(max_length=200, blank=True)
  state = models.CharField(max_length=10, choices=STATE, default='UNPAYED')

  def __str__(self):
    return str(self.date).split('.')[0]
