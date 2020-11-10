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
			ethnicity_obj = element['attributes']
			ethnicity = ethnicity_obj['Ethnicity']

			ethnicity = shorten_name(ethnicity)

			self.recruitment_data[ethnicity] = dict()

			for test, value in list(ethnicity_obj.items())[1:]:
				self.recruitment_data[ethnicity][test] = value

		# print(self.recruitment_data)
	
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

	def put_result(self, ethnicity, tests):
		print(f'Tests: {tests}')
		print('put_result')
		try:
			print(f'Before: {self.recruitment_data[ethnicity]}')
			for test, value in tests.items():
				if value is True:
					self.recruitment_data[ethnicity][test] += 1
				else:
					self.recruitment_data[ethnicity][test] -= 1
			print(f'After: {self.recruitment_data[ethnicity]}')
		except Exception as ex:
			result = None

# Helper function to help simplify / shorten Ethnicity Name
def shorten_name(ethnicity):
	if ethnicity == 'American Indian or Alaska Native (Not Hispanic or Latino)':
		ethnicity = 'American-Indian'
	elif ethnicity == 'Asian (Not Hispanic or Latino)':
		ethnicity = 'Asian'
	elif ethnicity == 'Black or African American (Not Hispanic or Latino)':
		ethnicity = 'Black'
	elif ethnicity == 'Hispanic or Latino':
		ethnicity = 'Latino'
	elif ethnicity == 'Native Hawaiian or Other Pacific Islander (Not Hispanic or Latino)':
		ethnicity = 'Hawaiian'
	elif ethnicity == 'Prefer not to answer':
		ethnicity = 'NA'
	elif ethnicity == 'Two or More Races (Not Hispanic or Latino)':
		ethnicity = 'Multiple'
	elif ethnicity == 'White (Not Hispanic or Latino)':
		ethnicity = 'White'
	elif ethnicity == '(blank)':
		ethnicity = 'Blank'
	return ethnicity

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
	rdb.put_result('White', {'Took_Physical_Test': True, 'Passed_Physical_Test': True, 'Completed_Written_Test': False})
