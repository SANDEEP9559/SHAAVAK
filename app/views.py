# from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect



from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def media(request):
    return render(request, 'media.html')

def van(request):
    all_data =  Van.objects.all()
    return render(request, 'van_services.html', {'key1':all_data})

def bus(request):
    all_data = Bus.objects.all()
    return render(request, 'bus_services.html',{'key1':all_data})

def rickshaw(request):
    all_data =  Rickshaw.objects.all()
    return render(request, 'rickshaw_services.html', {'key1':all_data})
