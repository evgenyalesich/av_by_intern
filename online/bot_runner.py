import telebot
import db_connector

bot = telebot.TeleBot("6804030085:AAEODu2L_L1F2tXf0EAHLodG4YXFB9rXqX8")


# 1. Проверка, есть ли в базе / Проверка блокировки/разблокировки
def register_if_not_exist(message):
	pass


# 2. Сохранять обращения пользователей в БД
def save_message(message):
	pass


# 3. Отправить пользователю ответ полученный из Джанго Админки
def sent_answer(id, to_sent_data):
	bot.send_message(id, to_sent_data)


# 4. Отправить всем пользователям ответ сообщение из рассылки
@bot.message_handler(commands=['sent_all'])
def sent_all(message):
	users = db_connector.get_all_not_blocked_users()
	for id in users:
		bot.send_message(id, 'Приветульки')


# def print_info(message):
# 	print(
# 	f"""
# 	id: {message.from_user.id}
# 	name: {message.from_user.first_name}
# 	fullname: {message.from_user.full_name}
# 	"""
# 	)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	register_if_not_exist(message)
	save_message(message)
	bot.reply_to(message, 'Ваш вопрос стоит в очереди на ответ')


bot.infinity_polling()
