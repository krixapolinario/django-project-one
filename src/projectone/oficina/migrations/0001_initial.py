# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome completo')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('cpf', models.CharField(max_length=20, verbose_name='cpf')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='telefone')),
                ('address_street', models.CharField(max_length=100, verbose_name='endereco')),
                ('address_city', models.CharField(max_length=50, verbose_name='cidade')),
                ('address_state', models.CharField(max_length=50, verbose_name='estado')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='adicionado em')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('price', models.CharField(max_length=10, verbose_name='preco')),
                ('quantity', models.CharField(max_length=4, verbose_name='quantidade')),
                ('state', models.CharField(choices=[('new', 'novo'), ('used', 'usado')], max_length=5, verbose_name='estado')),
                ('description', models.TextField(max_length=200, verbose_name='descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validade', models.CharField(max_length=2, verbose_name='validade')),
                ('payment', models.CharField(max_length=20, verbose_name='token')),
                ('description', models.TextField(max_length=200, verbose_name='observacoes')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('token', models.CharField(max_length=20, verbose_name='token')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.Client')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('price', models.CharField(max_length=10, verbose_name='preco')),
                ('description', models.TextField(max_length=200, verbose_name='descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='marca')),
                ('model', models.CharField(max_length=50, verbose_name='modelo')),
                ('year', models.CharField(max_length=4, verbose_name='ano')),
                ('license_plate', models.CharField(max_length=7, verbose_name='placa')),
                ('chassis', models.CharField(max_length=50, verbose_name='chassi')),
                ('kilometer', models.CharField(max_length=6, verbose_name='kilometragem')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='adicionado em')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.Client')),
            ],
        ),
        migrations.AddField(
            model_name='quotation',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.Service'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.Vehicle'),
        ),
    ]