from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Info
from .serializers import PhotoSerializer
# Create your views here.





class SetData(viewsets.ModelViewSet):

    queryset = Info.objects.all()
    serializer_class = PhotoSerializer