from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('testing1/', views.testing1, name='testing1'),
    path('name20/<str:name>', views.string_builder, name='string_builder'),
]
