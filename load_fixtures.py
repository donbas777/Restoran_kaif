import os
import django
import subprocess

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'la_riviera.settings')
django.setup()

# Створюємо директорії для медіа-файлів, якщо вони не існують
media_dirs = [
    'media/categories',
    'media/dishes',
    'media/events',
    'media/promotions',
    'media/team',
    'media/testimonials'
]

for directory in media_dirs:
    os.makedirs(directory, exist_ok=True)

# Список фікстур для завантаження в правильному порядку
fixtures = [
    'categories.json',
    'dishes.json',
    'tables.json',
    'events.json',
    'promotions.json',
    'team.json',
    'testimonials.json'
]

# Завантажуємо фікстури
for fixture in fixtures:
    print(f"Завантаження фікстури {fixture}...")
    result = subprocess.run(['python', 'manage.py', 'loaddata', f'fixtures/{fixture}'], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Фікстура {fixture} успішно завантажена.")
    else:
        print(f"Помилка при завантаженні фікстури {fixture}:")
        print(result.stderr)

print("Всі фікстури завантажено успішно!")
