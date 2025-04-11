from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.contact, name="home"), 
    path('contact/', views.contact, name="contact"),
    path('project/<int:id>/', views.project, name="project"),
]

"""path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    
]
"""