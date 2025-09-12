from django.db import models

# Create your models here.
from django.db import models
from interviews.models import InterviewSession
from django.conf import settings


class Question(models.Model):
    interview_session = models.ForeignKey(InterviewSession, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Optionally, add fields for topic/level or answer key/difficulty

    def __str__(self):
        return self.text[:70]




class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True)    # User's spoken/text response
    created_at = models.DateTimeField(auto_now_add=True)
    # You can add audio file/audio URL fields later for voice answers
