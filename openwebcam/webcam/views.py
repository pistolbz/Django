from django.shortcuts import render
from django.http import HttpResponse
from .opencv import capPhoto, openWebcam

def index(request):
    if request.GET.get('btn_takephoto'):
        capPhoto()
    return render(request, 'index.html')
