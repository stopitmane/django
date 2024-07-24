from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Audio(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audios/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
