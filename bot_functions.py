import telebot
from repository import RepoJSON
from telebot import types


repo = RepoJSON()
TOKEN = repo.token()

bot = telebot.TeleBot(TOKEN, parse_mode='html')


@bot.message_handler(commands=['start'])
def greetings(message):
	lang = message.from_user.language_code
	
	call_data, text = repo.button_info('question_to_me', lang)
	button = types.InlineKeyboardButton(text=text, callback_data=call_data)
	markup = types.InlineKeyboardMarkup()
	markup.add(button)
	
	bot.send_message(message.from_user.id, text=repo.fist_greetings(lang), reply_markup=markup)
	

bot.infinity_polling()

