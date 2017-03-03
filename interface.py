import os 
import sys
from matplotlib import pyplot as plt
class Interface(object):
	if img is None:
	print("Failed to load image file")
	sys.exit(1)
	
	if len(img.shape) == 3:
		height, width, channel = img.shape[:3]
	else:
		height, width = img.shape[:2]
	channel = 1
print ("width:" + str(width))
print ("height: "+ str(height))
print ("channel:" + str(channel))
print ("dtype:" + str(img.dtype)) 
	
