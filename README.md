@"
# Портал Онлайн-Обучения

Проект на Django 4.2.11 для управления курсами и заявками.

## Установка
```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures/courses.json
python manage.py runserver

"@ | Out-File -FilePath README.md -Encoding UTF8