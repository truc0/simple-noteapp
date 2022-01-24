from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note.urls')),
    path('', include('users.urls')),
]

debugpatterns = [
    path('docs/', include_docs_urls(title='Note API', patterns=urlpatterns))
]

if settings.DEBUG:
    urlpatterns += debugpatterns