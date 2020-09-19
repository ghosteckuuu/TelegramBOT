import telebot
bot = telebot.TeleBot("1386775530:AAFBOBJm8HhZq5EcsfyewP8IYWEhijc7jJU")
@bot.message_handler(content_types=["text"])
def handle_text_messages(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет")
	elif message.text == "Кто ты ?":
		bot.send_message(message.from_user.id, "Я чат-бот,который используется в качестве теста")
	elif message.text == "Как тебя зовут?":
		bot.send_message(message.from_user.id, "Меня зовут Аркаша")
	elif message.text == "Что ты умеешь?":
		bot.send_message(message.from_user.id, "Пока что я мало чего умею")
	else:
		bot.send_message(message.from_user.id, "Прости,но пока что список моих ответов не такой обширный,поэтому я не понимаю тебя и к сожалению не могу ответить")
bot.polling(none_stop=True, interval = 0)