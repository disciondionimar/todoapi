from django.urls import path

#third-party imports

#local imports
from authentication.views import RegisterAPIView, LoginAPIView, AuthUserAPIView


urlpatterns = [
    path('register/',RegisterAPIView.as_view(), name="register"),
    path('login/',LoginAPIView.as_view(), name="login"),
    path('user/', AuthUserAPIView.as_view(), name="userdetails")
]
