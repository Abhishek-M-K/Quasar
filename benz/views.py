from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'benz/index.html')
def add_cam(request):
    return render(request,'benz/add_cam.html')