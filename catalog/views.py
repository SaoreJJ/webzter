from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    """Контроллер главной страницы"""
    return render(request, 'catalog/home.html')


def contacts(request):
    """Контроллер страницы контактов"""
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # В реальном проекте здесь должна быть обработка формы
        # и отправка email

        # Выводим сообщение об успешной отправке
        messages.success(request, 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.')

        return redirect('contacts')

    return render(request, 'catalog/contacts.html')