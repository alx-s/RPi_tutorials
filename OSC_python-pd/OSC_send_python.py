#! /usr/bin/python

import OSC
import time

# Init OSC
client = OSC.OSCClient()
client.connect(('127.0.0.1', 9001)) # first argument is the IP of the host, second argument the port to use

try:
	client.send(OSC.OSCMessage("/adress", data) # first argument is the what we could call the OSC adress of the data, second argument is the actual data to be sent.
except:
	print "not connected"
        pass
