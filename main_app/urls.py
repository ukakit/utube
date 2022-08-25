from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('video/<int:pk>/', views.VideoDetail.as_view(), name="video_detail"),
    path('video/upload/', views.VideoCreate.as_view(), name="video_create"),
    path('video/<int:pk>/uploadthumb/', views.add_thumb, name="add_thumb"),
    path('video/<int:pk>/uploadmedia/', views.add_media, name="add_media"),
    path('video/<int:pk>/edit',views.VideoUpdate.as_view(), name="video_update"),
    path('video/<int:pk>/delete',views.VideoDelete.as_view(), name="video_delete"),
    path('video/<int:video_pk>/comment/<int:pk>/edit',views.CommentUpdate.as_view(), name="comment_update"),
    path('video/<int:video_pk>/comment/<int:pk>/delete',views.CommentDelete.as_view(), name="comment_delete"),
    path('account/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('account/<int:pk>/edit/', views.UserUpdate.as_view(), name='edit_profile'),
    path(r'results', views.SearchResultsView.as_view(), name='search_result'),
]
