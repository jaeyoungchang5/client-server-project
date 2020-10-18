'''
Final Project - Web Startup
RecruitmentController.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
import re, json
from recruitment_library import _recruitment_database

url='https://services1.arcgis.com/0n2NelSAfR7gTkr1/arcgis/rest/services/SBPD_Recruiting_Ethnicity/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

class RecruitmentController(object):
	def __init__(self, rdb=None):
		if rdb is None:
			self.rdb = _recruitment_database()
		else:
			self.rdb = rdb
		
		self.mdb.load_recruitment_data(url)

	# grabs all types of tests and their information by ethnicity
	def GET_ETHNICITY(self, eth):
		output = {'result' : 'success'}
		
		try:
			ethnicity_results = self.edb.get_ethnicity(eth)

			if ethnicity_results is not None:

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

