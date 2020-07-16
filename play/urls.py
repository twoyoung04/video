from django.urls import path

from . import views

app_name = 'play'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('upload/', views.ffmpeg_stream_upload, name = 'upload')
]