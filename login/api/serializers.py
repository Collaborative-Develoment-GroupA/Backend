from rest_framework import serializers
from .models import *

class adminloginserializer(serializers.ModelSerializer):
  class Meta:
    model=admin_login
    field='__all__'

class officerserializer(serializers.ModelSerializer):
  class Meta:
    model=Officer
    field='__all__'

class Officerdetailserializer(serializers.ModelSerializer):
  # forkey= officerserializer()
  class Meta: 
    model= Officer
    fields='__all__'

class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = '__all__'