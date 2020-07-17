from django.urls import path
from api_auth.views import SignupView, LoginView, EmailVerifyView, ResetPasswordView, AddView, UpdateView

urlpatterns = [
        path('signup', SignupView.as_view()),
        path('login', LoginView.as_view()),
        path('update', UpdateView.as_view()),
        path('add', AddView.as_view()),
        path('reset_password', ResetPasswordView.as_view()),
        path('email_verify', EmailVerifyView.as_view()),
]