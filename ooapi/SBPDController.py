'''
Final Project - Web Startup
SBPDController.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
import re, json
from SBPD_library import _ethnicities_database

class SBPDController(object):
	def __init__(self, edb=None):
		if edb is None:
			self.edb = _ethnicities_database()
		else:
			self.edb = edb

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

