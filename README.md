# 1. Открываем редактор или заменяем README.md полностью
@"
# Портал Онлайн-Обучения

Проект на Django 4.2.11 для управления курсами и заявками.

## Быстрый старт (Linux)

```bash
# 1. Клонируем проект
git clone https://github.com/ТВОЙ-ЛОГИН/demoexamezproj.git
cd demoexamezproj

# 2. Создаём виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Создаём БД
python manage.py migrate

# 5. Создаём админа
python manage.py createsuperuser

# 6. Загружаем курсы
python manage.py loaddata fixtures/courses.json

# 7. Создаём картинки для слайдера
mkdir -p static/img/slider/default

python3 << 'EOF'
from PIL import Image, ImageDraw

colors = [(26,86,219), (14,159,110), (245,158,11), (220,38,38)]
texts = ['Курсы вождения', 'Электробус', 'Трамвай', 'Трудоустройство']

for i, (color, text) in enumerate(zip(colors, texts)):
    img = Image.new('RGB', (1200, 500), color=color)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0,0), text)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(((1200-w)/2, (500-h)/2), text, fill='white')
    img.save(f'static/img/slider/default/slide{i+1}.jpg', 'JPEG', quality=85)

# Favicon
favicon = Image.new('RGBA', (32,32), color=(26,86,219,255))
favicon.save('static/logo/favicon.png', 'PNG')
EOF

# 8. Запускаем!
python manage.py runserver 0.0.0.0:8000