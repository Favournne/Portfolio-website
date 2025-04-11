
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 
from main import views  


urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Keep this ONLY here
    path('', views.contact, name="home"),
    path('contact/', views.contact, name="contact"),
    path('project/<int:id>/', views.project, name="project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
