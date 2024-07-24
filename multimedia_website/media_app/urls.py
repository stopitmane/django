from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('upload_audio/', views.upload_audio, name='upload_audio'),
]
