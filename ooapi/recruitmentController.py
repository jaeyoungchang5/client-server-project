'''
Final Project - Web Startup
RecruitmentController.py
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
		
		self.mdb.load_recruitment()

	# grabs all types of tests and their information by ethnicity
	def GET_ETHNICITY(self, eth):
		output = {'result' : 'success'}
		
		try:
			if:

			else:
				output['result'] = 'error'
				output['message'] = 'ethnicity not found'
			
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	# grabs all ethnicities and their result for a specific test type
	def GET_TEST(self, test):
		output = {'result' : 'success'}

		try:

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	# grabs all types of tests for 2 user-specified ethnicities
	def GET_COMPARE(self, eth1, eth2):


	# grabs all test data for each ethnicity
	def GET_TESTS(self):


	# grabs all ethnicity data for each test
	def GET_ETHNICITIES(self):


	# updates specific test result for a particular ethnicity

