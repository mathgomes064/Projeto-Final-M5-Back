from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("schedules/<uuid:pk>/", views.ScheduleView.as_view()),
]
