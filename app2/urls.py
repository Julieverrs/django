from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('', views.gallery, name='gallery'),  # Default view for app2
    path('gallery/', views.gallery, name='gallery'),  # Gallery page
    path('services/', views.services, name='services'),  # Services page
    path('team/', views.team, name='team'),  # Team page
]
