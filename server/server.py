'''
Final Project - Web Startup
server.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
from ethnicies_library import _ethnicities_database

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	edb = _ethnicities_database()

	# TODO: declare controllers
	# TODO: dispatchers

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
