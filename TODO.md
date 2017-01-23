# TODO

## Python 3 support

* PARTIAL: run py2to3 conversion on code (mostly done. still some possible issues with raw_input() calls)

## opencv 3 support

* DONE (but untested) detect opencv version 2 or 3 and use appropriates  sub-modules [start with this patch](https://github.com/falgard/MMM-Facial-Recognition-Tools/commit/06b303190893e5e6dddf35bd1a67f88abb8683b6) 
* DONE harvest other changes from [falgard](https://github.com/falgard/MMM-Facial-Recognition-Tools/commits/master)

## capture.py and lib/capture.py

* check for multiple faces in image, warn.
* interactively pick wich face to use if there is more than one
* add command line support for batch processing directories of files
* normalize input image size somehow
* permute each training image (clockwise, CCW, resize)
* test normalizing resulting .pgm file sizes 

## facerecognition.py

* Save unrecognized faces and allow to batch add to training data
* INVESTIGATED: eliminate JPEG errors "Corrupt JPEG data: premature end of data segment" (error is deep in cv2 capture code possible)

## haarcascade

* DONE: improve face recognition with glasses (this didn't work)
* SKIP: improve face recognition of slightly tilted faces (requires training new HAARS Cascade)

## Meta-parameters

Need to test to find optimal meta-parameters for face matching.

* create regression test suite

