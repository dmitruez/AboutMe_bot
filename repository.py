import json


class RepoJSON:
	FILE = 'config.json'
	
	
	def button_info(self, name: str, lang: str) -> tuple or str:
		with open(self.FILE, 'r', encoding='utf-8') as f:
			data = json.load(f)['buttons'][name]
			if lang == 'ru':
				text = data['ru']
				call_data = data['call_data']
	
			else:
				text = data['en']
				call_data = data['call_data']
		
		return call_data, text
		
	
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

# print(repo.button_info('question_to_me', 'ru'))
# print(repo.information('ru'))
# print(repo.fist_greetings('ru'))
# print(repo.token())