from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from hackdjango.serializers import UserSerializer, GroupSerializer

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")