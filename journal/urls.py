from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('entry', views.EntryList.as_view()),
    path('entry/<int:pk>', views.EntryDetail.as_view()),
    path('entry/create', views.EntryCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)