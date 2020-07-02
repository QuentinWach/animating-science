"""
This module enables the user to combine images from a given directory into a single mp4.
Created by Quentin Wach and can be used, adapted and shared under the MIT license.
"""
import cv2
import os
import re
import sys

# sort images in directory
def sorted_alphanumeric(data):
	convert = lambda text: int(text) if text.isdigit() else text.lower()
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
	return sorted(data, key=alphanum_key)

# delete all fille in dir
def delFiles(dir_path="img"):
	mypath = dir_path
	for root, dirs, files in os.walk(mypath):
	    for file in files:
	        os.remove(os.path.join(root, file))

# merge images into video
def createVideo(dir_path="img", output="movie.mp4"):
	ext = 'png'

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
	out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

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

	# delete all files in the directory
	delFiles(dir_path)
	print("...files deleted")

	print("...history video saved as {}".format(output))

