#!/usr/bin/python
import json
config_file = open('agentconfig.json','r')
configurations = json.load(config_file)
#print configurations.keys()
#print configurations.values()

for scriptname,time_value in configurations.items():
	print 'for ' + scriptname + ' the time value set is: ' +  time_value

