__meta={"type":"internal_script","name":"Config","version":[0,0,0,0]}
import Debug
import json
def loadConfigFile(location):
	uconf = open(location)
	global conf 
	conf=json.loads(uconf.read())