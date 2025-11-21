from rest_framework import serializers
from .models import User
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                
            )