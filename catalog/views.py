from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    """Контроллер главной страницы"""
    products = Product.objects.all().order_by('-created_at')

    context = {
        'products': products,
        'title': 'Каталог товаров',
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Контроллер страницы контактов"""
    context = {'title': 'Контакты'}
    return render(request, 'catalog/contacts.html', context)


def product_detail(request, pk):
    """Контроллер страницы одного товара"""
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'title': product.name,
    }
    return render(request, 'catalog/product_detail.html', context)