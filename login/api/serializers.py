from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class adminloginserializer(serializers.ModelSerializer):
  class Meta:
    model=admin_login
    field='__all__'

class officerserializer(serializers.ModelSerializer):
  class Meta:
    model=Officer
    field='__all__'

class Officerdetailserializer(serializers.ModelSerializer):
  class Meta: 
    model= Officer
    fields='__all__'

class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password',
#         )
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=User.objects.all(),
#                 fields=['username', 'email']
#             )
#         ]

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class FineSerializer(serializers.ModelSerializer):
   class Meta:
      model = Fine
      fields = '__all__'

class BluebookSerializer(serializers.ModelSerializer):
   class Meta:
      model = BluebookRenew
      fields = '__all__'