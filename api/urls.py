from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('test_api/', views.test_api, name='test_api'),
]
