from django.shortcuts import render, redirect
from .models import Product
from .forms import Autorisation, UserRegistrationForm, Check_code, New_password
from django.contrib.auth.models import User
import random
import string
from django.core.mail import send_mail
from django.conf import settings

def product_list(request): #функция для отображения списка продуктов
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def not_succes(request):
    return render(request, 'not_succes.html')

def enter(request):
    if request.method == 'POST':
        form = Autorisation(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username, email=email, password=password).exists():
                request.session['_username_'] = username
                request.session['_email_'] = email
                return redirect('user_cabinet_enter') #Пользователь существует, пароль верный
            else:
                return redirect('not_succes') #Пользователь не существует или неверный пароль
    else:
        form = Autorisation()
    return render(request, 'Enter.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid() and 'myCheckbox' in request.POST: #проверяем, присутствует ли myCheckbox в данных формы, доступных через request.POST
            if request.POST['myCheckbox'] == 'on': #Проверяем, нажата ли галочка
                request.session['username'] = form.cleaned_data['username'] #сохраняем в сессию данные, полученные из формы
                request.session['email'] = form.cleaned_data['email']
                request.session['password'] = form.cleaned_data['password']
                return redirect('enter_email')
    else:
        form = UserRegistrationForm()
    return render(request, 'for_register.html', {'form': form})

def agree_with_rules(request): #функция для отображения правил, если пользователю интересны наши правила
    return render(request, 'Правила.html')

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
        user = User(username=username, email=email, password=password) #сохранием данные, введенные в форму ранее
        user.save()
        request.session['username_for_show'] = username
        request.session['email_for_show'] = email
        return redirect('user_cabinet_register')
    else:
        return render(request, 'if_code_right.html')

def user_cabinet_register(request):
    username = request.session.get('username_for_show')
    email = request.session.get('email_for_show')
    user = User.objects.get(username=username, email=email)
    return render(request, 'Личный кабинет пользователя.html', {'user': user})

def check_confirmation_code(request):
    if request.method == 'POST':
        form = Check_code(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['entered_code'] #получаем данные из формы
            sent_code = request.session.get('confirmation_code') #получаем данные из сессии
            if entered_code == sent_code: #проверяем, правильно ли введен код, отправленный на почту пользователю
                return redirect('right_code') #если код верный, то перекидываем пользователя на соответствующую страницу
            else:
                return redirect('not_right_code') #в ином случае на страницу, где говорится, что код неверный
    else:
        form = Check_code()
    return render(request, 'enter_code.html', {'form': form})

def print_products(request):
    return render(request, 'Shop.html')

def user_cabinet_enter(request):
    username = request.session.get('_username_')
    email = request.session.get('_email_')
    user = User.objects.get(username=username, email=email)
    return render(request, 'Личный кабинет пользователя при входе на сервер.html', {'user': user})

def create_new_password(request): #пишем функцию, которая создает новый пароль
    if request.method == 'POST':
        form = New_password(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            new_password = form.cleaned_data['enter_new_password']
            user = User.objects.get(username=username, email=email)
            user.password = new_password
            user.save()
            return redirect('password_created')
    else:
        form = New_password()
    return render(request, 'Восстановление пароля.html', {'form': form})

def password_created(request): # сообщаем пользователю о том, что пароль изменен
    return render(request, 'Пароль успешно изменен.html')

def show_products_for_buy(request):
    product_data = Product.objects.all()
    return render(request, 'Shop.html', {'product_data': product_data})