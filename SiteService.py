#!/bin/python
import sys
import os
import cherrypy
from NameChecker import Builder
from newMethod import checkUsername
import datetime

today = datetime.datetime.now()
today = today.strftime('%m %d %Y %H:%M')

def ErrorPage(status, message, traceback, version):
	return "ERROR"
def multiLog(username, status, time):
    i=1
    while True:
        FILE = open('/var/www/html/assets/names'+str(i)+'.log', 'a+')
        AMOUNT = len(FILE.readlines())
        if AMOUNT == 35:
            i+=1
            FILE.close()
        if AMOUNT != 35:
            FILE.write(username+"|"+status+"|"+time+"\n")
            break

cherrypy.config.update({'server.socket_host': '66.70.189.221',})
cherrypy.config.update({'server.socket_port': 331,})
cherrypy.config.update({'tools.sessions.on': False,})
cherrypy.config.update({'error_page.404': ErrorPage})

class SiteService(object):
	@cherrypy.expose
	def index(self):
		return "How'd you get here? Seriously, you nasty little hacker."

	@cherrypy.expose
	def check(self, username=""):
            if username == "":
                return "ERROR"
            else:
                CheckedName = checkUsername(username)
                logName(username, CheckedName, today)
                multiLog(username, CheckedName, today)
                return CheckedName

if __name__ == '__main__':
	cherrypy.quickstart(SiteService())
