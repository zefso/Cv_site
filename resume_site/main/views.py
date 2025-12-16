from django.shortcuts import render

def home(request):
<<<<<<< HEAD
    return render(request, 'base/home.html')

def about_me(request):
    return render(request, 'main/about_me.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def experience(request):
    return render(request, 'main/experience.html')

def project(request):
    return render(request, 'main/project.html')

def skills(request):
    return render(request, 'main/skills.html')
# Create your views here.
=======
    return render(request, 'base/base.html')
>>>>>>> 75f61e8155e141f08a341450bfc440697d231ad8
