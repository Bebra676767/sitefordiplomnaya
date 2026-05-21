from django.conf import settings

def site_info(request):
    # CHANGE_THEME: Измените название и описание сайта
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'Портал Онлайн-Обучения'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', 'Профессиональное обучение вождению'),
        'THEME': getattr(settings, 'THEME_CONFIG', {}),
    }