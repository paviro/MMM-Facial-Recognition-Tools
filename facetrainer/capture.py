import lib.capture as capture
import lib.config as config

print "What do you want to do?"
print "[1] Capture training images from webcam"
print "[2] Convert '*.jpg' pictures from other cameras to training images"
choice = raw_input("--> ")
print
print "Enter the name of the person you want to capture or convert images for."
capture.CAPTURE_DIR = raw_input("--> ")
print "Images will be placed in " + config.TRAINING_DIR + capture.CAPTURE_DIR

if choice == "1":
    print
    print '-' * 20
    print "Starting process..."
    print
    capture.capture()
else:
    print
    print "Please enter path to images or drag and drop folder into terminal"
    capture.RAW_DIR = raw_input("--> ")
    print
    print '-' * 20
    print "Starting process..."
    print
    capture.convert()
