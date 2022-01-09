import requests
import json
import os


class SupaBase:
	def __init__(self):
		self.api_key = os.environ['supabase_api_key']
		self.url = os.environ['supabase_url']

		
		print("#M database | Database initiated")

	def read_table(self, table):
		SUPABASE_HEADERS = {
			'apikey': self.api_key,
			'Authorization': 'Bearer' + self.api_key}
		response = requests.get(f'{self.url}/{table}', headers=SUPABASE_HEADERS)
		res = json.loads(response.text)
		return res
		

	def add_to_table(self, table, data):
		SUPABASE_HEADERS = {
			'apikey': self.api_key,
			'Authorization': 'Bearer' + self.api_key}
		SUPABASE_HEADERS['content-Type'] = 'application/json'
		SUPABASE_HEADERS['Prefer'] = 'return=representation'
		response = requests.post(f'{self.url}/{table}', headers=SUPABASE_HEADERS, json=data)
		res = json.loads(response.text)
		return res

