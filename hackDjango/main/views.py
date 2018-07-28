from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import AppUserSerializer, SubjectSerializer
from .models import AppUser, Subject,Request
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    data = {
        'test':"test"
    }
    #print(str(request))
    return HttpResponse(request.method)

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

def addTwoNumber(a,b):
    return a+b

class AcceptTutor(APIView):
    def get(self,request):
        parameters = request.query_params
        return JsonResponse(data={
            'test':parameters  
        }
            )
    def post(self, request, *args, **kwargs):
        my_result=addTwoNumber(request.data.get('firstnum'),request.data.get('secondnum'))
        return Response(data={"my_return_data":my_result})