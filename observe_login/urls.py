from django.urls import path
from .views import SignInView


app_name = 'observe_login' 

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin')
]