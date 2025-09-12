from django.urls import path
from .views import QuestionListView, GenerateQuestionsView,AnswerCreateView

urlpatterns = [
    path('generate/<int:session_id>/', GenerateQuestionsView.as_view(), name='generate-questions'),
    path('list/<int:session_id>/', QuestionListView.as_view(), name='question-list'),
    path('answer/', AnswerCreateView.as_view(), name='answer-create'),

]
