from django.shortcuts import render, redirect
from .models import Product
from .forms import Autorisation, UserRegistrationForm, Check_code
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def product_list(request): #функция для отображения списка продуктов
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
            request.session['username'] = form.cleaned_data['username'] #сохраняем данные в сессию
            request.session['email'] = form.cleaned_data['email']
            request.session['password'] = form.cleaned_data['password']
            return redirect('enter_email')
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
        'Ваш код для подтверждения', #Название сообщения
        f'Ваш код для проверки: {code}', #Текст сообщения
        settings.EMAIL_HOST_USER,  # Адрес отправителя, который определен в настройках Django
        [user_email],  # Электронная почта пользователя
        fail_silently=False,
    )

def send_and_verify_code(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')  # Получаем адрес электронной почты из формы
        random_code = generate_random_code()  # Генерируем случайный код
        send_random_code_email(user_email, random_code)  # Отправляем код на почту
        request.session['confirmation_code'] = random_code # Сохраняем рандомный код в сессии
        return redirect('enter_code')
    else:
        return render(request, 'enter_email.html')

def not_right_code(request):
    return render(request, 'if_not_right_code.html')

def right_code(request):
    if request.method == 'POST':
        username = request.session.get('username') #получаем данные из сессии
        email = request.session.get('email')
        password = request.session.get('password')
        user = User(username=username, email=email, password=password) #сохранием данные, введенные в форму
        user.save()
        return redirect('user_cabinet')
    else:
        return render(request, 'if_code_right.html')

def user_cabinet(request):
    user = User.objects.all()
    return render(request, 'Личный кабинет пользователя.html', {'user': user})

def check_confirmation_code(request):
    if request.method == 'POST':
        form = Check_code(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['entered_code'] #получаем данные из формы
            sent_code = request.session.get('confirmation_code') #получаем данные из сессии
            form.save()
            if entered_code == sent_code: #проверяем, правильно ли введен код, отправленный на почту пользователю
                return redirect('right_code') #если код верный, то перекидываем пользователя на соответствующую страницу
            else:
                return redirect('not_right_code') #в ином случае на страницу, где говорится, что код неверный
    else:
        form = Check_code()
    return render(request, 'enter_code.html', {'form': form})












