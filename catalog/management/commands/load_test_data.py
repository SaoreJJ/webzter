from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные (удаляет старые)'

    def handle(self, *args, **options):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write('Старые данные удалены')

        # Создаем категории
        cat1 = Category.objects.create(
            name="Электроника",
            description="Электронные устройства"
        )
        cat2 = Category.objects.create(
            name="Книги",
            description="Литература"
        )
        cat3 = Category.objects.create(
            name="Одежда",
            description="Одежда и аксессуары"
        )

        # Создаем продукты
        Product.objects.create(
            name="Смартфон",
            description="Мощный смартфон",
            category=cat1,
            price=29999.99
        )
        Product.objects.create(
            name="Ноутбук",
            description="Игровой ноутбук",
            category=cat1,
            price=89999.99
        )
        Product.objects.create(
            name="Футболка",
            description="Хлопковая футболка",
            category=cat3,
            price=1999.99
        )

        self.stdout.write(self.style.SUCCESS(
            f'Создано: {Category.objects.count()} категорий, '
            f'{Product.objects.count()} продуктов'
        ))