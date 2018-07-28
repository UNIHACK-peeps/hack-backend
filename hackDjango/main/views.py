from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import AppUserSerializer, SubjectSerializer
from .models import AppUser, Subject
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Matches to be viewed or edited.
    """
    queryset = AppUser.objects.all().order_by('id')
    serializer_class = AppUserSerializer
class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Matches to be viewed or edited.
    """
    queryset = Subject.objects.all().order_by('id')
    serializer_class = SubjectSerializer
