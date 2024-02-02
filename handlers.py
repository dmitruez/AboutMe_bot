from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from repository import RepoJSON
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from services import ServiceBot
from entities import User
from states import States

service = ServiceBot()
repo = RepoJSON()
router = Router()
buttons = repo.buttons()

@router.message(Command("start"))
async def greetings(message: Message):
	lang = message.from_user.language_code
	button = buttons.show_information
	if lang == 'ru':
		text = button.ru
	else:
		text = button.en
	call_data = button.call_data
	
	button = [[InlineKeyboardButton(text=text, callback_data=call_data)]]
	user = User(
		message.from_user.first_name, message.from_user.username, message.from_user.id, message.from_user.language_code
		)
	service.save_to_json(user)
	markup = InlineKeyboardMarkup(inline_keyboard=button)
	await message.answer(repo.fist_greetings(lang), reply_markup=markup)

@router.callback_query(F.data == 'info')
async def starting_info(clbck: CallbackQuery, state: FSMContext, page=0):
	lang = clbck.from_user.language_code
	button_next = buttons.next_fact
	button_question = buttons.question_to_me
	button_back = buttons.previous_fact
	
	facts = repo.information(lang)
	pages_count = len(facts) - 1
	
	
	left = page - 1 if page != 0 else pages_count
	right = page + 1 if page != pages_count else 0
	
	if lang == 'ru':
		
		but = [[
			InlineKeyboardButton(text=button_back.ru, callback_data=button_back.call_data + str(left)),
			InlineKeyboardButton(text=button_next.ru, callback_data=button_next.call_data + str(right))],
			[InlineKeyboardButton(text=button_question.ru, callback_data=button_question.call_data)]]
	else:
		but = [[
			InlineKeyboardButton(text=button_back.en, callback_data=button_back.call_data + str(left)),
			InlineKeyboardButton(text=button_next.en, callback_data=button_next.call_data + str(right))],
			[InlineKeyboardButton(text=button_question.en, callback_data=button_question.call_data)]]
	markup = InlineKeyboardMarkup(inline_keyboard=but, row_widht=1)
	
	await clbck.message.edit_text(text=facts[page], reply_markup=markup)
	await clbck.answer()


@router.callback_query(lambda m: m.data)
async def next_fact(clbck: CallbackQuery, state: FSMContext):
	lang = clbck.from_user.language_code
	text_quest = repo.text_question(lang)
	if str(clbck.data).startswith('to '):
		page = int(str(clbck.data).split(' ')[1])
		await starting_info(clbck, state, page=page)
		
	elif clbck.data == 'question':
		await state.set_state(States.send_message_to_me)
		await clbck.message.answer(text=text_quest)
		
	elif clbck.data == 'reply':
		await state.set_state(States.reply_message)
		await clbck.message.bot.send_message(2048360747, 'Отправьте ответ пользователю')
		
		
@router.message(States.send_message_to_me)
async def send_to_me(message: Message):
	username = message.from_user.first_name
	url = message.from_user.url
	lang = message.from_user.language_code
	button_reply = buttons.reply_to_message
	question = message.text
	if lang == 'ru':
		text = button_reply.ru
	else:
		text = button_reply.en
		
	call_data = button_reply.call_data
	button = [[InlineKeyboardButton(text=text, callback_data=call_data)]]
	keyboard = InlineKeyboardMarkup(inline_keyboard=button)
	await message.bot.send_message(2048360747, text=
													f'<b>Пользователь:</b>  <a href="{url}">{username}</a>\n'
	                                                f'<b>Язык:</b>  {lang}\n'
	                                                f'<b>Вопрос:</b>  {question}', reply_markup=keyboard)


@router.message(States.reply_message)
async def reply_message(message: Message):
	lang = message.from_user.language_code
	question, answer = message.text.split(': ')
	if lang == 'ru':
		await message.answer(text=f'<b>Вопрос:</b> {question}\n\n<b>Ответ:</b> {answer}')
	else:
		await message.answer(text=f'<b>Question:</b> {question}\n\n<b>Answer:</b> {answer}')