import json
from entities import Button, ButtonsGroup, BotText, BotTextGroup, User


class RepoJSON:
	FILE = 'config.json'
	
	
	def buttons(self) -> ButtonsGroup:
		buttons_list = []
		with open(self.FILE, 'r', encoding='utf-8') as f:
			data = json.load(f)['buttons']
			for button in data:
				a = Button(
					name=button,
					ru=data[button]['ru'],
					en=data[button]['en'],
					call_data=data[button]['call_data']
					)
				
				buttons_list.append(a)
			
			buttons = ButtonsGroup(buttons_list)
			
		return buttons
	
	
	def information(self, lang: str) -> list:
		with open(self.FILE, 'r', encoding='utf-8') as f:
			data = json.load(f)['information']
			if lang == 'ru':
				info = data['ru']
			
			else:
				info = data['en']
		
		return info
	
	
	def about_bot(self) -> BotTextGroup:
		bot_info = []
		with open(self.FILE, 'r', encoding='utf-8') as f:
			data = json.load(f)['about_bot']
			for option in data['bot_text']:
				a = BotText(
					name=option,
					ru=data['bot_text'][option]['ru'],
					en=data['bot_text'][option]['en']
					)
				bot_info.append(a)
				
			bot = BotTextGroup(bot_info)
			
		return bot
	
	
	def token(self):
		with open(self.FILE, 'r', encoding='utf-8') as f:
			token = json.load(f)['about_bot']['TOKEN']
		
		return token
	

repo = RepoJSON()