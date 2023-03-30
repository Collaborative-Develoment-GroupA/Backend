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