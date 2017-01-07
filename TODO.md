# TODO

## capture.py and lib/capture.py

* check for multiple faces in image, warn.
* interactively pick wich face to use if there is more than one
* add command line support for batch processing directories of files
* normalize input image size somehow
* permute each training image (clockwise, CCW, resize)
* test normalizing resulting .pgm file sizes 

## facerecognition.py

* Save unrecognized faces and allow to batch add to training data
* eliminate JPEG errors "Corrupt JPEG data: premature end of data segment"

## haarcascade

* improve face recognition with glasses
* improve face recognition of slightly tilted faces

## Meta-parameters

Need to test to find optimal meta-parameters for face matching.

* create regression test suite

