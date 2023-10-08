from django.shortcuts import render
from .models import *



def base(request):
    return render(request , 'base.html' , {})

def video_darslar(request):
    video_darslar = Darslar.objects.all()
    
    return render(request , 'video-darslar.html' , {'video_dars':video_darslar,})

def dars(request, slug):
    dars = Darslar.objects.get(slug=slug)
    return render(request, "dars.html", {'darslar': dars,})

def korsatmalar(request):
    return render(request , 'korsatmalar.html' , {})

def vakansiyalar(request):
    vakansiyalar = Vakansiyalar.objects.all()
    return render(request , 'vakansiyalar.html' , {'vakansiya':vakansiyalar,})

def istedodlilar(request):
    istedodlilar = Istedodlilar.objects.all()
    return render(request , 'istedodlilar.html' , {'istedod':istedodlilar,})

def foydali_havolalar(request):
    foydali_havolalar = FoydaliHavolalar.objects.all()
    return render(request , 'foydali-havolalar.html' , {'foydali_havola':foydali_havolalar,})
