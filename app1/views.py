from django.shortcuts import render,HttpResponse
from app1.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')
def mmg(request):
    return render(request,'mmg1.html')
    # return HttpResponse('this is mmgases fileS')


def about(request):
    return render(request,'about.html')
    #return HttpResponse('this is about fileS')


def services(request):
    return render(request,'services.html')
    #return HttpResponse('this is servies fileS')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'contact.html')
    #return HttpResponse('this is contact fileS')
def oxcygen(request):
    return render(request,"oxcygen.html")
def nitrogen(request):
    return render(request,"nitrogen.html")
def indstrial(request):
    return render(request,"indstrial.html")
