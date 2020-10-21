'''
Final Project - Web Startup
userController.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
import re, json
from user_library import _user_database

class UserController(object):
    def __init__(self, udb=None):
        if udb is None:
            self.udb = _user_database()
        else:
            self.udb = udb
    
    def POST_USER(self, username):
        output = {'result': 'success'}

        data = json.loads(cherrypy.request.body.read().decode('utf-8'))

        self.udb.post_user(username, data)

        return json.dumps(output)

    def DELETE_USER(self, username):
        output = {'result': 'success'}

        self.udb.delete_user(username)
        return json.dumps(output)

    def GET_USERS(self):
        output = {'result' : 'success'}

        try:
            result = self.udb.get_users()
            if result is not None:
                output.update(result)
            else:
                output['result'] = 'error'
                output['message'] = 'users not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
