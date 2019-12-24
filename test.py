import sys, os
#sys.path.append(os.path.join(os.path.expanduser("~"), 'platform'))	# Work
sys.path.append("platform")	# test
from configuration import robot

robot.move(10)

