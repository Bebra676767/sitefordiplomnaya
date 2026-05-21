from django.db import models

# CHANGE_THEME: Измените названия курсов здесь или через админку
class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название курса')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL-идентификатор')
    description = models.TextField(blank=True, verbose_name='Описание курса')
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    
    def __str__(self):
        return self.name