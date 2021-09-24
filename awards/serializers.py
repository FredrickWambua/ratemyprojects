from rest_framework import serializers
from rest_framework import Profile, Project, Rates

class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
