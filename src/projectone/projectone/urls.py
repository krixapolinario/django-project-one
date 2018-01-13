from django.conf.urls import url
from django.contrib import admin

from oficina import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.loginview, name='login'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^oficina/', views.loginview, name='oficina'),
    url(r'^logout/', views.logoutview, name='logout'),
]
