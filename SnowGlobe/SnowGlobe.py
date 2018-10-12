from All_snowing_eye import *
import time

def mainLoop():
	snowGlobe()
	time.sleep(900)
	mainLoop()



mainLoop()
