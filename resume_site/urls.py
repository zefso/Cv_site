from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import set_language
from django.conf.urls.i18n import i18n_patterns

# 1. Шляхи, які не потребують перекладу (Адмінка та логіка перемикання)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set-language/<str:lang_code>/', set_language, name='set_language'),
]

# 2. Шляхи з мовними префіксами (/uk/, /en/, /pl/)
urlpatterns += i18n_patterns(
    path('', include('main.urls')), # Це підтягне всі маршрути з твого додатка main
)

# 3. Налаштування для медіа-файлів (тільки для розробки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'main.views.custom_404'