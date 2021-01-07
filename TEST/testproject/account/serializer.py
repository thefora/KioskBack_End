from rest_framework import serializers
from .models import k_user
from django.contrib.auth import authenticate

class k_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = k_user
        fields = ['phone', 'password']

    def create(self, validated_data):
        user = k_user.objects.create_user(
            phone = validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user