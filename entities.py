from dataclasses import dataclass
import json

@dataclass
class User:
	name: str
	username: str
	id: int
	language_code: str

