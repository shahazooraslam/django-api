from django.shortcuts import render
from rest_framework import generics
from .models import Blogpost
from .serializers import blogspotserializers
# Create your views here.

class BlogpostListCreate(generics.ListCreateAPIView):
    queryset=Blogpost.objects.all()
    serializer_class=blogspotserializers
class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogpost.objects.all()
    serializer_class=blogspotserializers
    lookup_field="pk"