'''
Final Project - Web Startup
user_library.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import requests
import json

class _user_database():
    def __init__(self):
        self.user_data = dict()

    def post_user(self, username, data):
        print(f'adding user ({username})')
        self.user_data[username] = dict()
        
        self.user_data[username]['fname'] = data['fname']
        self.user_data[username]['lname'] = data['lname']
        
        self.user_data[username]['password'] = data['password']
        self.user_data[username]['email'] = data['email']
        print(f'user data: {self.user_data[username]}')


    def delete_user(self, username):
        print(f'deleting user ({username})')
        del(self.user_data[username])
    
    def get_users(self):
        print('getting all user data')
        try:
            result = dict()
            for key, value in self.user_data.items():
                result[key] = value
            print(f'all user data: {result}')
        except Exception as ex:
            result = None

        return result


if __name__ == '__main__':
    udb = _user_database()

    data = {'fname': 'FNAME1', 'lname': 'LNAME1', 'password': 'Test Password 1', 'email': 'test@test.com'}
    udb.post_user('username1', data)
    data = {'fname': 'FNAME2', 'lname': 'LNAME2', 'password': 'Test Password 2', 'email': 'tes2@test.com'}
    udb.post_user('username2', data)
    print(udb.get_users())
    udb.delete_user('username1')
    print(udb.get_users())

        