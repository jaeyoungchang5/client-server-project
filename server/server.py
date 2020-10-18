'''
Final Project - Web Startup
server.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
from recruitmentController import RecruitmentController
from recruitment_library import _recruitment_database

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	rdb = _recruitment_database()

	# TODO: declare controllers
	recruitmentController = RecruitmentController(rdb=rdb)
	# TODO: dispatchers
	dispatcher.connect('ethnicity_get', '/tests/:ethnicity', controller=recruitmentController, action='GET_KEY', conditions=dict(method=['GET']))
	dispatcher.connect('test_get', '/ethnicities/:test', controller=recruitmentController, action='GET_KEY', conditions=dict(method=['GET']))
	dispatcher.connect('tests_get', '/tests/', controller=recruitmentController, action='GET_TESTS', conditions=dict(method=['GET']))
	dispatcher.connect('ethnicities_get', '/ethnicities/', controller=recruitmentController, action='GET_ETHNICITIES', conditions=dict(method=['GET']))
	dispatcher.connect('result_put', '/results/:test', controller=recruitmentController, action='PUT_RESULT', conditions=dict(method=['PUT']))
	dispatcher.connect('result_post', '/results/', controller=recruitmentController, action='POST_RESULT', conditions=dict(method=['POST']))
	dispatcher.connect('result_delete', '/results/', controller=recruitmentController, action='DELETE_RESULT', conditions=dict(method=['DELETE']))
	

	conf = {
			'global': {
				'server.thread_pool': 5,
				'server.socket_host': 'localhost',
				},
			'/': {
				'request.dispatch': dispatcher,
				}
			}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

# end of start_service

if __name__ == '__main__':
	start_service()
