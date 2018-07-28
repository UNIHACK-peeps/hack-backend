from django.contrib import admin
from main.models import AppUser,Request,Subject
# Register your models here.
admin.site.register(AppUser)
admin.site.register(Request)
admin.site.register(Subject)