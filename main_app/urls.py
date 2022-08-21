from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('video/<int:pk>/', views.VideoDetail.as_view(), name="video_detail"),
]
