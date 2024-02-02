from dataclasses import dataclass
import json

@dataclass
class User:
	name: str
	username: str
	id: int
	language_code: str


@dataclass
class Button:
	name: str
	ru: str
	en: str
	call_data: str


class GroupButtons:
	show_information = None
	question_to_me = None
	next_fact = None
	previous_fact = None
	reply_to_message = None
	
	def __init__(self, buttons: list[Button]):
		for button in buttons:
			if button.name == 'show_information':
				self.show_information = button
			elif button.name == 'question_to_me':
				self.question_to_me = button
			elif button.name == 'next_fact':
				self.next_fact = button
			elif button.name == 'previous_fact':
				self.previous_fact = button
			elif button.name == 'reply_to_message':
				self.reply_to_message = button
			else:
				pass