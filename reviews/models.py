from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    application = models.ForeignKey('orders.Application', on_delete=models.CASCADE, verbose_name='Заявка')
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Отзыв от {self.user.username} к заявке #{self.application.id}'
    
    def clean(self):
        if self.application_id:
            from orders.models import Application
            try:
                app = Application.objects.get(pk=self.application_id)
                if app.status != 'completed':
                    raise ValidationError('Отзыв можно оставить только для завершенного обучения')
            except Application.DoesNotExist:
                pass
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)