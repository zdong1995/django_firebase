from django.urls import path
from api_auth.views import RegisterView, LoginView


urlpatterns = [
        path('register', RegisterView.as_view()),
        path('login', LoginView.as_view()),
]