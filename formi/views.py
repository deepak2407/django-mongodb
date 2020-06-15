from django.shortcuts import render
from .models import sample_collection
# Create your views here.
from django.http import HttpResponse
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['firstdb']
collection = db.formi_sample_collection

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
    x=collection.count_documents({})
    return render(request, 'sucess.html', {'val':x})