from aiogram.fsm.state import State
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from repository import RepoJSON
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from services import ServiceBot
from entities import User


service = ServiceBot()
repo = RepoJSON()
router = Router()
send_message_to_me = State()

@router.message(Command("start"))
async def greetings(message: Message):
	lang = message.from_user.language_code
	call_data, text = repo.button_info('show_information', lang)
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
	facts = repo.information(lang)
	pages_count = len(facts) - 1
	
	call_data_next, text_next = repo.button_info('next_fact', lang)
	call_data_question, text_question = repo.button_info('question_to_me', lang)
	call_data_back, text_back = repo.button_info('previous_fact', lang)
	
	left = page - 1 if page != 0 else pages_count
	right = page + 1 if page != pages_count else 0
	
	buttons = [[
		InlineKeyboardButton(text=text_back, callback_data=call_data_back + str(left)),
		InlineKeyboardButton(text=text_next, callback_data=call_data_next + str(right))
		], [InlineKeyboardButton(text=text_question, callback_data=call_data_question)]]
	markup = InlineKeyboardMarkup(inline_keyboard=buttons, row_widht=1)
	
	await clbck.message.edit_text(text=facts[page], reply_markup=markup)
	await clbck.answer()


@router.callback_query(lambda m: m.data)
async def next_fact(clbck: CallbackQuery, state: FSMContext):
	lang = clbck.from_user.language_code
	text_quest = repo.text_question(lang)
	if str(clbck.data).startswith('to '):
		
		page = int(str(clbck.data).split(' ')[1])
		
		await starting_info(clbck, state, page=page)
	else:
		await state.set_state(send_message_to_me)
		await clbck.message.answer(text=text_quest)
		
		
@router.message(send_message_to_me)
async def send_to_me(message: Message):
	username = message.from_user.first_name
	url = message.from_user.url
	lang = message.from_user.language_code
	question = message.text
	
	call_data_reply, text_reply = repo.button_info("reply_to_message", lang)
	button = [[InlineKeyboardButton(text=text_reply, callback_data=call_data_reply)]]
	keyboard = InlineKeyboardMarkup(inline_keyboard=button)
	await message.bot.send_message(2048360747, text=
													f'<b>Пользователь:</b>  <a href="{url}">{username}</a>\n'
	                                                f'<b>Язык:</b>  {lang}\n'
	                                                f'<b>Вопрос:</b>  {question}', reply_markup=keyboard)
	