from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def addpage(request):
    f1=forms.MyForm
    return render(request,"add.html",{'form':f1})

def getdata(request):
    if request.method=='POST':
        u=request.POST['username']  
        p=request.POST['password']
        ph=request.POST['phone_no']
        a=request.POST['address']
        s1=models.Student(username=u,password=p,phone_no=ph,address=a)
        s1.save() # This will save to database
        return render(request,"add.html",{"username":u,"password":p,"phone_no":ph,"address":a})    