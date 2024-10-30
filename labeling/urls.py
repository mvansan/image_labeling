from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random_image, name='random_image'),  
]