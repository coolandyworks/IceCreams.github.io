from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"ANAND KUMAR TRIPATHI"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is a homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is a aboutpage")

def services(request):
    return render(request, 'services.html')
    r#eturn HttpResponse("this is a servicepage")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'form has been submitted succesfully')

    return render(request, 'contact.html')
    #return HttpResponse("this is a contact page")