from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create/', views.create_item, name='create_item'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)