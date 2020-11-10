'''
Final Project - Web Startup
server.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
from recruitmentController import RecruitmentController
from recruitment_library import _recruitment_database
from userController import UserController
from user_library import _user_database
from resetController import ResetController

class optionsController:
	def OPTIONS(self, *args, **kwargs):
		return ""

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"


def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	rdb = _recruitment_database()
	udb = _user_database()

	# TODO: declare controllers
	recruitmentController = RecruitmentController(rdb=rdb)
	userController = UserController(udb=udb)
	resetController = ResetController(rdb=rdb)
	# TODO: dispatchers
	dispatcher.connect('ethnicity_get', '/tests/:ethnicity', controller=recruitmentController, action='GET_ETHNICITY', conditions=dict(method=['GET']))
	dispatcher.connect('test_get', '/ethnicities/:test', controller=recruitmentController, action='GET_TEST', conditions=dict(method=['GET']))

	dispatcher.connect('tests_get', '/tests/', controller=recruitmentController, action='GET_TESTS', conditions=dict(method=['GET']))
	dispatcher.connect('ethnicities_get', '/ethnicities/', controller=recruitmentController, action='GET_ETHNICITIES', conditions=dict(method=['GET']))

	dispatcher.connect('result_put', '/results/:ethnicity', controller=recruitmentController, action='PUT_RESULT', conditions=dict(method=['PUT']))

	dispatcher.connect('user_post', '/user/:username', controller=userController, action = 'POST_USER', conditions=dict(method=['POST']))
	dispatcher.connect('user_delete', '/user/:username', controller=userController, action = 'DELETE_USER', conditions=dict(method=['DELETE']))
	dispatcher.connect('user_get_all', '/user/all/', controller=userController, action = 'GET_USERS', conditions=dict(method=['GET']))
	

	dispatcher.connect('reset_data', '/reset/', controller=resetController, action='RESET_DATA', conditions=dict(method=['PUT']))

	# CORS related options endpoints
	dispatcher.connect('tests_key_options', '/tests/:ethnicity', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('ethnicities_key_options', '/ethnicities/:test', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('tests_options', '/tests/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('ethnicities_options', '/ethnicities/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	
	dispatcher.connect('put_results_options', '/results/:ethnicity', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('user_key_options', '/user/:username', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('user_options', '/user/all/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('reset_options', '/reset/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))


	conf = {
			'global': {
				'server.thread_pool': 5,
				'server.socket_host': 'student13.cse.nd.edu',
				'server.socket_port': 51047,
				},
			'/': {
				'request.dispatch': dispatcher,
				'tools.CORS.on': True,
				}
			}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

# end of start_service

if __name__ == '__main__':
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()
