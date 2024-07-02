from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"entidades/index.html")

def contact(request):
    return render(request,"entidades/contact.html")

def projects(request):
    return render(request,"entidades/projects.html")

def resume(request):
    return render(request,"entidades/resume.html")