from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', home, name="home"),
    path('contact/', contact, name="contact"),
    path('projects/', projects, name="projects"),
    path('resume/', resume, name="resume"),
]
