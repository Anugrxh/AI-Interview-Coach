from rest_framework import serializers
from .models import Question, Answer

# Keep your existing serializers unchanged
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']

# New serializer for nested answers without 'question' field (for history API)
class AnswerNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']

# New serializer using nested answers inside questions
class QuestionWithAnswersSerializer(serializers.ModelSerializer):
    answers = AnswerNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at', 'answers']
