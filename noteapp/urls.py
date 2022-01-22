from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as TokenView

from users.auth import LogoutView, RegisterView

authpatterns = [
    path('auth/login', TokenView.obtain_auth_token, name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('auth/register', RegisterView.as_view(), name='register'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note.urls')),
    path('', include('users.urls')),
] + authpatterns
