import cv2
import os
import shutil
import re

dir_path = './imgs/'
ext = 'png'

# sort images in directory
def sorted_alphanumeric(data):
	convert = lambda text: int(text) if text.isdigit() else text.lower()
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
	return sorted(data, key=alphanum_key)

# TODO: scale up low resolution image + gaussian blur
def scaleBlur():
	pass

# merge images into video
def createVideo(name):
	output = str(name) + '.mp4'
	
	# create directory list of images
	images = []
	for f in sorted_alphanumeric(os.listdir(dir_path)):
		if f.endswith(ext):
			images.append(f)

	# Determine the width and height from the first image
	image_path = os.path.join(dir_path, images[0])
	frame = cv2.imread(image_path)
	cv2.imshow('video',frame)
	height, width, channels = frame.shape

	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
	#fourcc = cv2.VideoWriter_fourcc(*'gifv') # Be sure to use lower case
	out = cv2.VideoWriter(output, fourcc, 25.0, (width, height))

	for image in images:
		image_path = os.path.join(dir_path, image)
		frame = cv2.imread(image_path)
		out.write(frame) # Write out frame to video
		cv2.imshow('video',frame)
		if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
			break

	# Release everything if job is finished
	out.release()
	cv2.destroyAllWindows()

	print("...history video saved as {}".format(output))

# delete all files in the dir_path
def delImgs():
	for filename in os.listdir(dir_path):
	    file_path = os.path.join(dir_path, filename)
	    try:
	        if os.path.isfile(file_path) or os.path.islink(file_path):
	            os.unlink(file_path)
	        elif os.path.isdir(file_path):
	            shutil.rmtree(file_path)
	    except Exception as e:
	        print('Failed to delete %s. Reason: %s' % (file_path, e))

