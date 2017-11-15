from django.db import models

# Create your models here.

class Client(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  cpf = models.CharField(max_length=20)
  phonenumber = models.CharField(max_length=20)
  address_street = models.CharField(max_length=100)
  address_city = models.CharField(max_length=50)
  address_state = models.CharField(max_length=50)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Vehicle(models.Model):
  owner = models.ForeignKey(Client, on_delete=models.CASCADE)
  brand = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  year = models.CharField(max_length=4)
  license_plate = models.CharField(max_length=8)
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
  description = models.TextField(max_length=200)

  def __str__(self):
    return self.name

class Service(models.Model):
  name = models.CharField(max_length=50)
  price = models.CharField(max_length=10)
  description = models.TextField(max_length=200)

  def __str__(self):
    return self.name

class Quotation(models.Model):
  STATE=(
        ('APPROVED', 'Aprovado'),
        ('REJECTED', 'Rejeitado'),
        ('WAITING', 'Aguardando'),
  )
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
  items = models.ForeignKey(Product, on_delete=models.CASCADE)
  services = models.ForeignKey(Service, on_delete=models.CASCADE)
  validade = models.CharField(max_length=2)
  payment = models.CharField(max_length=20)
  description = models.TextField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  token = models.CharField(max_length=20)
  state = models.CharField(max_length=11, choices=STATE, default='WAITING')

  def __str__(self):
    return self.date

class ServiceOrder(models.Model):
  STATE=(
        ('PAYED', 'pago'),
        ('UNPAYED', 'nao pago'),
  )
  date = models.DateTimeField(auto_now_add=True)
  description = models.TextField(max_length=200)
  state = models.CharField(max_length=10, choices=STATE, default='UNPAYED')

  def __str__(self):
    return self.date
