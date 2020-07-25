from django.shortcuts import render, loader
from django.http import HttpResponse
from addrecord.models import Student
from . import models
# Create your views here.
def showrecordpage(request):
    obj=Student.objects.all()
    return render(request,"show.html",{'Student':obj})

def getdata(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        ph=request.POST['phone_no']
        a=request.POST['address']
        s1=models.Student(username=u,password=p,phone_no=ph,address=a)
        s1.save() # This will save to database
        return render(request,"show.html",{"username":u,"password":p,"phone_no":ph,"address":a})    