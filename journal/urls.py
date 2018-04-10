from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('entry', views.EntryList.as_view()),
    path('entry/create', views.EntryCreate.as_view()),
    path('entry/update/<pub_date>', views.EntryUpdate.as_view()),
    path('entry/delete/<pub_date>', views.EntryDelete.as_view()),
    path('concert', views.ConcertList.as_view()),
    path('concert/create', views.ConcertCreate.as_view()),
    path('concert/update/<date>', views.ConcertUpdate.as_view()),
    path('concert/delete/<date>', views.ConcertDelete.as_view()),
    path('artist', views.ArtistList.as_view()),
    path('artist/create', views.ArtistCreate.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
