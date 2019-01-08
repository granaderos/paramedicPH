from django.shortcuts import render
from patient.models import Patient
from api.serializers import PatientSerializer
from rest_framework import generics
# Create your views here.

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
