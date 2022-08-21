from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('video/<int:pk>/', views.VideoDetail.as_view(), name="video_detail"),
    path('video/upload/', views.VideoCreate.as_view(), name="video_create"),
    path('video/<int:pk>/edit',views.VideoUpdate.as_view(), name="video_update"),

]
