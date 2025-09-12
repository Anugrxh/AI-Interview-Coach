from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

class InterviewSession(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='interviews')
    field = models.CharField(max_length=64)  # Now user can enter any field!
    difficulty = models.CharField(max_length=16, choices=DIFFICULTY_CHOICES)
    num_questions = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.email} - {self.field} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
