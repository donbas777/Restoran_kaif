import os
import django
import datetime
from decimal import Decimal

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'la_riviera.settings')
django.setup()

# Імпортуємо моделі після налаштування Django
from django.utils import timezone
from menu.models import Category, Dish
from reservation.models import Table
from events.models import Event, Promotion
from core.models import TeamMember, Testimonial

def create_categories():
    """Створення категорій меню"""
    categories = [
        {
            'name': 'Закуски',
            'slug': 'zakusky',
            'description': 'Легкі закуски для початку трапези',
        },
        {
            'name': 'Супи',
            'slug': 'supy',
            'description': 'Гарячі та холодні супи',
        },
        {
            'name': 'Основні страви',
            'slug': 'osnovni-stravy',
            'description': 'Вишукані основні страви',
        },
        {
            'name': 'Десерти',
            'slug': 'deserty',
            'description': 'Солодкі десерти та випічка',
        },
        {
            'name': 'Напої',
            'slug': 'napoi',
            'description': 'Безалкогольні та алкогольні напої',
        },
    ]
    
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'slug': cat_data['slug'],
                'description': cat_data['description'],
            }
        )
        if created:
            print(f"Створено категорію: {category.name}")
        else:
            print(f"Категорія вже існує: {category.name}")
    
    return Category.objects.all()

def create_dishes(categories):
    """Створення страв"""
    dishes = [
        {
            'name': 'Карпаччо з телятини',
            'category_name': 'Закуски',
            'description': 'Тонко нарізана телятина з руколою, пармезаном та оливковою олією',
            'price': Decimal('320.00'),
            'is_vegetarian': False,
            'is_special': True,
            'is_available': True,
            'preparation_time': 15,
        },
        {
            'name': 'Брускетта з томатами',
            'category_name': 'Закуски',
            'description': 'Хрусткий багет з томатами, базиліком та оливковою олією',
            'price': Decimal('180.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 10,
        },
        {
            'name': 'Тартар з лосося',
            'category_name': 'Закуски',
            'description': 'Свіжий лосось з авокадо, цибулею та лимонним соком',
            'price': Decimal('350.00'),
            'is_vegetarian': False,
            'is_special': True,
            'is_available': True,
            'preparation_time': 20,
        },
        {
            'name': 'Борщ український',
            'category_name': 'Супи',
            'description': 'Традиційний український борщ з яловичиною та сметаною',
            'price': Decimal('200.00'),
            'is_vegetarian': False,
            'is_special': False,
            'is_available': True,
            'preparation_time': 30,
        },
        {
            'name': 'Крем-суп з грибів',
            'category_name': 'Супи',
            'description': 'Ніжний крем-суп з білих грибів з трюфельною олією',
            'price': Decimal('250.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 25,
        },
        {
            'name': 'Гаспачо',
            'category_name': 'Супи',
            'description': 'Холодний іспанський суп з томатів та овочів',
            'price': Decimal('220.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 15,
        },
        {
            'name': 'Філе міньйон',
            'category_name': 'Основні страви',
            'description': 'Соковите філе яловичини з картопляним пюре та соусом деміглас',
            'price': Decimal('550.00'),
            'is_vegetarian': False,
            'is_special': True,
            'is_available': True,
            'preparation_time': 35,
        },
        {
            'name': 'Різотто з грибами',
            'category_name': 'Основні страви',
            'description': 'Кремове різотто з білими грибами та пармезаном',
            'price': Decimal('320.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 30,
        },
        {
            'name': 'Лосось на грилі',
            'category_name': 'Основні страви',
            'description': 'Лосось на грилі з овочами та лимонним соусом',
            'price': Decimal('420.00'),
            'is_vegetarian': False,
            'is_special': False,
            'is_available': True,
            'preparation_time': 25,
        },
        {
            'name': 'Тірамісу',
            'category_name': 'Десерти',
            'description': 'Класичний італійський десерт з маскарпоне та кавою',
            'price': Decimal('180.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 20,
        },
        {
            'name': 'Шоколадний фондан',
            'category_name': 'Десерти',
            'description': 'Теплий шоколадний кекс з рідкою серединою та ванільним морозивом',
            'price': Decimal('220.00'),
            'is_vegetarian': True,
            'is_special': True,
            'is_available': True,
            'preparation_time': 15,
        },
        {
            'name': 'Чізкейк',
            'category_name': 'Десерти',
            'description': 'Ніжний чізкейк з ягідним соусом',
            'price': Decimal('190.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 15,
        },
        {
            'name': 'Лимонад домашній',
            'category_name': 'Напої',
            'description': 'Освіжаючий лимонад з лимоном та м\'ятою',
            'price': Decimal('120.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 5,
        },
        {
            'name': 'Вино червоне',
            'category_name': 'Напої',
            'description': 'Сухе червоне вино Каберне Совіньйон',
            'price': Decimal('350.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 1,
        },
        {
            'name': 'Еспресо',
            'category_name': 'Напої',
            'description': 'Класичний італійський еспресо',
            'price': Decimal('80.00'),
            'is_vegetarian': True,
            'is_special': False,
            'is_available': True,
            'preparation_time': 3,
        },
    ]
    
    # Створюємо словник для швидкого пошуку категорій за назвою
    category_dict = {category.name: category for category in categories}
    
    for dish_data in dishes:
        category = category_dict.get(dish_data['category_name'])
        if not category:
            print(f"Помилка: категорія {dish_data['category_name']} не знайдена")
            continue
        
        dish, created = Dish.objects.get_or_create(
            name=dish_data['name'],
            defaults={
                'category': category,
                'description': dish_data['description'],
                'price': dish_data['price'],
                'is_vegetarian': dish_data['is_vegetarian'],
                'is_special': dish_data['is_special'],
                'is_available': dish_data['is_available'],
                'preparation_time': dish_data['preparation_time'],
            }
        )
        if created:
            print(f"Створено страву: {dish.name}")
        else:
            print(f"Страва вже існує: {dish.name}")

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
        table, created = Table.objects.get_or_create(
            number=table_data['number'],
            defaults={
                'capacity': table_data['capacity'],
                'location': table_data['location'],
                'is_active': True,
            }
        )
        if created:
            print(f"Створено столик: {table.number}")
        else:
            print(f"Столик вже існує: {table.number}")

def create_events():
    """Створення подій"""
    events = [
        {
            'title': 'Вечір італійської кухні',
            'description': 'Спеціальний вечір, присвячений італійській кухні. Наш шеф-кухар приготує автентичні італійські страви, які ви зможете скуштувати під акомпанемент італійських вин.',
            'start_date': datetime.date(2025, 5, 15),
            'end_date': datetime.date(2025, 5, 15),
            'start_time': datetime.time(18, 0),
            'end_time': datetime.time(22, 0),
            'location': 'Ресторан La Riviera',
            'price': Decimal('500.00'),
            'is_free': False,
        },
        {
            'title': 'Дегустація вин',
            'description': 'Запрошуємо вас на дегустацію вин від кращих виноробів Європи. Ви зможете спробувати різні сорти вин та дізнатися більше про культуру виноробства.',
            'start_date': datetime.date(2025, 5, 20),
            'end_date': datetime.date(2025, 5, 20),
            'start_time': datetime.time(19, 0),
            'end_time': datetime.time(22, 0),
            'location': 'Винний погріб La Riviera',
            'price': Decimal('600.00'),
            'is_free': False,
        },
        {
            'title': 'Майстер-клас з приготування десертів',
            'description': 'Наш шеф-кондитер проведе майстер-клас з приготування вишуканих десертів. Ви дізнаєтесь секрети приготування тірамісу, панакоти та шоколадного фондану.',
            'start_date': datetime.date(2025, 5, 25),
            'end_date': datetime.date(2025, 5, 25),
            'start_time': datetime.time(15, 0),
            'end_time': datetime.time(18, 0),
            'location': 'Кулінарна студія La Riviera',
            'price': Decimal('400.00'),
            'is_free': False,
        },
        {
            'title': 'Джазовий вечір',
            'description': 'Проведіть вечір під звуки живого джазу. Насолоджуйтесь вишуканими стравами та напоями під акомпанемент джазового тріо.',
            'start_date': datetime.date(2025, 6, 5),
            'end_date': datetime.date(2025, 6, 5),
            'start_time': datetime.time(19, 0),
            'end_time': datetime.time(23, 0),
            'location': 'Ресторан La Riviera',
            'price': Decimal('300.00'),
            'is_free': False,
        },
    ]
    
    for event_data in events:
        event, created = Event.objects.get_or_create(
            title=event_data['title'],
            defaults={
                'description': event_data['description'],
                'start_date': event_data['start_date'],
                'end_date': event_data['end_date'],
                'start_time': event_data['start_time'],
                'end_time': event_data['end_time'],
                'location': event_data['location'],
                'price': event_data['price'],
                'is_free': event_data['is_free'],
            }
        )
        if created:
            print(f"Створено подію: {event.title}")
        else:
            print(f"Подія вже існує: {event.title}")

def create_promotions():
    """Створення акцій"""
    promotions = [
        {
            'title': 'Щасливі години',
            'description': 'Знижка 20% на всі напої з 17:00 до 19:00 з понеділка по четвер.',
            'start_date': datetime.date(2025, 5, 1),
            'end_date': datetime.date(2025, 6, 30),
            'is_active': True,
            'discount_percent': 20,
        },
        {
            'title': 'Сімейна неділя',
            'description': 'Знижка 15% на все меню для сімей з дітьми щонеділі.',
            'start_date': datetime.date(2025, 5, 1),
            'end_date': datetime.date(2025, 6, 30),
            'is_active': True,
            'discount_percent': 15,
        },
        {
            'title': 'День народження',
            'description': 'Знижка 30% на все меню в день вашого народження (при пред\'явленні документу).',
            'start_date': datetime.date(2025, 5, 1),
            'end_date': datetime.date(2025, 12, 31),
            'is_active': True,
            'discount_percent': 30,
        },
    ]
    
    for promo_data in promotions:
        promo, created = Promotion.objects.get_or_create(
            title=promo_data['title'],
            defaults={
                'description': promo_data['description'],
                'start_date': promo_data['start_date'],
                'end_date': promo_data['end_date'],
                'is_active': promo_data['is_active'],
                'discount_percent': promo_data['discount_percent'],
            }
        )
        if created:
            print(f"Створено акцію: {promo.title}")
        else:
            print(f"Акція вже існує: {promo.title}")

def create_team_members():
    """Створення команди ресторану"""
    team_members = [
        {
            'name': 'Олександр Петренко',
            'position': 'Шеф-кухар',
            'bio': 'Олександр має більше 15 років досвіду роботи в кращих ресторанах Європи. Він спеціалізується на середземноморській кухні та постійно вдосконалює своє мистецтво.',
            'is_active': True,
            'order': 1,
        },
        {
            'name': 'Марія Коваленко',
            'position': 'Шеф-кондитер',
            'bio': 'Марія - талановитий кондитер з досвідом роботи в Парижі. Її десерти - справжні витвори мистецтва, які не залишать байдужими навіть найвибагливіших гурманів.',
            'is_active': True,
            'order': 2,
        },
        {
            'name': 'Ігор Савченко',
            'position': 'Сомельє',
            'bio': 'Ігор - сертифікований сомельє з багаторічним досвідом. Він допоможе вам обрати ідеальне вино до вашої страви та розповість про особливості кожного сорту.',
            'is_active': True,
            'order': 3,
        },
        {
            'name': 'Наталія Іванова',
            'position': 'Менеджер ресторану',
            'bio': 'Наталія відповідає за бездоганний сервіс та комфорт наших гостей. Вона завжди готова допомогти з організацією вашого візиту та зробити його незабутнім.',
            'is_active': True,
            'order': 4,
        },
    ]
    
    for member_data in team_members:
        member, created = TeamMember.objects.get_or_create(
            name=member_data['name'],
            defaults={
                'position': member_data['position'],
                'bio': member_data['bio'],
                'is_active': member_data['is_active'],
                'order': member_data['order'],
            }
        )
        if created:
            print(f"Створено члена команди: {member.name}")
        else:
            print(f"Член команди вже існує: {member.name}")

def create_testimonials():
    """Створення відгуків"""
    testimonials = [
        {
            'name': 'Олена Мельник',
            'text': 'Неймовірний ресторан з чудовою атмосферою та смачними стравами. Особливо сподобалось різотто з грибами та тірамісу. Обов\'язково повернемось!',
            'rating': 5,
            'is_active': True,
        },
        {
            'name': 'Андрій Ковальчук',
            'text': 'Святкували річницю весілля в La Riviera. Все було на вищому рівні - від обслуговування до якості страв. Дякуємо за незабутній вечір!',
            'rating': 5,
            'is_active': True,
        },
        {
            'name': 'Марина Шевченко',
            'text': 'Відвідали ресторан під час відпустки в Ковелі. Чудовий сервіс, вишукані страви та приємна атмосфера. Філе міньйон просто тане в роті!',
            'rating': 4,
            'is_active': True,
        },
        {
            'name': 'Віктор Лисенко',
            'text': 'Проводили корпоратив в La Riviera. Все було організовано на найвищому рівні. Особлива подяка шеф-кухарю за неймовірні страви та персоналу за уважність до деталей.',
            'rating': 5,
            'is_active': True,
        },
    ]
    
    for testimonial_data in testimonials:
        testimonial, created = Testimonial.objects.get_or_create(
            name=testimonial_data['name'],
            defaults={
                'text': testimonial_data['text'],
                'rating': testimonial_data['rating'],
                'is_active': testimonial_data['is_active'],
            }
        )
        if created:
            print(f"Створено відгук від: {testimonial.name}")
        else:
            print(f"Відгук вже існує від: {testimonial.name}")

def main():
    """Головна функція для заповнення бази даних"""
    print("Заповнення бази даних тестовими даними...")
    
    print("\nСтворення категорій...")
    categories = create_categories()
    
    print("\nСтворення страв...")
    create_dishes(categories)
    
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
