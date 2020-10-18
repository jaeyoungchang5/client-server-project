'''
Final Project - Web Startup
recruitment_library.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import requests
import json

class _recruitment_database:

	def __init__(self):
		self.recruitment_data = dict()
		# Structure of dict
		# 

	def load_recruitment_data(self, url):
		print('loading data')
		content = requests.get(url)
		jsonObj = json.loads(content.content)
		for element in jsonObj['features']:
			ethnicity = element['attributes']
			self.recruitment_data[ethnicity['Ethnicity']] = dict()
			for test, value in ethnicity.items():
				if test == 'Ethnicity':
					continue

				self.recruitment_data[ethnicity['Ethnicity']][test] = value
		print(self.recruitment_data)
		# for key, value in self.recruitment_data.items():
		# 	print(key)
		# 	print(value)
		# 	print()
	
	def get_ethnicity(self, ethnicity):
		print('get_ethnicity')
		try:
			result = self.recruitment_data[ethnicity]
		except Exception as ex:
			result = None

		return result
	
	def get_test(self, utest):
		print('get_test')
		result = dict()
		try:
			for ethnicity, tests in self.recruitment_data.items():
				for test, value in tests.items():
					if test == utest:
						result[ethnicity]= value
		except Exception as ex:
			pass
		
		return result
	
	def get_ethnicities(self):
		print('get_ethnicities')
		result = dict()
		try:
			for ethnicity, value in self.recruitment_data.items():
				result[ethnicity] = value['Submitted_Application']
		except Exception as ex:
			result = None
			
		return result
		
	
	def get_tests(self):
		print('get_tests')
		try:
			result = self.recruitment_data['All']
		except Exception as ex:
			result = None

		return result

	def put_result(self, ethnicity, results):
		pass

	




if __name__ == "__main__":
	url = 'https://services1.arcgis.com/0n2NelSAfR7gTkr1/arcgis/rest/services/SBPD_Recruiting_Ethnicity/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

	rdb = _recruitment_database()

	rdb.load_recruitment_data(url)
	print(rdb.get_ethnicity('Asian (Not Hispanic or Latino)'))
	print(rdb.get_test('Took_Physical_Test'))
	print(rdb.get_ethnicities())
	print(rdb.get_tests())
