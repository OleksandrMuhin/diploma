
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from diploma import settings
from diplomapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diplomapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
