#from django.contrib.auth.models import User, Group
from .models import AppUser, Subject
from rest_framework import serializers

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('name','id','acceptRequest')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name','id')
