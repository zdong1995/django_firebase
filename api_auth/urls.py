from django.urls import path
from api_auth.views import SignupView, LoginView


urlpatterns = [
        path('signup', SignupView.as_view()),
        path('login', LoginView.as_view()),
]