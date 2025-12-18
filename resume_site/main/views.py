from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def about_me(request):
    return render(request, 'main/about_me.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def experience(request):
    return render(request, 'main/experience.html')

def projects(request):
    return render(request, 'main/projects.html')

def skills(request):
    return render(request, 'main/skills.html')
# Create your views here.

