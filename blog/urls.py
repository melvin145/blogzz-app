
from django.contrib import admin
from django.urls import path,include
import main.urls
from froala_editor import views
from .import settings

from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("main.urls")),
    #path('ckeditor/', include('ckeditor_uploader.urls')),
    path('froala_editor/',include('froala_editor.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
