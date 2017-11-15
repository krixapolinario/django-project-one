from django.db import models

# Create your models here.

class Client(models.Model):
  name = models.CharField('Nome Completo', max_length=100)
  email = models.EmailField('E-Mail')
  cpf = models.CharField('CPF', max_length=20)
  phonenumber = models.CharField('Telefone', max_length=20)
  address_street = models.CharField('Endereco', max_length=100)
  address_city = models.CharField('Cidade', max_length=50)
  address_state = models.CharField('Estado', max_length=50)
  date_joined = models.DateTimeField('Adicionado em', auto_now_add=True)

  def __str__(self):
    return self.name

class Vehicle(models.Model):
  owner = models.ForeignKey(Client, on_delete=models.CASCADE)
  brand = models.CharField('Marca', max_length=50)
  model = models.CharField('Modelo', max_length=50)
  year = models.CharField('Ano', max_length=4)
  license_plate = models.CharField('Placa', max_length=8)
  chassis = models.CharField('Chassi', max_length=50)
  kilometer = models.CharField('Kilometragem', max_length=6)
  date_joined = models.DateTimeField('Adicionado em', auto_now_add=True)

  def __str__(self):
    return self.license_plate

class Product(models.Model):
  STATE=(
        ('new', 'Novo'),
        ('used', 'Usado'),
  )
  name = models.CharField('Nome', max_length=50)
  price = models.CharField('Valor', max_length=10)
  quantity = models.CharField('Quantidade', max_length=4)
  state = models.CharField('Estado', max_length=5, choices=STATE)
  description = models.TextField('Descricao', max_length=200)

  def __str__(self):
    return self.name

class Service(models.Model):
  name = models.CharField('Nome', max_length=50)
  price = models.CharField('Valor', max_length=10)
  description = models.TextField('Descricao', max_length=200)

  def __str__(self):
    return self.name

class Quotation(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
  items = models.ForeignKey(Product, on_delete=models.CASCADE)
  services = models.ForeignKey(Service, on_delete=models.CASCADE)
  validade = models.CharField('Validade', max_length=2)
  payment = models.CharField('Token',max_length=20)
  description = models.TextField('Observacoes', max_length=200)
  date = models.DateTimeField('Data', auto_now_add=True)
  token = models.CharField('Token',max_length=20)

  def __str__(self):
    return self.id

class ServiceOrder(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
  items = models.ForeignKey(Product, on_delete=models.CASCADE)
  services = models.ForeignKey(Service, on_delete=models.CASCADE)
  payment = models.CharField('Token',max_length=20)
  description = models.TextField('Observacoes', max_length=200)
  date = models.DateTimeField('Data', auto_now_add=True)

  def __str__(self):
    return self.id
