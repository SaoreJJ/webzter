from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Category, Contact


def home(request):
    """Контроллер главной страницы"""
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(f"- {product.name}: {product.price} руб.")

    context = {
        'latest_products': latest_products,
    }
    return render(request, 'catalog/home.html', context)


# ДОБАВИТЬ ЭТУ ФУНКЦИЮ
def contacts(request):
    """Контроллер страницы контактов"""
    contacts_list = Contact.objects.all().order_by('-created_at')

    context = {
        'contacts': contacts_list,
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)