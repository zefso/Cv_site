from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва проєкту")
    description = models.TextField(verbose_name="Опис")
    image = models.ImageField(upload_to='projects/', verbose_name="Зображення")
    link = models.URLField(blank=True, verbose_name="Посилання на сайт/GitHub")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проєкт"
        verbose_name_plural = "Проєкти"