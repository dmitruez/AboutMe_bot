import json
from entities import Button, User, GroupButtons


class RepoJSON:
	FILE = 'config.json'
	
	
	def buttons(self) -> GroupButtons:
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
			
			buttons = GroupButtons(buttons_list)
			
		return buttons
	
	
	def information(self, lang: str) -> list:
		with open(self.FILE, 'r', encoding='utf-8') as f:
			data = json.load(f)['information']
			if lang == 'ru':
				info = data['ru']
			
			else:
				info = data['en']
		
		return info
	
	
	def token(self):
		with open(self.FILE, 'r', encoding='utf-8') as f:
			token = json.load(f)['about_bot']['TOKEN']
		
		return token
	
	
	def fist_greetings(self, lang):
		with open(self.FILE, 'r', encoding='utf-8') as f:
			data = json.load(f)['about_bot']['greetings']
			if lang == 'ru':
				greetings = data['ru']
			
			else:
				greetings = data['en']
		
		return greetings
	
	
	def text_question(self, lang):
		with open(self.FILE, 'r', encoding='utf-8') as f:
			data = json.load(f)['about_bot']['text_question']
			if lang == 'ru':
				question = data['ru']
			
			else:
				question = data['en']
		
		return question

repo = RepoJSON()