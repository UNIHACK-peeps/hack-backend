from django.db import models

# Create your models here.

SUBJECTS = (("MAT", "Mathematics"),
            ("GEO", "Geography"),
            ("ENG", "English"),
            ("MAN", "Mandarin"))


class AppUser(models.Model):
    name = models.CharField(max_length=200)
    subjectsOffered = models.ManyToManyField("Subject",related_name="subjectsOffered")

    def acceptRequest(self, request_id):
        Request[request_id].acceptedTutors_set.add(self)
        
    def acceptTutor(self, request_id, tutor_id):
        currRequest = Request.objects.get(id=request_id)
        acceptedTutor = AppUser.objects.get(id=tutor_id)
        currRequest.chosenTutor = acceptedTutor
    def __str__(self):
        return self.name
    
class Request(models.Model):
    tutee = models.OneToOneField("AppUser", on_delete=models.CASCADE, related_name="tutee")
    requestedSubject = models.OneToOneField("Subject", on_delete=models.CASCADE,
                                            related_name="requestedSubject")
    avaliableTutors = models.ManyToManyField("AppUser", related_name="avaliableTutors", blank=True)
    acceptedTutors = models.ManyToManyField("AppUser", related_name="acceptedTutors",blank=True,default=None)
    chosenTutor = models.OneToOneField("AppUser", on_delete=models.CASCADE,
                                       related_name="chosenTutor", null=True,blank = True)
    
    def computeAvaliableTutors(self, subject_id, frequency):
        """
        Telling the tutors what requests are for them
        """
        subject = Subject.objects.get(id=subject_id)
        for tutor in AppUser.objects.all():
            if subject in tutor.subjectsOffered.all():
                avaliableTutors.add(tutor)

    
class Subject(models.Model):
    name = models.CharField(max_length=3, choices=SUBJECTS)
    def __str__(self):
        return self.name