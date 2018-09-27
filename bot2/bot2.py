# Импорт компонент
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


logging.basicConfig(
	format='%(asctime)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log'
	)


def greet_user(bot, update):
	# Кракозябры вместо русского текста
    # text = 'Вызван /start'
    text ='Add: /start'
    # Вывод в коонсоль
    # print(text)
    # Вывод в лог
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
	user_text = "Hello: {}! Received: {}".format(
		update.message.chat.first_name,
		update.message.text)
	# Вывод в консоль
	# print(update.message)
	# Вывод в лог
	logging.info("User: %s, Chad ID: %s, Message: %s",
		update.message.chat.username,
		update.message.chat.id,
		update.message.text)
	update.message.reply_text(user_text)


def main():
	mybot = Updater("501304893:AAEB4vN6wnsMJ4xOs0MpsU2zCe3gYT9dCV8", request_kwargs=PROXY)

	# logging.info('Бот запускается')
	logging.info('BotStart')

	# Реакция на события
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	mybot.start_polling()
	mybot.idle()


main()
