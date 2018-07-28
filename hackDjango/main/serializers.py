#from django.contrib.auth.models import User, Group
from .models import AppUser, Subject,Request
from rest_framework import serializers

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('name','id')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name','id')
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('tutee','requestedSubject')
