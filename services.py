import json
from entities import User
class ServiceBot:
	USERS_FILE = 'users.json'
	def save_to_json(self, user: User):
		client = {}
		
		with open(self.USERS_FILE, 'r', encoding="utf-8") as fp:
			data = json.load(fp)
			client["name"] = user.name
			client["username"] = user.username
			client['language_code'] = user.language_code
			data["users"][user.username] = client
			
		with open(self.USERS_FILE, "w", encoding="utf-8") as outfile:
			json.dump(data, outfile, indent=5, ensure_ascii=False)
		