import datetime, ephem, logging, settings
from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import planet_lists


# настройка логов бота
logging.basicConfig(filename='bot.log', 
                                    format='[%(asctime)s] [%(levelname)s] => %(message)s',
                                    datefmt='%Y-%m-%d %H:%M:%S', 
                                    level=logging.INFO)

# НЕ РАБОТАЕТ с включенной proxy !!!
# Настройки прокси. 
# PROXY = {'proxy_url': settings.PROXY_URL,
#                 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}
#request_kwargs=PROXY


def greet_user(update, context):
    # update - то, что мы получили от телеграма на команду start
    # context - с помощью нее можем отдавать команды боту. Может понадобиться если мы хотим отправить сообщение другому юзеру

    print('Вызван /start')
    update.message.reply_text('Привет! Хочешь узнать чуть больше про планеты?' 
                                                'Введи команду  /planet и название на английском')


def talk_to_me(update, context):
    text = update.message.text
    if  'planet' not in text:
        print(text)
        update.message.reply_text(text)


def planet_info(update, context):
    user_text = update.message.text
    user_planet = user_text.split(' ')[1]
    user_planet.lower()
    user_planet.capitalize()

    if bool(user_planet not in planet_lists.planet_names):
        update.message.reply_text('Извини! Я не знаю такую планету. Попробуй еще раз')
    else:
        # получаем местоположение планеты
        today_date = datetime.datetime.now().strftime('%Y/%m/%d')
        planet_class = getattr(ephem, user_planet)
        planet_today = planet_class(today_date)
        find_const = ephem.constellation(planet_today)
        const_name = find_const[1]
        where_planet = planet_lists.constellation_dict[const_name]
        update.message.reply_text(f'Сегодня {user_planet} находится в Созвездии {where_planet}'
                                                        'Понравилось? Попробуй еще')


def main():
    mybot = Updater(settings.APY_KEY, use_context=True)

    # активируем команду старт
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')

    mybot.start_polling()
    mybot.idle()        # запускаем бота (он будет работать, пока его не остановим)


if __name__ == '__main__':
    main()