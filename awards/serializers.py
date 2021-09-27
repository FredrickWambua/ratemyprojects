from rest_framework import serializers
from .models import CustomUser, Profile, Project, Rates


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=65, min_length=2)

    class Meta:
        model = CustomUser
        fields = ['username', 'email','password', 'date_joined']

    def validate(self, attrs):
        if CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email':('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'