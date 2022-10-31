from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('', include('mail_controller.urls'), name='gmail'),
    path('', include('googledriveapp.urls'), name='drive'),
]