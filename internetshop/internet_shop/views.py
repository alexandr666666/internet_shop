from django.shortcuts import render, redirect
from .models import Product, Account
from django.http import *
from .forms import Autorisation, UserRegistrationForm, Check_code
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
import random
import string
from django.core.mail import send_mail
from django.conf import settings
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def not_succes(request):
    return render(request, 'not_succes.html')

def enter(request):
    if request.method == 'POST':
        form = Autorisation(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] #получаем данные из формы
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, email=email, password=password)
            if user is not None:
                # Пароль верный, пользователь существует
                return redirect('product_list')
            else:
                # Пользователь не существует или пароль неверный
                return render(request, 'not_succes.html')
    else:
        form = Autorisation()
    return render(request, 'Enter.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'for_register.html')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = UserRegistrationForm()
    return render(request, 'for_register.html', {'form': form})

def generate_random_code():
    code_length = 6  # длина кода
    characters = string.ascii_letters + string.digits  #числа и буквы, из которых будет состоять код
    random_code = ''.join(random.choices(characters, k=code_length))  #выбераем рандомные символы
    return random_code

def send_random_code_email(user_email, code):
    send_mail(
        'Ваш код для подтверждения',
        f'Ваш код для проверки: {code}',
        settings.EMAIL_HOST_USER,  # Адрес отправителя, который определен в настройках Django
        [user_email],  # Электронная почта пользователя
        fail_silently=False,
    )

def send_and_verify_code(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')  # Получаем адрес электронной почты из формы
        random_code = generate_random_code()  # Генерируем случайный код
        send_random_code_email(user_email, random_code)  # Отправляем код на почту
        #Здесь вы также сохраняете random_code в сессии или в базе данных для последующей проверки
        request.session['confirmation_code'] = random_code
        return render(request, 'enter_code.html')
    else:
        return render(request, 'enter_email.html')

def check_confirmation_code(request):
    if request.method == 'POST':
        entered_code = request.POST.get('entered_code')
        expected_code = request.session.get('confirmation_code')
        if entered_code == expected_code:
            # Код верный
            return redirect('product_list')
        else:
            # Код неверный
            return redirect('not_succes')
    return render(request, 'enter_code.html')









