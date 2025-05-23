# La Riviera Restaurant Website

Повноцінний веб-застосунок для ресторану "La Riviera" на основі Django з використанням HTML, CSS (Bootstrap 5) та Django Template Language.

## Функціональність

- **Головна сторінка**: Фото ресторану, короткий опис, слайдер із фото страв та інтер'єру
- **Меню**: Категорії страв з можливістю додавання до замовлення
- **Кошик та оформлення замовлення**: Перегляд доданих страв, оформлення замовлення
- **Бронювання столиків**: Форма для вибору дати, часу та кількості гостей
- **Події та акції**: Перелік майбутніх подій та спеціальних пропозицій
- **Сторінка "Про нас"**: Історія ресторану, інформація про шеф-кухаря та команду
- **Контакти**: Карта, адреса, телефон, форма зворотного зв'язку

## Технічні деталі

- **Фреймворк**: Django
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **База даних**: SQLite (за замовчуванням)
- **Адаптивний дизайн**: Підтримка мобільних та десктопних пристроїв

## Встановлення та запуск

1. Клонуйте репозиторій:
   ```
   git clone <repository-url>
   cd la_riviera
   ```

2. Створіть та активуйте віртуальне середовище:
   ```
   python -m venv venv
   venv\Scripts\activate  # для Windows
   source venv/bin/activate  # для Linux/Mac
   ```

3. Встановіть залежності:
   ```
   pip install -r requirements.txt
   ```

4. Виконайте міграції:
   ```
   python manage.py migrate
   ```

5. Створіть суперкористувача для доступу до адмін-панелі:
   ```
   python manage.py createsuperuser
   ```

6. Запустіть сервер розробки:
   ```
   python manage.py runserver
   ```

7. Відкрийте браузер та перейдіть за адресою http://127.0.0.1:8000/

## Адміністрування

Адмін-панель доступна за адресою http://127.0.0.1:8000/admin/

В адмін-панелі ви можете:
- Додавати/редагувати/видаляти категорії та страви меню
- Керувати бронюваннями столиків
- Переглядати та обробляти замовлення
- Додавати події та акції
- Керувати командою ресторану та відгуками

## Структура проекту

- **core**: Базовий додаток з головною сторінкою, сторінками "Про нас" та "Контакти"
- **menu**: Додаток для керування меню ресторану
- **reservation**: Додаток для бронювання столиків
- **order**: Додаток для оформлення замовлень
- **events**: Додаток для керування подіями та акціями

## Додаткова інформація

Для повноцінної роботи веб-застосунку рекомендується:
1. Додати реальні фотографії страв та ресторану
2. Налаштувати відправку електронних листів для підтвердження бронювань та замовлень
3. Налаштувати платіжну систему для онлайн-оплати замовлень

## Автор

Розроблено для ресторану "La Riviera"
#   R e s t o r a n _ k a i f  
 