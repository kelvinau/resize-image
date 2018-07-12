import sys
import os
from PIL import Image
from resizeimage import resizeimage, imageexceptions
from shutil import copyfile
 
def resize(dir, widthStr):
    resizedDir = dir + 'resized/'
    width = int(widthStr)
    if not os.path.exists(resizedDir):
        os.makedirs(resizedDir)
    for filename in os.listdir(dir):
        if filename.endswith(('.JPG', '.jpg', '.JPEG', '.jpeg', '.PNG', '.png', '.GIF', '.gif')): 
            print 'Resizing {0}...'.format(filename)
            with Image.open(dir + filename) as image:
				try:
					cover = resizeimage.resize_width(image, width)
					cover.save(resizedDir + filename, image.format)
				except imageexceptions.ImageSizeError, e:
					copyfile(dir + filename, resizedDir + filename)
					print e.message
                
				
        
if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print "Please support the parameters (Make sure to add the last slash). e.g. python resize.py c:\image\ 640"
    else:
        resize(sys.argv[1], sys.argv[2])