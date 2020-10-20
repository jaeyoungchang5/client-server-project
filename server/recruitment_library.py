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
			result = None
		
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
		print('put_result')
		try:
			print(self.recruitment_data[ethnicity])
			for test, value in results.items():
				if value is True:
					self.recruitment_data[ethnicity][test] += 1
				else:
					self.recruitment_data[ethnicity][test] -= 1
			
			print(self.recruitment_data[ethnicity])
		except Exception as ex:
			result = None


	def post_result(self, ethnicity, test):
		print('post_result')
		self.recruitment_data[ethnicity][test] += 1
	
	def delete_result(self, ethnicity, test):
		print('post_result')
		self.recruitment_data[ethnicity][test] -= 1
	




if __name__ == "__main__":
	url = 'https://services1.arcgis.com/0n2NelSAfR7gTkr1/arcgis/rest/services/SBPD_Recruiting_Ethnicity/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

	rdb = _recruitment_database()

	rdb.load_recruitment_data(url)
	print(rdb.get_ethnicity('Asian (Not Hispanic or Latino)'))
	print(rdb.get_test('Took_Physical_Test'))
	print(rdb.get_ethnicities())
	print(rdb.get_tests())
	rdb.post_result('Asian (Not Hispanic or Latino)', 'Took_Physical_Test')
	rdb.put_result('Asian (Not Hispanic or Latino)', {'Took_Physical_Test': True, 'Passed_Physical_Test': True, 'Completed_Written_Test': False})
	print(rdb.get_ethnicity('Asian (Not Hispanic or Latino)'))



class _recruitment_database:

	def __init__(self):
		self.recruitment_data = dict()
		'''
		Structure of dictionary: dictionary of dictionaries
		{
			'Ethnicity 1': 
				{
					'Test 1': 6, 
					'Test 2': 7, 
					...
				}, 
			'Ethnicity 2': {...}, ...
		}
		'''

	def load_recruitment_data(self, url):
		print('loading data')
		content = requests.get(url)
		jsonObj = json.loads(content.content)
		for element in jsonObj['features']:
			ethnicity = element['attributes']

			if ethnicity['Ethnicity'] == 'White (Not Hispanic or Latino)':
				ethnicity['Ethnicity'] = 'White'

			self.recruitment_data[ethnicity['Ethnicity']] = dict()
			for test, value in ethnicity.items():
				if test == 'Ethnicity':
					continue

				self.recruitment_data[ethnicity['Ethnicity']][test] = value
		print(self.recruitment_data)
	
	def get_ethnicity(self, ethnicity):
		print('get_ethnicity')
		try:
			result = self.recruitment_data[ethnicity]
		except Exception as ex:
			result = None
		print(result)

		'''
		What get_ethnicity returns:
		- given an ethnicity, it returns the ethnicity's results for each test

		Structure of result:
		{
			'Test 1': 9, 
			'Test 2': 20, ...
		}
		'''
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
			result = None
		
		'''
		What get_test returns:
		- given a test, it returns how every ethnicity scored for the given test

		Structure of result:
		{
			'Ethnicity 1': 6,
			'Ethnicity 2': 8, ...
		}
		'''
		return result
	
	def get_ethnicities(self):
		print('get_ethnicities')
		result = dict()
		try:
			for ethnicity, value in self.recruitment_data.items():
				result[ethnicity] = value['Submitted_Application']
		except Exception as ex:
			result = None
			
		'''
		What get_ethnicities returns:
		- how much of each ethnicity applied to SBPD

		Structure of result:
		{
			'Ethnicity 1': 40,
			'Ethnicity 2': 80, ...
		}
		'''
		return result
		
	
	def get_tests(self):
		print('get_tests')
		try:
			result = self.recruitment_data['All']
		except Exception as ex:
			result = None

		'''
		What get_tests returns:
		- how many people took/passed each test

		Structure of result:
		{
			'Test 1': 1830,
			'Test 2': 1374, ...
		}
		'''
		return result

	def put_result(self, data):
		print('put_result')
		ethnicity = data['Ethnicity']
		results = data['Tests']
		try:
			print(self.recruitment_data[ethnicity])
			for test, value in results.items():
				if value is True:
					self.recruitment_data[ethnicity][test] += 1
				else:
					self.recruitment_data[ethnicity][test] -= 1
		except Exception as ex:
			result = None


	def post_result(self, data):
		print('post_result')
		ethnicity = data['Ethnicity']
		test = data['Test']
		print(f'before: {self.recruitment_data[ethnicity][test]}')
		self.recruitment_data[ethnicity][test] += 1
		print(f'after: {self.recruitment_data[ethnicity][test]}')
	
	def delete_result(self, data):
		print('post_result')
		ethnicity = data['Ethnicity']
		test = data['Test']
		print(f'before: {self.recruitment_data[ethnicity][test]}')
		self.recruitment_data[ethnicity][test] -= 1
		print(f'after: {self.recruitment_data[ethnicity][test]}')

if __name__ == "__main__":
	url = 'https://services1.arcgis.com/0n2NelSAfR7gTkr1/arcgis/rest/services/SBPD_Recruiting_Ethnicity/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

	rdb = _recruitment_database()

	rdb.load_recruitment_data(url)
	print(rdb.get_ethnicity('White'))
	print(rdb.get_test('Passed_Physical_Test'))
	print(rdb.get_ethnicities())
	print(rdb.get_tests())
	rdb.post_result({'Ethnicity': 'White', 'Test': 'Took_Physical_Test'})
	rdb.delete_result({'Ethnicity': 'White', 'Test': 'Took_Physical_Test'})
	rdb.put_result({'Ethnicity': 'White', 'Tests': {'Took_Physical_Test': True, 'Passed_Physical_Test': True, 'Completed_Written_Test': False}})
