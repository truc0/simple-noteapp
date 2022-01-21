from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as TokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', TokenView.obtain_auth_token),
    path('', include('note.urls')),
    path('', include('users.urls')),
]
