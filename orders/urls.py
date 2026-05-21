from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_applications, name='my_applications'),
    path('create/', views.create_application, name='create_application'),
    path('<int:pk>/', views.application_detail, name='application_detail'),
]