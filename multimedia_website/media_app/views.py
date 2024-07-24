from django.shortcuts import render, redirect
from .models import Image, Video, Audio
from .forms import ImageForm, VideoForm, AudioForm

def home(request):
    images = Image.objects.all()
    videos = Video.objects.all()
    audios = Audio.objects.all()
    return render(request, 'media_app/home.html', {'images': images, 'videos': videos, 'audios': audios})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'media_app/upload_image.html', {'form': form})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'media_app/upload_video.html', {'form': form})

def upload_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AudioForm()
    return render(request, 'media_app/upload_audio.html', {'form': form})
