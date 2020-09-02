from django.template.backends import django
from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('works', views.works, name='works'),
    path('directors', views.directors, name='directors'),
    path('photographers', views.photographers, name='photographers'),
    path('about_us', views.about_us, name='about_us'),
    path('contacts', views.contacts, name='contacts'),
    path('photographers/<int:id>/', views.photo_artist, name='photo_artist'),
    path('directors/<int:id>/', views.director_artist, name='director_artist'),
]
