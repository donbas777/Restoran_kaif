import os
import django
import datetime
from decimal import Decimal
import sqlite3
import json

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'la_riviera.settings')
django.setup()

# Імпортуємо необхідні модулі
from django.conf import settings
from django.utils import timezone

# Шлях до бази даних
db_path = settings.DATABASES['default']['NAME']
print(f"Використовуємо базу даних: {db_path}")

def execute_sql(sql, params=None):
    """Виконати SQL запит"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)
    conn.commit()
    conn.close()

def execute_sql_fetch(sql, params=None):
    """Виконати SQL запит і повернути результат"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

def create_categories():
    """Створення категорій меню"""
    categories = [
        {
            'name': 'Закуски',
            'slug': 'zakusky',
            'description': 'Легкі закуски для початку трапези',
            'order': 1,
        },
        {
            'name': 'Супи',
            'slug': 'supy',
            'description': 'Гарячі та холодні супи',
            'order': 2,
        },
        {
            'name': 'Основні страви',
            'slug': 'osnovni-stravy',
            'description': 'Вишукані основні страви',
            'order': 3,
        },
        {
            'name': 'Десерти',
            'slug': 'deserty',
            'description': 'Солодкі десерти та випічка',
            'order': 4,
        },
        {
            'name': 'Напої',
            'slug': 'napoi',
            'description': 'Безалкогольні та алкогольні напої',
            'order': 5,
        },
    ]
    
    for cat_data in categories:
        # Перевіряємо, чи існує категорія
        existing = execute_sql_fetch(
            "SELECT id FROM menu_category WHERE name = ?", 
            (cat_data['name'],)
        )
        
        if existing:
            print(f"Категорія вже існує: {cat_data['name']}")
            continue
        
        # Створюємо категорію
        execute_sql(
            """
            INSERT INTO menu_category (name, slug, description, order)
            VALUES (?, ?, ?, ?)
            """,
            (
                cat_data['name'],
                cat_data['slug'],
                cat_data['description'],
                cat_data['order'],
            )
        )
        print(f"Створено категорію: {cat_data['name']}")

def create_dishes():
    """Створення страв"""
    dishes = [
        {
            'name': 'Карпаччо з телятини',
            'category_name': 'Закуски',
            'description': 'Тонко нарізана телятина з руколою, пармезаном та оливковою олією',
            'price': 320.00,
            'is_vegetarian': 0,
            'is_special': 1,
            'is_available': 1,
            'preparation_time': 15,
        },
        {
            'name': 'Брускетта з томатами',
            'category_name': 'Закуски',
            'description': 'Хрусткий багет з томатами, базиліком та оливковою олією',
            'price': 180.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 10,
        },
        {
            'name': 'Тартар з лосося',
            'category_name': 'Закуски',
            'description': 'Свіжий лосось з авокадо, цибулею та лимонним соком',
            'price': 350.00,
            'is_vegetarian': 0,
            'is_special': 1,
            'is_available': 1,
            'preparation_time': 20,
        },
        {
            'name': 'Борщ український',
            'category_name': 'Супи',
            'description': 'Традиційний український борщ з яловичиною та сметаною',
            'price': 200.00,
            'is_vegetarian': 0,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 30,
        },
        {
            'name': 'Крем-суп з грибів',
            'category_name': 'Супи',
            'description': 'Ніжний крем-суп з білих грибів з трюфельною олією',
            'price': 250.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 25,
        },
        {
            'name': 'Гаспачо',
            'category_name': 'Супи',
            'description': 'Холодний іспанський суп з томатів та овочів',
            'price': 220.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 15,
        },
        {
            'name': 'Філе міньйон',
            'category_name': 'Основні страви',
            'description': 'Соковите філе яловичини з картопляним пюре та соусом деміглас',
            'price': 550.00,
            'is_vegetarian': 0,
            'is_special': 1,
            'is_available': 1,
            'preparation_time': 35,
        },
        {
            'name': 'Різотто з грибами',
            'category_name': 'Основні страви',
            'description': 'Кремове різотто з білими грибами та пармезаном',
            'price': 320.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 30,
        },
        {
            'name': 'Лосось на грилі',
            'category_name': 'Основні страви',
            'description': 'Лосось на грилі з овочами та лимонним соусом',
            'price': 420.00,
            'is_vegetarian': 0,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 25,
        },
        {
            'name': 'Тірамісу',
            'category_name': 'Десерти',
            'description': 'Класичний італійський десерт з маскарпоне та кавою',
            'price': 180.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 20,
        },
        {
            'name': 'Шоколадний фондан',
            'category_name': 'Десерти',
            'description': 'Теплий шоколадний кекс з рідкою серединою та ванільним морозивом',
            'price': 220.00,
            'is_vegetarian': 1,
            'is_special': 1,
            'is_available': 1,
            'preparation_time': 15,
        },
        {
            'name': 'Чізкейк',
            'category_name': 'Десерти',
            'description': 'Ніжний чізкейк з ягідним соусом',
            'price': 190.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 15,
        },
        {
            'name': 'Лимонад домашній',
            'category_name': 'Напої',
            'description': 'Освіжаючий лимонад з лимоном та м\'ятою',
            'price': 120.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 5,
        },
        {
            'name': 'Вино червоне',
            'category_name': 'Напої',
            'description': 'Сухе червоне вино Каберне Совіньйон',
            'price': 350.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 1,
        },
        {
            'name': 'Еспресо',
            'category_name': 'Напої',
            'description': 'Класичний італійський еспресо',
            'price': 80.00,
            'is_vegetarian': 1,
            'is_special': 0,
            'is_available': 1,
            'preparation_time': 3,
        },
    ]
    
    # Отримуємо категорії
    categories = execute_sql_fetch("SELECT id, name FROM menu_category")
    category_dict = {name: id for id, name in categories}
    
    for dish_data in dishes:
        category_id = category_dict.get(dish_data['category_name'])
        if not category_id:
            print(f"Помилка: категорія {dish_data['category_name']} не знайдена")
            continue
        
        # Перевіряємо, чи існує страва
        existing = execute_sql_fetch(
            "SELECT id FROM menu_dish WHERE name = ?", 
            (dish_data['name'],)
        )
        
        if existing:
            print(f"Страва вже існує: {dish_data['name']}")
            continue
        
        # Створюємо slug
        slug = dish_data['name'].lower().replace(' ', '-').replace("'", '').replace('"', '')
        
        # Поточний час
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Створюємо страву
        execute_sql(
            """
            INSERT INTO menu_dish (
                name, slug, description, price, 
                is_vegetarian, is_special, is_available, 
                created_at, updated_at, category_id, preparation_time
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                dish_data['name'],
                slug,
                dish_data['description'],
                dish_data['price'],
                dish_data['is_vegetarian'],
                dish_data['is_special'],
                dish_data['is_available'],
                now,
                now,
                category_id,
                dish_data['preparation_time'],
            )
        )
        print(f"Створено страву: {dish_data['name']}")

def create_tables():
    """Створення столиків"""
    tables = [
        {'number': 1, 'capacity': 2, 'location': 'Біля вікна'},
        {'number': 2, 'capacity': 2, 'location': 'Біля вікна'},
        {'number': 3, 'capacity': 4, 'location': 'Центр залу'},
        {'number': 4, 'capacity': 4, 'location': 'Центр залу'},
        {'number': 5, 'capacity': 6, 'location': 'Біля каміна'},
        {'number': 6, 'capacity': 8, 'location': 'VIP зона'},
    ]
    
    for table_data in tables:
        # Перевіряємо, чи існує столик
        existing = execute_sql_fetch(
            "SELECT id FROM reservation_table WHERE number = ?", 
            (table_data['number'],)
        )
        
        if existing:
            print(f"Столик вже існує: {table_data['number']}")
            continue
        
        # Створюємо столик
        execute_sql(
            """
            INSERT INTO reservation_table (number, capacity, location, is_active)
            VALUES (?, ?, ?, ?)
            """,
            (
                table_data['number'],
                table_data['capacity'],
                table_data['location'],
                1,  # is_active = True
            )
        )
        print(f"Створено столик: {table_data['number']}")

def create_events():
    """Створення подій"""
    events = [
        {
            'title': 'Вечір італійської кухні',
            'description': 'Спеціальний вечір, присвячений італійській кухні. Наш шеф-кухар приготує автентичні італійські страви, які ви зможете скуштувати під акомпанемент італійських вин.',
            'start_date': '2025-05-15',
            'end_date': '2025-05-15',
            'start_time': '18:00:00',
            'end_time': '22:00:00',
            'location': 'Ресторан La Riviera',
            'price': 500.00,
            'is_free': 0,
        },
        {
            'title': 'Дегустація вин',
            'description': 'Запрошуємо вас на дегустацію вин від кращих виноробів Європи. Ви зможете спробувати різні сорти вин та дізнатися більше про культуру виноробства.',
            'start_date': '2025-05-20',
            'end_date': '2025-05-20',
            'start_time': '19:00:00',
            'end_time': '22:00:00',
            'location': 'Винний погріб La Riviera',
            'price': 600.00,
            'is_free': 0,
        },
        {
            'title': 'Майстер-клас з приготування десертів',
            'description': 'Наш шеф-кондитер проведе майстер-клас з приготування вишуканих десертів. Ви дізнаєтесь секрети приготування тірамісу, панакоти та шоколадного фондану.',
            'start_date': '2025-05-25',
            'end_date': '2025-05-25',
            'start_time': '15:00:00',
            'end_time': '18:00:00',
            'location': 'Кулінарна студія La Riviera',
            'price': 400.00,
            'is_free': 0,
        },
        {
            'title': 'Джазовий вечір',
            'description': 'Проведіть вечір під звуки живого джазу. Насолоджуйтесь вишуканими стравами та напоями під акомпанемент джазового тріо.',
            'start_date': '2025-06-05',
            'end_date': '2025-06-05',
            'start_time': '19:00:00',
            'end_time': '23:00:00',
            'location': 'Ресторан La Riviera',
            'price': 300.00,
            'is_free': 0,
        },
    ]
    
    for event_data in events:
        # Перевіряємо, чи існує подія
        existing = execute_sql_fetch(
            "SELECT id FROM events_event WHERE title = ?", 
            (event_data['title'],)
        )
        
        if existing:
            print(f"Подія вже існує: {event_data['title']}")
            continue
        
        # Поточний час
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Створюємо подію
        execute_sql(
            """
            INSERT INTO events_event (
                title, description, start_date, end_date, 
                start_time, end_time, location, price, is_free,
                created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_data['title'],
                event_data['description'],
                event_data['start_date'],
                event_data['end_date'],
                event_data['start_time'],
                event_data['end_time'],
                event_data['location'],
                event_data['price'],
                event_data['is_free'],
                now,
                now,
            )
        )
        print(f"Створено подію: {event_data['title']}")

def create_promotions():
    """Створення акцій"""
    promotions = [
        {
            'title': 'Щасливі години',
            'description': 'Знижка 20% на всі напої з 17:00 до 19:00 з понеділка по четвер.',
            'start_date': '2025-05-01',
            'end_date': '2025-06-30',
            'is_active': 1,
            'discount_percent': 20,
            'discount_amount': None,
        },
        {
            'title': 'Сімейна неділя',
            'description': 'Знижка 15% на все меню для сімей з дітьми щонеділі.',
            'start_date': '2025-05-01',
            'end_date': '2025-06-30',
            'is_active': 1,
            'discount_percent': 15,
            'discount_amount': None,
        },
        {
            'title': 'День народження',
            'description': 'Знижка 30% на все меню в день вашого народження (при пред\'явленні документа).',
            'start_date': '2025-05-01',
            'end_date': '2025-12-31',
            'is_active': 1,
            'discount_percent': 30,
            'discount_amount': None,
        },
    ]
    
    for promo_data in promotions:
        # Перевіряємо, чи існує акція
        existing = execute_sql_fetch(
            "SELECT id FROM events_promotion WHERE title = ?", 
            (promo_data['title'],)
        )
        
        if existing:
            print(f"Акція вже існує: {promo_data['title']}")
            continue
        
        # Поточний час
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Створюємо акцію
        execute_sql(
            """
            INSERT INTO events_promotion (
                title, description, start_date, end_date, 
                is_active, discount_percent, discount_amount,
                created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                promo_data['title'],
                promo_data['description'],
                promo_data['start_date'],
                promo_data['end_date'],
                promo_data['is_active'],
                promo_data['discount_percent'],
                promo_data['discount_amount'],
                now,
                now,
            )
        )
        print(f"Створено акцію: {promo_data['title']}")

def create_team_members():
    """Створення команди ресторану"""
    team_members = [
        {
            'name': 'Олександр Петренко',
            'position': 'Шеф-кухар',
            'bio': 'Олександр має більше 15 років досвіду роботи в кращих ресторанах Європи. Він спеціалізується на середземноморській кухні та постійно вдосконалює своє мистецтво.',
            'is_active': 1,
            'order': 1,
        },
        {
            'name': 'Марія Коваленко',
            'position': 'Шеф-кондитер',
            'bio': 'Марія - талановитий кондитер з досвідом роботи в Парижі. Її десерти - справжні витвори мистецтва, які не залишать байдужими навіть найвибагливіших гурманів.',
            'is_active': 1,
            'order': 2,
        },
        {
            'name': 'Ігор Савченко',
            'position': 'Сомельє',
            'bio': 'Ігор - сертифікований сомельє з багаторічним досвідом. Він допоможе вам обрати ідеальне вино до вашої страви та розповість про особливості кожного сорту.',
            'is_active': 1,
            'order': 3,
        },
        {
            'name': 'Наталія Іванова',
            'position': 'Менеджер ресторану',
            'bio': 'Наталія відповідає за бездоганний сервіс та комфорт наших гостей. Вона завжди готова допомогти з організацією вашого візиту та зробити його незабутнім.',
            'is_active': 1,
            'order': 4,
        },
    ]
    
    for member_data in team_members:
        # Перевіряємо, чи існує член команди
        existing = execute_sql_fetch(
            "SELECT id FROM core_teammember WHERE name = ?", 
            (member_data['name'],)
        )
        
        if existing:
            print(f"Член команди вже існує: {member_data['name']}")
            continue
        
        # Створюємо члена команди
        execute_sql(
            """
            INSERT INTO core_teammember (name, position, bio, is_active, order)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                member_data['name'],
                member_data['position'],
                member_data['bio'],
                member_data['is_active'],
                member_data['order'],
            )
        )
        print(f"Створено члена команди: {member_data['name']}")

def create_testimonials():
    """Створення відгуків"""
    testimonials = [
        {
            'name': 'Олена Мельник',
            'text': 'Неймовірний ресторан з чудовою атмосферою та смачними стравами. Особливо сподобалось різотто з грибами та тірамісу. Обов\'язково повернемось!',
            'rating': 5,
            'is_active': 1,
        },
        {
            'name': 'Андрій Ковальчук',
            'text': 'Святкували річницю весілля в La Riviera. Все було на вищому рівні - від обслуговування до якості страв. Дякуємо за незабутній вечір!',
            'rating': 5,
            'is_active': 1,
        },
        {
            'name': 'Марина Шевченко',
            'text': 'Відвідали ресторан під час відпустки в Ковелі. Чудовий сервіс, вишукані страви та приємна атмосфера. Філе міньйон просто тане в роті!',
            'rating': 4,
            'is_active': 1,
        },
        {
            'name': 'Віктор Лисенко',
            'text': 'Проводили корпоратив в La Riviera. Все було організовано на найвищому рівні. Особлива подяка шеф-кухарю за неймовірні страви та персоналу за уважність до деталей.',
            'rating': 5,
            'is_active': 1,
        },
    ]
    
    for testimonial_data in testimonials:
        # Перевіряємо, чи існує відгук
        existing = execute_sql_fetch(
            "SELECT id FROM core_testimonial WHERE name = ?", 
            (testimonial_data['name'],)
        )
        
        if existing:
            print(f"Відгук вже існує від: {testimonial_data['name']}")
            continue
        
        # Поточний час
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Створюємо відгук
        execute_sql(
            """
            INSERT INTO core_testimonial (name, text, rating, is_active, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                testimonial_data['name'],
                testimonial_data['text'],
                testimonial_data['rating'],
                testimonial_data['is_active'],
                now,
            )
        )
        print(f"Створено відгук від: {testimonial_data['name']}")

def main():
    """Головна функція для заповнення бази даних"""
    print("Заповнення бази даних тестовими даними...")
    
    print("\nСтворення категорій...")
    create_categories()
    
    print("\nСтворення страв...")
    create_dishes()
    
    print("\nСтворення столиків...")
    create_tables()
    
    print("\nСтворення подій...")
    create_events()
    
    print("\nСтворення акцій...")
    create_promotions()
    
    print("\nСтворення команди ресторану...")
    create_team_members()
    
    print("\nСтворення відгуків...")
    create_testimonials()
    
    print("\nБаза даних успішно заповнена тестовими даними!")

if __name__ == "__main__":
    main()
