from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse 
from .models import Project, Tag, Contact
from django.contrib import messages
from main import models



# Create your views here.

def home(request):
    
    return render(request, "home.html")

def contact(request):
    if request.method=="POST":
        print('Post request received')

        name =request.POST.get("name")
        email =request.POST.get("email")
        contact =request.POST.get("contact")#
        print(name,email,contact)

        if len(name)>1 and len(name)<25:
           pass
        else:
           messages.error(request, 'Length of name should be greater than 1 and less then 25 words ')
           return render(request, 'home.html')
        
        if len(email)>1 and len(email)<15:
           pass
        else:
           messages.error(request, 'Email not valid ')
           return render(request, 'home.html')
        
        if len(contact)>1 and len(contact)<15:
           pass
        else:
           messages.error(request, 'Invalid number')
           return render(request, 'home.html')
        contact_entry = Contact(name=name, email=email, contact=contact)
        contact_entry.save()

        messages.success(request, "Thank you for contacting me! Your message has been received.")
        print("Data saved successfully 🎉")
    return render(request, "home.html")

   
   
def project(request, id):
    return render(request, "project.html")

       