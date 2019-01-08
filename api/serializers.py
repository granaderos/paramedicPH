from rest_framework import serializers
from hospital.models import Hospital
from patient.models import Patient
from municipal.models import Municipal

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('hospitalName', 'personInCharge', 'address','telephone', 'username', 'password')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'middle_name', 'last_name', 'address', 'number', 'email_address', 'username', 'password')

class MunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipal
        fields = ('municipal_name', 'person_in_charge', 'telephone', 'address', 'username', 'password')