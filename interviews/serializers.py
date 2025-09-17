from rest_framework import serializers
from .models import InterviewSession

class InterviewSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSession
        fields = ['id', 'field', 'difficulty', 'num_questions', 'created_at', 'is_active']
        read_only_fields = ['id', 'created_at', 'is_active']



from rest_framework import serializers
from .models import InterviewSession
from questions.serializers import QuestionWithAnswersSerializer

# Keep your existing InterviewSessionSerializer unchanged

class InterviewSessionHistorySerializer(serializers.ModelSerializer):
    questions = QuestionWithAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = InterviewSession
        fields = ['id', 'field', 'difficulty', 'num_questions', 'created_at', 'is_active', 'questions']
        read_only_fields = ['id', 'created_at', 'is_active']
