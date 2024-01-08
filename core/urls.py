from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('',views.index, name='home'),
    path('calculation',views.calculation)
    ]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    