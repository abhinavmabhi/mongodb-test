from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_item,name="create_item"),
    path('base/',views.index,name='index'),
]