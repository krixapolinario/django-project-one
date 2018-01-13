from django.conf.urls import url
from django.contrib import admin

from oficina import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.loginview, name='login'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^inicio/', views.homeview, name='inicio'),
    url(r'^cadastro/', views.registerview, name='cadastro'),
    url(r'^logout/', views.logoutview, name='logout'),
]
