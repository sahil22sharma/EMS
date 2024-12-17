from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")

def adminReg(request):
    return render(request, 'EMSadmin/adminReg.html')