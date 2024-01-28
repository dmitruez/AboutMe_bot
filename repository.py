import json


class RepoJSON:
	FILE = 'config.json'
	
	def button(self, call_data):
		with open(self.FILE, 'r', encoding='utf-8') as f:
			button = json.load(f)['buttons'][call_data]
			
			return call_data, button

