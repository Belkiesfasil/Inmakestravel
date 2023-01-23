from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Persons

# Create your views here.
def demo(request):

     obj=Place.objects.all()
     obj1=Persons.objects.all()
     # name="india"
     # return render(request,"home.html",{'obj':name})
     return render(request,"index.html",{'result':obj,'result1':obj1})

# def about(request):
#      return render(request,"about.html")
# def contact(request):
#      return HttpResponse("Helloooo...am contact")
def addition(request):
     x=int(request.GET['num1'])
     y=int(request.GET['num2'])
     res=x+y
     return render(request,"result.html",{'result':res})
