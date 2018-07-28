from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'requests', views.RequestViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^acceptTutee/$', views.AcceptTutee.as_view()),
    url(r'^confirmTutor/$', views.AcceptTutor.as_view()),
    url(r'^getMyTutees/$', views.getMyTutees.as_view()),
    url(r'^getMyTutors/$', views.getMyTutors.as_view()),
    url(r'^Notifications/$', views.Notifications.as_view())
]
