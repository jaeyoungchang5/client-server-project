'''
Final Project - Web Startup
resetController.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

import cherrypy
import re, json
from recruitment_library import _recruitment_database

class ResetController(object):
    def __init__(self, rdb=None):
        if rdb is None:
            self.rdb = _recruitment_database()
        else:
            self.rdb = rdb
        
        

    def RESET_DATA(self):
        output = {'result' : 'success'}

        data = json.loads(cherrypy.request.body.read().decode())

        self.rdb.__init__()
        print('RESET: loading data')
        url = 'https://services1.arcgis.com/0n2NelSAfR7gTkr1/arcgis/rest/services/SBPD_Recruiting_Ethnicity/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
        self.rdb.load_recruitment_data(url)
        return json.dumps(output)