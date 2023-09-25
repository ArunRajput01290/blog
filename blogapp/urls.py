
from django.contrib import admin
from django.urls import include, path
from. import views

urlpatterns = [
    path('', views.index,name="Home"),
    path('vehicle.html', views.vehicle,name="Vehicle Portal"),
    path('about.html', views.about,name="Home"),
    path('desire.html', views.desire,name="Home"),
    path('contact.html', views.contact,name="Home"),
    path('confidence.html', views.confidence,name="Home"),
    path('think.html', views.think,name="Home"),
    path('idea.html', views.idea,name="Home"),
    path('rich.html', views.rich,name="Home"),
    path('conc.html', views.conc,name="Home"),
]