from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_note', views.add_note)
]