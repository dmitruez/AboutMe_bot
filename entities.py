from dataclasses import dataclass


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


class ButtonsGroup:

	def __init__(self, buttons: list[Button]):
		for button in buttons:
			list(self.__dir__()).append(button.name)
			self.__setattr__(button.name, button)
			


@dataclass()
class BotText:
	name: str
	ru: str
	en: str

class BotTextGroup:
	
	def __init__(self, bot_info: list[BotText]):
		for text in bot_info:
			list(self.__dir__()).append(text.name)
			self.__setattr__(text.name, text)
