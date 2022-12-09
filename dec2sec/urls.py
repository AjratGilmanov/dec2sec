
from django.urls import path
from dec2secapp import views

urlpatterns = [
    path('', views.index),
    path('form', views.form)
]