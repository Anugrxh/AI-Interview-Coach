from django.urls import path
from .views import InterviewSessionCreateView

urlpatterns = [
    path('start/', InterviewSessionCreateView.as_view(), name='interview-session-create'),
]
