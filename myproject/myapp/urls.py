from django.urls import path
from .views import AuthorProfileList

urlpatterns = [
    path('api/authorprofiles/', AuthorProfileList.as_view(), name='authorprofile-list'),
]
