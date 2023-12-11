import telebot
import requests
API_KEY = f'e7bebe47e79b01e4a2942213213e02ed'
lang = 'ru'
token = f'6960607637:AAH6i3WKC0B3YY4QhqsHjdoTEzzcm-j7utk'
bot = telebot.TeleBot(token)

def kelvin_to_celsius(temp_k):#создаем функцию, которая будет преобразовывать градусы кельвина в градусы цельсия
    temp_c = temp_k - 273.15
    return round(temp_c, 1)

@bot.message_handler(commands=['start']) #пишем функцию, которая вызывается после команды start
def start_message(message): #данная функция нужна для того, чтобы поприветствовать пользователя
    msg = bot.reply_to(message, 'Hello! I am weather bot!')
    bot.send_message(message.chat.id, f'Input name of city if you wanna continie!')
    bot.register_next_step_handler(msg, print_weather)

@bot.message_handler(content_types=['text']) #пишем функцию, которая выводит погоду в конкретном городе
def print_weather(message):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&lang={lang}&appid={API_KEY}'
    weather = requests.get(url).json()
    weather_info = f'Weather in {message.text}\n\n'
    for key, value in weather['main'].items():
        if key == 'temp':
            key = 'Температура воздуха: '
            value = kelvin_to_celsius(value)
        if key == 'feels_like':
            key = 'Ощущается как: '
            value = kelvin_to_celsius(value)
        if key == 'temp_min':
            key = 'Минимальная температура: '
            value = kelvin_to_celsius(value)
        if key == 'temp_max':
            key = 'Максимальная температура: '
            value = kelvin_to_celsius(value)
        if key == 'pressure':
            key = 'Давление: '
        if key == 'humidity':
            key = 'Влажность воздуха: '
        weather_info += f'{key} {value}\n'
    bot.send_message(message.chat.id, weather_info)
bot.polling(none_stop=True)