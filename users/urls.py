from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewset

router = DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    path('', include(router.urls))
]