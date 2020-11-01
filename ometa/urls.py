from django.urls import path

from .import views
from .api_views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('works', views.works, name='works'),
    path('directors', views.directors, name='directors'),
    path('photographers', views.photographers, name='photographers'),
    path('about_us', views.about_us, name='about_us'),
    path('contacts', views.contacts, name='contacts'),
    path('photographers/<int:id>', views.photo_artist, name='photo_artist'),
    path('directors/<int:id>', views.director_artist, name='director_artist'),

    # path('preview_videos/', PreviewVideosView.as_view()),
    # path('works/', WorksView.as_view()),
    # path('directors/', DirectorsView.as_view()),
    # path('directors/<int:id>/', DirectorArtistView.as_view()),
    # path('photographers/', PhotographersView.as_view()),
    # path('photographers/<int:id>/', PhotoArtistView.as_view()),
    # path('about_us/', AboutUsView.as_view()),
    # path('contacts/', ContactsView.as_view()),
]
