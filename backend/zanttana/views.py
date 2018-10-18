from django.shortcuts import render

from rest_framework import generics

from .models import Zantta, Profile, Lodging, Logistics
from .serializers import ZanttaSerializer, ProfileSerializer, LodgingSerializer, LogisticsSerializer


# profile serializers
class ListProfile(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DetailProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 


# Zantta serializers
class ListZantta(generics.ListCreateAPIView):
    queryset = Zantta.objects.all()
    serializer_class = ZanttaSerializer

class DetailZantta(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zantta.objects.all()
    serializer_class = ZanttaSerializer 


# Lodging serializers
class ListLodging(generics.ListCreateAPIView):
    queryset = Lodging.objects.all()
    serializer_class = LodgingSerializer

class DetailLodging(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lodging.objects.all()
    serializer_class = LodgingSerializer 


# Logistics serializers
class ListLogistics(generics.ListCreateAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer

class DetailLogistics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer 