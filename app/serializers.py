from rest_framework import serializers
from app.models import Doctor,Patient

class Patientserializer(serializers.ModelSerializer):
    doctor=serializers.HyperlinkedRelatedField()
    class Meta:
        model=Patient
        fields="__all__"

class DoctorSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField()
    class Meta:
        model=Doctor
        fields="__all__"
