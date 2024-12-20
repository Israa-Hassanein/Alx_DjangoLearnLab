from django.urls import path
from .views import RegisterView
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
]