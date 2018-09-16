from django.urls import path
from users.views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    UserTokenAPIView,
)

app_name = "users"

urlpatterns = [
    path(r"users/", UserRegistrationAPIView.as_view(), name="list"),
    path(r"users/login/", UserLoginAPIView.as_view(), name="login"),
    path(r"tokens/<pk>/", UserTokenAPIView.as_view(), name="token"),
]
