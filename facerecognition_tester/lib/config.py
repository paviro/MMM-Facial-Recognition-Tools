#!/usr/bin/python
# coding: utf8
"""MMM-Facial-Recognition - MagicMirror Module
Face Recognition Testing Script Config
The MIT License (MIT)

Copyright (c) 2016 Paul-Vincent Roll (MIT License)
Based on work by Tony DiCola (Copyright 2013) (MIT License)
"""
import inspect
import os
import platform

_platform = platform.system().lower()
path_to_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# NOTE: Substitute your own user names here. These are just placeholders, and you will get errors
# if your training.xml file has more than 10 user classes.
users = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8", "User9", "User10"]

if (users[0] == "User1"):
    print("Don't forget to customize the user name list in config.py")

# Edit the values below to configure the training and usage of the
# face recognition box.
RECOGNITION_ALGORITHM = 1
# force the use of a usb webcam on raspberry pi (on other platforms this is always true automatically)
useUSBCam = False

# Threshold for the confidence of a recognized face before it's considered a
# positive match.  Confidence values below this threshold will be considered
# a positive match because the lower the confidence value, or distance, the
# more confident the algorithm is that the face was correctly detected.
# Start with a value of 3000, but you might need to tweak this value down if
# you're getting too many false positives (incorrectly recognized faces), or up
# if too many false negatives (undetected faces).
# POSITIVE_THRESHOLD = 3500.0
if RECOGNITION_ALGORITHM == 1:
    POSITIVE_THRESHOLD = 80
elif RECOGNITION_ALGORITHM == 2:
    POSITIVE_THRESHOLD = 250
else:
    POSITIVE_THRESHOLD = 3000

# File to save and load face recognizer model.
TRAINING_FILE = path_to_file + '/training.xml'

# Size (in pixels) to resize images for training and prediction.
# Don't change this unless you also change the size of the training images.
FACE_WIDTH = 92
FACE_HEIGHT = 112

# Face detection cascade classifier configuration.
# You don't need to modify this unless you know what you're doing.
# See: http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html
HAAR_FACES = path_to_file + '/cascades/haarcascade_frontalface.xml'
HAAR_EYES = path_to_file + '/cascades/haarcascade_eye.xml'
HAAR_SCALE_FACTOR = 1.3
HAAR_MIN_NEIGHBORS_FACE = 3
HAAR_MIN_NEIGHBORS_EYES = 2
HAAR_MIN_SIZE_FACE = (30, 30)
HAAR_MIN_SIZE_EYES = (20, 20)


def get_camera():
    try:
        if useUSBCam:
            print("Force use of USBCam...")
            raise Exception()
        import picam
        print("Picam selected...")  # ausgewählt
        capture = picam.OpenCVCapture()
        capture.start()
        return capture
    except Exception:
        import webcam
        print("Webcam selected...")
        return webcam.OpenCVCapture(device_id=0)
