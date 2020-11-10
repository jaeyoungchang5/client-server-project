'''
Final Project - Web Startup
recruitmentController.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
import re, json
from recruitment_library import _recruitment_database

class RecruitmentController(object):
	def __init__(self, rdb=None):
		if rdb is None:
			self.rdb = _recruitment_database()
		else:
			self.rdb = rdb

		print('controller load data')
		url = 'https://services1.arcgis.com/0n2NelSAfR7gTkr1/arcgis/rest/services/SBPD_Recruiting_Ethnicity/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
		self.rdb.load_recruitment_data(url)

	# grabs all types of tests and their information by ethnicity
	def GET_ETHNICITY(self, ethnicity):
		output = {'result' : 'success'}
		
		try:
			result = self.rdb.get_ethnicity(ethnicity)

			if result is not None:
				# for test, value in result.items():
				# 	output[test] = value
				output.update(result)
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
				output.update(result)
			else:
				output['result'] = 'error'
				output['message'] = 'test not found'
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		print(output)
		return json.dumps(output)

	# grabs all test data for each ethnicity
	def GET_TESTS(self):
		output = {'result' : 'success'}

		try:
			result = self.rdb.get_tests()
			if result is not None:
				output.update(result)
			else:
				output['result'] = 'error'
				output['message'] = 'tests not found'

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	# grabs all ethnicity data for each test
	def GET_ETHNICITIES(self):
		output = {'result' : 'success'}

		try:
			result = self.rdb.get_ethnicities()
			if result is not None:
				output.update(result)
			else:
				output['result'] = 'error'
				output['message'] = 'ethnicities not found'

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	# updates specific test result for a particular ethnicity
	def PUT_RESULT(self, ethnicity):
		output = {'result' : 'success'}

		data = json.loads(cherrypy.request.body.read().decode('utf-8'))

		tests = dict()
		for test, value in data.items():
			tests[test] = value

		self.rdb.put_result(ethnicity, data)


		return json.dumps(output)