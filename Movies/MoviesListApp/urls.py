from django.urls import path
from . import views

urlpatterns = [
    path('', views.Movies_list, name = 'Movies_list')
]