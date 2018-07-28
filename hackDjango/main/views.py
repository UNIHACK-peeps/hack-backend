from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import App_UserSerializer
from .models import App_User
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Matches to be viewed or edited.
    """
    queryset = App_User.objects.all().order_by('id')
    serializer_class = App_UserSerializer