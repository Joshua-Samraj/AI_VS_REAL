# image_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
]
