#this program would load an image and try to find the pattern of a blue circle
#inside a yellow circle, and print out the pattern's related parameters.
import time
from SimpleCV import *

cam = Camera(0, {'width':1024, 'height':768})


size = cam.getImage().size()
display = Display(size)

while display.isNotDone():
	start_time = time.time()
	
	source = cam.getImage()
	yellow_distance = source.colorDistance(Color.YELLOW).binarize(thresh=100)
	yellow_blobs = yellow_distance.findBlobs()
	if yellow_blobs is None:
		source.save(display)
		continue

			
	blue_distance = source.colorDistance(Color.BLUE).binarize(thresh=150)
	blue_blobs = blue_distance.findBlobs()
	if blue_blobs is None:
		source.save(display)
		continue

	
	for yellow_blob in yellow_blobs:
		for blue_blob in blue_blobs:
			if yellow_blob.contains(blue_blob):
				print "found pattern!"
				print "yellow circle centre is", yellow_blob.x, yellow_blob.y
				print "yellow circle radius is", yellow_blob.radius()
				print "blue circle center is", blue_blob.x, blue_blob.y
				print "blue circle radius is", blue_blob.radius()
				yellow_centre = (yellow_blob.x, yellow_blob.y)
				blue_centre = (blue_blob.x, blue_blob.y)
				source.dl().circle(blue_centre, blue_blob.radius(), Color.BLACK, width=3)
				source.dl().circle(yellow_centre, yellow_blob.radius(), Color.BLACK, width=6)
	source.save(display)

	print "elapsed", time.time()-start_time
