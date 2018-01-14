from django.conf.urls import url
from django.contrib import admin

from oficina import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.loginview, name='login'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^inicio/', views.homeview, name='inicio'),
    url(r'^novocliente/', views.newclientview, name='novocliente'),
    url(r'^novocarro/', views.newvehicleview, name='novocarro'),
    url(r'^novoproduto/', views.newproductview, name='novoproduto'),
    url(r'^novoorcamento/', views.newquotationview, name='novoorcamento'),
    url(r'^novaordemservico/', views.newserviceorderview, name='novaordemservico'),
    url(r'^logout/', views.logoutview, name='logout'),
]
