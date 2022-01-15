from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail), # <int:question_id> : int 숫자가 매핑됨을 의미
]