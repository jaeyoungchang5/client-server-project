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
	RESULT_URL = SITE_URL + '/results/'

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_get_ethnicity(self):
		ethnicity = 'White (Not Hispanic or Latino)'
		r = requests.get(self.TEST_URL + ethnicity)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp[''], '')
		self.assertEqual(resp[''], '')

	def test_get_test(self):
		test = 'Passed_Physical_Test'

		r = requests.get(self.ETHNICITIES_URL + test)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))

	def test_get_tests(self):
		r = requests.get(self.TEST_URL)
		self.asserTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))

	def test_get_ethnicities(self):
		r = requests.get(self.ETHNICITIES_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))

	def test_put_result(self):
		test = 'Passed_Physical_Test'
		r = requests.get(self.TEST_URL + test)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['test'], '')
		
		d = {}
		d['test'] = 'Passed_Physical Test'
		d['ethnicity'] = 'White (Not Hispanic or Latino)'
		r = requests.put(self.TEST_URL + test, data = json.dumps(d))

		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.TEST_URL + test)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['test'], d['test'])
		self.assertEqual(resp['ethnicity'], d['ethnicity'])

	def test_post_result(self):
		d = {}
		d['test'] = 'Passed_Physical_Test'
		d['ethnicity'] = 'White (Not Hispanic or Latino)'

		r = requests.post(self.RESULT_URL, data = json.dumps(d))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp[''], )

		r = requests.get(self.TEST_URL + str(resp['']))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['test'], d['test'])
		self.assertEqual(resp['ethnicity'], d['ethnicity'])

	def test_delete_result(self):
		d = {}
		
		r = requests.delete(self.TEST_URL, data = json.dumps(d))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.TEST_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		dic = resp['candidates']
		self.assertFalse(dic)


if __name__ == "__main__":
	unittest.main()
