#!/usr/bin/env python3
#allows for proper python2 support
from __future__ import division

import subprocess, os

from bottle import get, post, request, run, static_file, response, redirect

#############################################################
#					 POST PseudoDatabase					#
#############################################################

posts = {
	'one': {
		'image': "https://unsplash.it/640/480/?random&0,2",
		'title': "POST 1: Donald trump gets tackled by ex-rugby player during TV interview.",
		'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod \
				tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, \
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \
				Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
				Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
	},
	'two': {
		'image': "https://unsplash.it/640/480/?random&0,3",
		'title': "POST 2: Donald trump gets tackled by ex-rugby player during TV interview.",
		'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod \
				tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, \
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \
				Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
				Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
	},
	'three': {
		'image': "https://unsplash.it/640/480/?random&0,4",
		'title': "POST 3: Donald trump gets tackled by ex-rugby player during TV interview.",
		'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod \
				tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, \
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \
				Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
				Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
	}
}
#############################################################
#					   BOTTLE Server						#
#			Acts as both the main HTML Server				#
#				  and the message server.					#
#############################################################

print(os.path.realpath(__file__))
htmlFileDirectory = os.path.realpath(__file__).replace("/demonewsserver.py", "")

@get('/discover') # or @route('/login')
def discover():
	file = open(htmlFileDirectory + "/Advanced Squadra - Newspaper.html", 'r')
	interfacePage = file.read()
	file.close()
	
	return interfacePage

@get("/")
def wrong():
    redirect("/discover")

#192.168.1.1:1337/getpost?id=one
@get('/getpost') # or @route('/login')
def getpost():
	postID = request.query.id
	print ("Message ID: " + str(postID))

	output = "\
	<div id='image'>" + posts[postID]["image"] + "</div>\
	<div id='title'>" + posts[postID]["title"] + "</div>\
	<div id='body'>" + posts[postID]["body"] + "</div>\
	"
	
	return output

#############################################################
#							INIT							#
#############################################################

daPort = 1337

#Init
stdoutdata = subprocess.check_output('ifconfig | grep "inet addr:192.168.1.10"', shell=True)
ipAddr = "192.168.1.10" + stdoutdata.decode("utf-8")[32]
print("Server is up @ " + ipAddr + ":" + str(daPort))
print()

run(host=ipAddr, port=daPort, debug=True)