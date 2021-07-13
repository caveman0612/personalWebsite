from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('/', views.home, name="home"),
    path('rentals/', views.rentals, name="rentals"),
    path('services/', views.services, name="services"),
    path('events/', views.events, name="events"),
    path('contact/', views.contact, name="contact"),

]
