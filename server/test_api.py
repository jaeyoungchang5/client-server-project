# test_api.py

'''
Final Project - Web Startup
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import unittest
import requests
import json

class TestAPI(unittest.TestCase):

	SITE_URL = 'http://localhost:8080'
	print("testing for server: " + SITE_URL)
	ETHNICITIES_URL = SITE_URL + '/ethnicities/'
	TEST_URL = SITE_URL + '/tests/'

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_get_ethnicity(self):
		ethnicity = 'White (Not Hispanic or Latino)'
		r = requests.get(self.ETHNICITIES_URL + ethnicity)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp[''], '')
		self.assertEqual(resp[''], '')

if __name__ == "__main__":
	unittest.main()
