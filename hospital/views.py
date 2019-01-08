from django.shortcuts import render
from hospital.models import Hospital
from api.serializers import HospitalSerializer
from rest_framework import generics

class HospitalList(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    lookup_field = 'username'
