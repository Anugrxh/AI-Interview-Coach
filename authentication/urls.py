from django.urls import path
from .views import \
    UserRegistrationView,\
    LogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
