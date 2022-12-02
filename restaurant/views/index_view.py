from django.shortcuts import render
import traceback

def index(request):
    return render(request, 'home/index.html')