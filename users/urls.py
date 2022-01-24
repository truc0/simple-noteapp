from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as TokenView

from users.views import UserViewset
from users.auth import LogoutView, RegisterView, ChangePasswordView

router = DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    path('', include(router.urls))
]

authpatterns = [
    path('auth/login', TokenView.obtain_auth_token, name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('auth/register', RegisterView.as_view(), name='register'),
    path(
        'auth/change-password', 
        ChangePasswordView.as_view({'patch': 'update', 'put': 'update'}), 
        name='change-password'
        ),
]

urlpatterns += authpatterns