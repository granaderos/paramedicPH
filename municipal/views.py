from django.shortcuts import render
from municipal.models import Municipal
from api.serializers import MunicipalSerializer
from rest_framework import generics
# Create your views here.

class MunicipalList(generics.ListCreateAPIView):
    queryset = Municipal.objects.all()
    serializer_class = MunicipalSerializer

class MunicipalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipal.objects.all()
    serializer_class = MunicipalSerializer
