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
	RESET_URL = SITE_URL + '/reset/'

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError as ex:
			return False
	
	def reset_data(self):
		r = requests.put(self.RESET_URL)

	def test_get_ethnicity(self):
		self.reset_data()
		ethnicity = 'White'
		r = requests.get(self.TEST_URL + ethnicity)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))

		self.assertEqual(resp['Submitted_Application'], 818)
		self.assertEqual(resp['Took_Physical_Test'], 181)
		self.assertEqual(resp['Passed_Physical_Test'], 154)
		self.assertEqual(resp['Completed_Written_Test'], 126)
		self.assertEqual(resp['Passed_Written_Test'], 106)
		self.assertEqual(resp['Completed_Interview'], 76)
		self.assertEqual(resp['Passed_Interview'], 51)
		self.assertEqual(resp['Passed_Background'], 40)
		self.assertEqual(resp['Passed_Polygraph__Medical__Psyc'], 26)

	def test_get_test(self):
		self.reset_data()
		test = 'Passed_Physical_Test'
		r = requests.get(self.ETHNICITIES_URL + test)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))

		self.assertEqual(resp['American Indian or Alaska Native (Not Hispanic or Latino)'], 0)
		self.assertEqual(resp['Asian (Not Hispanic or Latino)'], 4)
		self.assertEqual(resp['Black or African American (Not Hispanic or Latino)'], 33)
		self.assertEqual(resp['Hispanic or Latino'], 36)
		self.assertEqual(resp['Native Hawaiian or Other Pacific Islander (Not Hispanic or Latino)'], 0)
		self.assertEqual(resp['Prefer not to answer'], 1)
		self.assertEqual(resp['Two or More Races (Not Hispanic or Latino)'], 8)
		self.assertEqual(resp['Unknown'], 0)
		self.assertEqual(resp['White'], 154)
		self.assertEqual(resp['(blank)'], 32)

	def test_get_tests(self):
		self.reset_data()
		r = requests.get(self.TEST_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())

		self.assertEqual(resp['Submitted_Application'], 1374)
		self.assertEqual(resp['Took_Physical_Test'], 321)
		self.assertEqual(resp['Passed_Physical_Test'], 268)
		self.assertEqual(resp['Completed_Written_Test'], 214)
		self.assertEqual(resp['Passed_Written_Test'], 168)
		self.assertEqual(resp['Completed_Interview'], 111)
		self.assertEqual(resp['Passed_Interview'], 79)
		self.assertEqual(resp['Passed_Background'], 57)
		self.assertEqual(resp['Passed_Polygraph__Medical__Psyc'], 33)

	def test_get_ethnicities(self):
		self.reset_data()
		r = requests.get(self.ETHNICITIES_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())

		self.assertEqual(resp['American Indian or Alaska Native (Not Hispanic or Latino)'], 3)
		self.assertEqual(resp['Asian (Not Hispanic or Latino)'], 20)
		self.assertEqual(resp['Black or African American (Not Hispanic or Latino)'], 256)
		self.assertEqual(resp['Hispanic or Latino'], 151)
		self.assertEqual(resp['Native Hawaiian or Other Pacific Islander (Not Hispanic or Latino)'], 1)
		self.assertEqual(resp['Prefer not to answer'], 13)
		self.assertEqual(resp['Two or More Races (Not Hispanic or Latino)'], 52)
		self.assertEqual(resp['Unknown'], 0)
		self.assertEqual(resp['White'], 818)
		self.assertEqual(resp['(blank)'], 60)

	# def test_put_result(self):
	# 	test = 'Passed_Physical_Test'
	# 	r = requests.get(self.TEST_URL + test)
	# 	self.assertTrue(self.is_json(r.content.decode('utf-8')))
	# 	resp = json.loads(r.content.decode('utf-8'))
	# 	self.assertEqual(resp['test'], '')
		
	# 	d = {}
	# 	d['test'] = 'Passed_Physical Test'
	# 	d['ethnicity'] = 'White (Not Hispanic or Latino)'
	# 	r = requests.put(self.TEST_URL + test, data = json.dumps(d))

	# 	self.assertTrue(self.is_json(r.content.decode('utf-8')))
	# 	resp = json.loads(r.content.decode('utf-8'))
	# 	self.assertEqual(resp['result'], 'success')

	# 	r = requests.get(self.TEST_URL + test)
	# 	self.assertTrue(self.is_json(r.content.decode('utf-8')))
	# 	resp = json.loads(r.content.decode('utf-8'))
	# 	self.assertEqual(resp['test'], d['test'])
	# 	self.assertEqual(resp['ethnicity'], d['ethnicity'])

	# def test_post_result(self):
	# 	d = {}
	# 	d['test'] = 'Passed_Physical_Test'
	# 	d['ethnicity'] = 'White (Not Hispanic or Latino)'

	# 	r = requests.post(self.RESULT_URL, data = json.dumps(d))
	# 	self.assertTrue(self.is_json(r.content.decode()))
	# 	resp = json.loads(r.content.decode())
	# 	self.assertEqual(resp['result'], 'success')
	# 	self.assertEqual(resp[''], )

	# 	r = requests.get(self.TEST_URL + str(resp['']))
	# 	self.assertTrue(self.is_json(r.content.decode()))
	# 	resp = json.loads(r.content.decode())
	# 	self.assertEqual(resp['test'], d['test'])
	# 	self.assertEqual(resp['ethnicity'], d['ethnicity'])

	# def test_delete_result(self):
	# 	d = {}
		
	# 	r = requests.delete(self.TEST_URL, data = json.dumps(d))
	# 	self.assertTrue(self.is_json(r.content.decode()))
	# 	resp = json.loads(r.content.decode())
	# 	self.assertEqual(resp['result'], 'success')

	# 	r = requests.get(self.TEST_URL)
	# 	self.assertTrue(self.is_json(r.content.decode()))
	# 	resp = json.loads(r.content.decode())
	# 	dic = resp['candidates']
	# 	self.assertFalse(dic)


if __name__ == "__main__":
	unittest.main()
