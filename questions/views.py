from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer  # To be created
from .services import generate_interview_questions
from interviews.models import InterviewSession

class GenerateQuestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, session_id):
        try:
            interview_session = InterviewSession.objects.get(pk=session_id, user=request.user, is_active=True)
        except InterviewSession.DoesNotExist:
            return Response({"error": "Session not found or inactive."}, status=status.HTTP_404_NOT_FOUND)
        # Only generate if not already generated
        if interview_session.questions.exists():
            return Response({"error": "Questions already generated for this session."}, status=400)
        field = interview_session.field
        difficulty = interview_session.difficulty
        num_questions = interview_session.num_questions
        try:
            questions_list = generate_interview_questions(field, difficulty, num_questions)
        except Exception as e:
            return Response({"error": f"Question generation failed: {str(e)}"}, status=500)
        created = []
        for q in questions_list:
            obj = Question.objects.create(
                interview_session=interview_session,
                text=q,
            )
            created.append(obj)
        # To serialize and return created questions:
        from .serializers import QuestionSerializer
        return Response(QuestionSerializer(created, many=True).data)





from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import QuestionSerializer,AnswerSerializer
from .models import Question
from interviews.models import InterviewSession
from rest_framework.response import Response
from rest_framework import status

class QuestionListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        session_id = self.kwargs.get('session_id')
        user = self.request.user
        # Ensure session belongs to user
        return Question.objects.filter(interview_session__id=session_id, interview_session__user=user)



from rest_framework import generics, permissions

class AnswerCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
