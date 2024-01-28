import json


languages = {
	"rus": 0,
	"eng": 1
	}

class RepoJSON:
	FILE = 'config.json'
	
	
	def button(self, call_data: str, lang: str) -> tuple:
		"""
		
		:param call_data: The call_data in the json file
		:param lang: The language of the button name
		:return: returns also call_data and button name
		
		"""
		
		with open(self.FILE, 'r', encoding='utf-8') as f:
			button = json.load(f)['buttons'][call_data][languages[lang]]
			
			return call_data, button
	
	
	def information(self, lang: str) -> list:
		"""
		
		:param lang: The language of information
		:return: Information about me
		
		"""
		
		with open(self.FILE, 'r', encoding='utf-8') as f:
			info_ = json.load(f)['information']
			info = list(map(lambda m: m[languages[lang]], info_))
			return info