import os
import subprocess

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic
from play.models import Movie

from video.settings import BASE_DIR


class IndexView(generic.ListView):
    template_name = 'play/index.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.all()

def ffmpeg_stream_upload(self):
    rtmpUrl = "rtmp://localhost:1935/zbcs/room"
    file_path = '/Users/dft/project/video/static/else/Feng.mp4'
    # ffmpeg command
    command = ['ffmpeg', '-re', '-i', file_path, '-vcodec', 'copy', '-acodec', 'copy', '-r', '60',
           '-f', 'flv', rtmpUrl]

    process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8",
                               text=True)
    for line in process.stdout:
        print(line)
    process.wait()
    if process.poll() == 0:
        print("success:", process)
    else:
        print("error:", process)

    # to-do
    # web开始获取视频流
    #
    #返回视频播放页面

    return