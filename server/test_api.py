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

	SITE_URL = 'http://student13.cse.nd.edu:8080'
	print("testing for server: " + SITE_URL)
	ETHNICITIES_URL = SITE_URL + '/ethnicities/'
	TEST_URL = SITE_URL + '/tests/'
	RESULT_URL = SITE_URL + '/results/'
	RESET_URL = SITE_URL + '/reset/'
	USER_URL = SITE_URL + '/user/'

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

		self.assertEqual(resp['American-Indian'], 0)
		self.assertEqual(resp['Asian'], 4)
		self.assertEqual(resp['Black'], 33)
		self.assertEqual(resp['Latino'], 36)
		self.assertEqual(resp['Hawaiian'], 0)
		self.assertEqual(resp['NA'], 1)
		self.assertEqual(resp['Multiple'], 8)
		self.assertEqual(resp['Unknown'], 0)
		self.assertEqual(resp['White'], 154)
		self.assertEqual(resp['Blank'], 32)

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

		self.assertEqual(resp['American-Indian'], 3)
		self.assertEqual(resp['Asian'], 20)
		self.assertEqual(resp['Black'], 256)
		self.assertEqual(resp['Latino'], 151)
		self.assertEqual(resp['Hawaiian'], 1)
		self.assertEqual(resp['NA'], 13)
		self.assertEqual(resp['Multiple'], 52)
		self.assertEqual(resp['Unknown'], 0)
		self.assertEqual(resp['White'], 818)
		self.assertEqual(resp['Blank'], 60)

	def test_put_result(self):
		self.reset_data()
		ethnicity = 'White'
		tests = {'Took_Physical_Test': True, 'Passed_Physical_Test': True, 'Completed_Written_Test': False}

		r = requests.put(self.RESULT_URL + ethnicity, data = json.dumps(tests))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.TEST_URL + ethnicity)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))

		self.assertEqual(resp['Submitted_Application'], 818)
		self.assertEqual(resp['Took_Physical_Test'], 182)
		self.assertEqual(resp['Passed_Physical_Test'], 155)
		self.assertEqual(resp['Completed_Written_Test'], 125)
		self.assertEqual(resp['Passed_Written_Test'], 106)
		self.assertEqual(resp['Completed_Interview'], 76)
		self.assertEqual(resp['Passed_Interview'], 51)
		self.assertEqual(resp['Passed_Background'], 40)
		self.assertEqual(resp['Passed_Polygraph__Medical__Psyc'], 26)

	def test_post_user(self):
		username1 = 'user1'
		user_data_1 = {'fname': 'fname1', 'lname': 'lname1', 'password': 'password1', 'email': 'email1@test.com'}
		username2 = 'user2'
		user_data_2 = {'fname': 'fname2', 'lname': 'lname2', 'password': 'password2', 'email': 'email2@test.com'}

		r = requests.post(self.USER_URL + username1, data = json.dumps(user_data_1))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.post(self.USER_URL + username2, data = json.dumps(user_data_2))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.USER_URL + 'all/')
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())

		self.assertEqual(resp['user1'], {'fname': 'fname1', 'lname': 'lname1', 'password': 'password1', 'email': 'email1@test.com'})
		self.assertEqual(resp['user2'], {'fname': 'fname2', 'lname': 'lname2', 'password': 'password2', 'email': 'email2@test.com'})

	def test_delete_user(self):
		username1 = 'user1'
		user_data_1 = {'fname': 'fname1', 'lname': 'lname1', 'password': 'password1', 'email': 'email1@test.com'}
		username2 = 'user2'
		user_data_2 = {'fname': 'fname2', 'lname': 'lname2', 'password': 'password2', 'email': 'email2@test.com'}

		r = requests.post(self.USER_URL + username1, data = json.dumps(user_data_1))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.post(self.USER_URL + username2, data = json.dumps(user_data_2))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		username = 'user1'
		r = requests.delete(self.USER_URL + username)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.USER_URL + 'all/')
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())

		self.assertEqual(resp['user2'], {'fname': 'fname2', 'lname': 'lname2', 'password': 'password2', 'email': 'email2@test.com'})

	def test_get_users(self):
		username1 = 'user1'
		user_data_1 = {'fname': 'fname1', 'lname': 'lname1', 'password': 'password1', 'email': 'email1@test.com'}
		username2 = 'user2'
		user_data_2 = {'fname': 'fname2', 'lname': 'lname2', 'password': 'password2', 'email': 'email2@test.com'}

		r = requests.post(self.USER_URL + username1, data = json.dumps(user_data_1))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.post(self.USER_URL + username2, data = json.dumps(user_data_2))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.USER_URL + 'all/')
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())

		self.assertEqual(resp['user1'], {'fname': 'fname1', 'lname': 'lname1', 'password': 'password1', 'email': 'email1@test.com'})
		self.assertEqual(resp['user2'], {'fname': 'fname2', 'lname': 'lname2', 'password': 'password2', 'email': 'email2@test.com'})


	# def test_post_result(self):
	# 	d = {}
	# 	d['test'] = 'Passed_Physical_Test'
	# 	d['ethnicity'] = 'White (Not Latino)'

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
