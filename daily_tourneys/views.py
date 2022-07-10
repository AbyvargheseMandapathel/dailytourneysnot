from django.shortcuts import render
from .models import BGMI
# Create your views here.

def index(request):

  dests =  BGMI.objects.all()


  return render (request, 'index.html',{'dests':dests})