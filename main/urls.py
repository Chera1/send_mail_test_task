# coding=utf-8
from django.conf.urls import url
from django.contrib import admin
from mailganer import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('subscribe/', views.subscribe, name='subscribe'),
    url('mass_mailing/', views.mass_mailing, name='mass_mailing'),
    url('validate/', views.validate_email, name='validate_email'),
]
