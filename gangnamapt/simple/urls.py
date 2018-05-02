from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('note/', views.note, name='note'),
]
