# boards/views.py
from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
    
def igrande(request):
    return render(request, 'igrande.html')
    
def thesun(request):
    return render(request, 'thesun.html')

def qwf(request):
    return render(request, 'qwf.html')
    
def bprogress(request):
    return render(request, 'bprogress.html')