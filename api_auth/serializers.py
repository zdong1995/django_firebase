from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import AuthenticatedUser


# Serializer for Registration
class SignupSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        return self.Meta.model.objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'first_name', 'last_name',
        )


# Serializer for Login Authentication
class LoginSerializer(serializers.ModelSerializer):

    def create(self, authenticated_data):
        data = {
            key: value for key, value in authenticated_data.items()
        }
        return self.Meta.model.objects.create_user(**authenticated_data)

    class Meta:
        model = AuthenticatedUser
        fields = ('first_name', 'localId', 'idToken', 'refreshToken')
        read_only_fields = ('localId',)
