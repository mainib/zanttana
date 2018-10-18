from django.shortcuts import render

from rest_framework import generics

from .models import Zantta, Profile, Lodging, Logistic, Msg
from .serializers import ZanttaSerializer, ProfileSerializer, LodgingSerializer, LogisticsSerializer, MsgSerializer


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
    queryset = Logistic.objects.all()
    serializer_class = LogisticsSerializer

class DetailLogistics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logistic.objects.all()
    serializer_class = LogisticsSerializer 

# Msg serializers
class ListMsg(generics.ListCreateAPIView):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer

class DetailMsg(generics.RetrieveUpdateDestroyAPIView):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer 