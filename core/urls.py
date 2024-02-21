from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

