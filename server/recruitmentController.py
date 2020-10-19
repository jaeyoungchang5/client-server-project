'''
Final Project - Web Startup
RecruitmentController.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
import re, json
from recruitment_library import _recruitment_database

#url='https://services1.arcgis.com/0n2NelSAfR7gTkr1/arcgis/rest/services/SBPD_Recruiting_Ethnicity/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

class RecruitmentController(object):
	def __init__(self, rdb=None):
		if rdb is None:
			self.rdb = _recruitment_database()
		else:
			self.rdb = rdb

		url = 'https://services1.arcgis.com/0n2NelSAfR7gTkr1/arcgis/rest/services/SBPD_Recruiting_Ethnicity/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
		self.rdb.load_recruitment_data(url)

	# grabs all types of tests and their information by ethnicity
	def GET_ETHNICITY(self, eth):
		output = {'result' : 'success'}
		
		try:
			ethnicity_results = self.rdb.get_ethnicity(eth)

			if ethnicity_results is not None:
				result = self.rdb.get_ethnicity(eth)
				for test, value in result.items():
					output[test] = value
			else:
				output['result'] = 'error'
				output['message'] = 'ethnicity not found'
			
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		
		print(output)
		return json.dumps(output)

	# grabs all ethnicities and their result for a specific test type
	def GET_TEST(self, test):
		output = {'result' : 'success'}

		try:
			result = self.rdb.get_test(test)
			if result is not None:
				for ethnicity, value in result.items():
					output[ethnicity] = value
			else:
				output['result'] = 'error'
				output['message'] = 'test not found'
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		print(output)
		return json.dumps(output)

	# grabs all types of tests for 2 user-specified ethnicities
	def GET_COMPARE(self, eth1, eth2):
		pass

	# grabs all test data for each ethnicity
	def GET_TESTS(self):
		output = {'result' : 'success'}

		try:
			result = self.rdb.get_tests()
			if result is not None:
				for ethnicity, val1 in result.items():
					for test, val2 in result.items():
						output[ethnicity] = val1
						output[test] = val2
			else:
				output['result'] = 'error'
				output['message'] = 'tests not found'

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

	# grabs all ethnicity data for each test
	def GET_ETHNICITIES(self):
		output = {'result' : 'success'}

		try:
			result = self.rdb.get_ethnicities()
			if result is not None:
				for test, val1 in result.items():
					for ethnicity, val2 in result.items():
						output[test] = val1
						output[ethnicity] = val2
			else:
				output['result'] = 'error'
				output['message'] = 'ethnicities not found'

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

	# updates specific test result for a particular ethnicity
	def PUT_RESULT(self, test):
		pass
		'''
		output = {'result' : 'success'}

		data = json.loads(cherrypy.request.body.read().decode('utf-8'))

		tests = list()
		tests.append(data[''])
		tests.append(data[''])

		self.rdb.

		return json.dumps(output)
		'''

	# increment data for specific ethnicity
	def POST_RESULT(self, ethnicity, test):
		output = {'result' : 'success'}
		tests = list()
		data = json.loads(cherrypy.request.body.read())

		try:
			self.rdb.post_result(ethnicity, test)
		
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	# delete a candidate's application data
	def DELETE_RESULT(self, ethnicity, test):
		output = {'result' : 'success'}
		self.rdb.delete_result(ethnicity, test)

		return json.dumps(output)

