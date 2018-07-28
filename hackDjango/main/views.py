from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import AppUserSerializer, SubjectSerializer,RequestSerializer
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

class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Matches to be viewed or edited.
    """
    queryset = Request.objects.all().order_by('id')
    serializer_class = RequestSerializer

def addTwoNumber(a,b):
    return a+b

class AcceptTutee(APIView):
    """ Adding the tutor who accepted the request to the accepted tutor list """

    def post(self, request, *args, **kwargs):
        acceptedTutor = AppUser.objects.get(id=int(request.data.get('tutor_id')))
        currentRequest = Request.objects.get(id=int(request.data.get('request_id')))
        currentRequest.acceptedTutors.add(acceptedTutor)

        return JsonResponse(data={"yeet": "yeet"})

class AcceptTutor(APIView):
    """ Tutee Confirm Tutor """
    
    def post(self, request, *args, **kwargs):
        confirmedTutor = AppUser.objects.get(id=int(request.data.get("tutor_id")))
        currentRequest = Request.objects.get(id=int(request.data.get("request_id")))
        currentRequest.chosenTutor = confirmedTutor

class getMyTutors(APIView):
    """ /tutors?user_id=something """

    def get(self, request):
        params = request.query_params
        currentUser = AppUser.object.get(id=int(params["user_id"]))

        # Get list of requests that this user id has, weird logic fuck my ass
        return JsonResponse(data=currentUser.tutee.all())
    

class getMyTutees(APIView):
    
    def get(self, request):
        params = request.query_params
        currentUser = AppUser.object.get(id=int(params["user_id"]))
        return JsonResponse(data=currentUser.chosenTutor.all())

class Notifications(APIView):

    def 
