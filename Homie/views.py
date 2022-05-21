from django.shortcuts import render

# Create your views here.

def info (request):
    return render(request, 'Homie/info.html')

def join_us (request):
    return render(request, 'Homie/join_us.html')

def welcome (request):
    return render(request, 'Homie/welcome.html')