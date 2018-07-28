#from django.contrib.auth.models import User, Group
from .models import App_User
from rest_framework import serializers

class App_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = App_User
        fields = ('name','id')