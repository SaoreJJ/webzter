# 1. Импорт моделей
from catalog.models import Category, Product

# 2. Создание категорий
category1 = Category.objects.create(name="Электроника", description="Электронные устройства")
category2 = Category.objects.create(name="Книги", description="Литература различных жанров")
category3 = Category.objects.create(name="Одежда", description="Мужская и женская одежда")

# 3. Создание продуктов
product1 = Product.objects.create(
    name="Смартфон",
    description="Мощный смартфон с большим экраном",
    category=category1,
    price=29999.99
)

product2 = Product.objects.create(
    name="Ноутбук",
    description="Игровой ноутбук",
    category=category1,
    price=89999.99
)

product3 = Product.objects.create(
    name="Футболка",
    description="Хлопковая футболка",
    category=category3,
    price=1999.99
)

# 4. Получение всех категорий
all_categories = Category.objects.all()
print("Все категории:", list(all_categories))

# 5. Получение всех продуктов
all_products = Product.objects.all()
print("Все продукты:", list(all_products))

# 6. Найти все продукты в определенной категории
electronics_products = Product.objects.filter(category=category1)
print("Продукты в категории 'Электроника':", list(electronics_products))

# 7. Обновить цену для определенного продукта
product1.price = 27999.99
product1.save()
print(f"Обновленная цена {product1.name}: {product1.price}")

# 8. Удалить продукт
# product3.delete()
# print("Продукт удален")