from django.urls import path
from . import views

urlpatterns = [
    path('estimate/', views.estimate_value, name='estimate_value'),
]