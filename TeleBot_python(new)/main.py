import telebot
from config import keys, TOKEN
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Привет. Для конвертация воспользуйся командой --> /values\
*********************************\
\n Записывай данные в формате:\
\n \n <имя исходной валюты> <имя конвертируемой валюты> <сумма конвертируемой валюты через точку>'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n USD \n RUB \n EUR'
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Неподходящее количество параметров. Обрати внимание на инструкцию: /help.')
        quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Думаю, что здесь есть ошибка.\n{e}')
    except Exception as e:
        bot.reply_to(message, f"Не могу обработать команду:( \n{e}")
    else:
        total_base_result = round(float(total_base) * float(amount),2)
        text = f'Цена денежной единицы {keys[quote]} в {keys[base]} - {total_base}. Результат конвертации - {total_base_result}'
        bot.send_message(message.chat.id, text)

bot.polling(non_stop=True)