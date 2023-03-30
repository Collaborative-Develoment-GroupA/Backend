from rest_framework import serializers
from .models import *

class adminloginserializer(serializers.ModelSerializer):
  class Meta:
    model=admin_login
    field='__all__'