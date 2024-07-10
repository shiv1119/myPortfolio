from rest_framework import generics
from .models import AuthorProfile
from .serializers import AuthorProfileSerializer

class AuthorProfileList(generics.ListAPIView):
    queryset = AuthorProfile.objects.all()
    serializer_class = AuthorProfileSerializer