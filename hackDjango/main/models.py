from django.db import models

# Create your models here.

class App_User(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    def __str__(self):
        return self.name