from django.urls import path, include
from .views import main

app_name='covid19'
import covid_19.views

urlpatterns = [
    path('', main, name='home'),
]
