from django.shortcuts import render
from .models import Course

def index(request):
    courses = Course.objects.all()[:6]
    context = {
        'courses': courses,
        # CHANGE_THEME: Измените заголовок главной страницы
        'hero_title': 'Профессиональное обучение вождению',
        'hero_subtitle': 'Получите права категории D и станьте водителем общественного транспорта',
    }
    return render(request, 'index.html', context)