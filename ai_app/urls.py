# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('identifikasi-lahan/', predict_mangrove, name="predict_mangrove"),
    path('identifikasi-jenis-by-image/', predict_mangrove_image, name="predict_mangrove_image"),
]