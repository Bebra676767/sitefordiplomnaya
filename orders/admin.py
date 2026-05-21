from django.contrib import admin
from .models import Application

def make_in_progress(modeladmin, request, queryset):
    queryset.update(status='in_progress')
make_in_progress.short_description = 'Перевести в "Идет обучение"'

def make_completed(modeladmin, request, queryset):
    queryset.update(status='completed')
make_completed.short_description = 'Перевести в "Обучение завершено"'

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course', 'start_date', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['status', 'course', 'start_date']
    search_fields = ['user__username', 'user__profile__fio']
    actions = [make_in_progress, make_completed]
    date_hierarchy = 'created_at'