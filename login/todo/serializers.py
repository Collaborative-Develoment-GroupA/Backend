from rest_framework import serializers
from .models import Todo, Login

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id' ,'title', 'description', 'completed')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('id' ,'email', 'password', 'username')