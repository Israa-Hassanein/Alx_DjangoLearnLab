from django.urls import path
from .views import RegisterView
from django.contrib import admin
from django.urls import include
from . import views
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow_user'),
    path('users/', views.ListUsersView.as_view(), name='list_users'),  # Add this route
]

