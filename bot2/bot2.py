# Импорт компонент
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


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
	mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

	# logging.info('Бот запускается')
	logging.info('BotStart')

	# Реакция на события
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	mybot.start_polling()
	mybot.idle()


main()
