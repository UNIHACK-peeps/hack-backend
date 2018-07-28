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

# Converting objects to dict
from django.forms.models import model_to_dict


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
    API endpoint that allows Subjects to be viewed or edited.
    """
    queryset = Subject.objects.all().order_by('id')
    serializer_class = SubjectSerializer

class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Requests to be viewed or edited.
    """
    queryset = Request.objects.all().order_by('id')
    serializer_class = RequestSerializer

class AcceptTutee(APIView):
    """ Adding the tutor who accepted the request to the accepted tutor list """

    def post(self, request, *args, **kwargs):
        acceptedTutor = AppUser.objects.get(id=int(request.data.get('tutor_id')))
        currentRequest = Request.objects.get(id=int(request.data.get('request_id')))
        currentRequest.acceptedTutors.add(acceptedTutor)

        return JsonResponse(data={"yeet": "yeet"})

class ConfirmTutor(APIView):
    """ Tutee Confirm Tutor """
    
    def post(self, request, *args, **kwargs):
        confirmedTutor = AppUser.objects.get(id=int(request.data.get("tutor_id")))
        currentRequest = Request.objects.get(id=int(request.data.get("request_id")))
        currentRequest.chosenTutor = confirmedTutor

        return JsonResponse(data={"yeet": "yeet"})

class getMyTutees(APIView):
    
    def get(self, request):
        params = request.query_params
        currentUser = AppUser.object.get(id=int(params["user_id"]))
        return JsonResponse(data=currentUser.chosenTutor.all())

class getMyTutors(APIView):
    """ /tutors?user_id=something """

    def get(self, request):
        params = request.query_params
        currentUser = AppUser.object.get(id=int(params["user_id"]))

        # Get list of requests that this user id has, weird logic fuck my ass
        return JsonResponse(data=currentUser.tutee.all())

class Notifications(APIView):

    def get(self, request):
        params = request.query_params
        currentUser = AppUser.object.get(id=int(params["user_id"]))

        D = {}
        # my potential tutors List
        D["tutors"] = {}
        for req in currentUser.tutees.all():
            subjectName = str(req.requestedSubject)
            D[subjectName] = []
            for tutor in req.avaliableTutors:
                tutor_dict = model_to_dict(tutor)
                D[subjectName].append(tutor_dict)

        # my Tutees List
        D["tutees"] = {}
        for req in currentUser.avaliableTutors.all():
            subjectName = str(req.requestedSubject)
            if subjectName not in D["tutees"]:
                D[subjectName] = [req.tutee]
            D[subjectName].append(req.tutee)

        return JsonResponse(data=D)
        
        






