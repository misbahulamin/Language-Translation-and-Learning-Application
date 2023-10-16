
from rest_framework import serializers
from .models import RegisterModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterModel
        fields = ["email", "password"]

    
    