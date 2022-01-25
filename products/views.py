from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
# Create your views here.
def index(request):
    productss = Products.objects.all
    return render(request, 'index.html', {'productss': productss})
    

def new(request):
    return HttpResponse('New Products')



