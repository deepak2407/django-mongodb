from django.shortcuts import render
from .models import sample_collection
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'GET':
        post=sample_collection()
        post.data= request.GET['name1']
        post.save()
        return render(request, 'sucess.html', {'val': post.data})  

    else:
        return render(request,'index.html')

def showData(request):
    x=sample_collection.objects.filter(data='abc')
    return render(request, 'sucess.html', {'val':x})