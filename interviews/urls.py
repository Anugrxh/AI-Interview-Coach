from django.urls import path
from .views import InterviewSessionCreateView,InterviewHistoryView

urlpatterns = [
    path('start/', InterviewSessionCreateView.as_view(), name='interview-session-create'),
    path('history/', InterviewHistoryView.as_view(), name='interview-history'),
]
