from django.contrib import admin
from django.urls import path
from main import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    
    path('about_me/', views.about_me, name='about_me'),
    path('contacts/', views.contacts, name='contacts'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    
]
