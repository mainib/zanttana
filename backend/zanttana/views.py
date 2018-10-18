from django.shortcuts import render

from rest_framework import generics

from .models import Zantta
from .serializers import ZanttaSerializer


class ListZantta(generics.ListCreateAPIView):
    queryset = Zantta.objects.all()
    serializer_class = ZanttaSerializer


class DetailZantta(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zantta.objects.all()
    serializer_class = ZanttaSerializer