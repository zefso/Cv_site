from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about_me/', views.about_me, name='about_me'),
    path('contacts/', views.contacts, name='contacts'),
    path('experience/', views.experience, name='experience'),
    path('project/', views.project, name='project'),
    path('skills/', views.skills, name='skills'),
    



=======
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
>>>>>>> 75f61e8155e141f08a341450bfc440697d231ad8
]
