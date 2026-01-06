from django.shortcuts import render, redirect
import requests
from .forms import ContactForm
from .models import Project

def home(request):
    project = Project.objects.all().order_by('-created_at')[:4]
    return render(request, 'base/home.html', {'projects': project})

def about_me(request):
    return render(request, 'main/about_me.html')

def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # 2. ДРУКУЄМО У КОНСОЛЬ (для тесту)
        print(f"Отримано дані: {name}, {email}, {message}")
        
        if name and email and message:
            send_telegram_message(name, email, subject, message)
            success = True
            print("Повідомлення відправлено в функцію Telegram")
        else:
            print("Помилка: Якесь із полів порожнє!")
            
    return render(request, 'main/contacts.html', {'success': success})

def experience(request):
    return render(request, 'main/experience.html')

def projects(request):
    project = Project.objects.all().order_by('-created_at')
    return render(request, 'main/projects.html', {'projects': project})

def skills(request):
    return render(request, 'main/skills.html')

def send_telegram_message(name, email, subject, message):
    token = "8279558209:AAEb-CbxM-iswftzYplpLoH5nsvXJAdn70w"
    chat_id = "657820985"
    text = f"📩 Нове повідомлення!\n\n👤 Від: {name}\n📧 Email: {email}\n📌 Тема: {subject}\n📝 Текст: {message}"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    try:
        requests.post(url, data={'chat_id': chat_id, 'text': text}, timeout=5)
    except Exception as e:
        print(f"Помилка відправки: {e}")

def custom_404(request, exception):
    return render(request, '404.html', status=404)