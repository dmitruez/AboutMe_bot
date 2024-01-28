import json


class RepoJSON:
	FILE = 'config.json'
	
	
	def button(self, name: str, lang: str) -> tuple:
		if lang == 'ru':
			with open(self.FILE, 'r', encoding='utf-8') as f:
				button = json.load(f)['buttons'][name]['ru']
				call_data = json.load(f)['buttons'][name]['call_data']
		
		else:
			with open(self.FILE, 'r', encoding='utf-8') as f:
				button = json.load(f)['buttons'][name]['en']
				call_data = json.load(f)['buttons'][name]['call_data']
		
		return call_data, button
	
	
	def information(self, lang: str) -> list:
		if lang == 'ru':
			with open(self.FILE, 'r', encoding='utf-8') as f:
				info = json.load(f)['information']['ru']
		
		else:
			with open(self.FILE, 'r', encoding='utf-8') as f:
				info = json.load(f)['information']['en']
		
		return info
	
	
	def token(self):
		with open(self.FILE, 'r', encoding='utf-8') as f:
			token = json.load(f)['about_bot']['TOKEN']
		
		return token
	
	
	def fist_greetings(self, lang):
		if lang == 'ru':
			with open(self.FILE, 'r', encoding='utf-8') as f:
				greetings = json.load(f)['about_bot']['greetings']['ru']
		
		else:
			with open(self.FILE, 'r', encoding='utf-8') as f:
				greetings = json.load(f)['about_bot']['greetings']['en']
		
		return greetings