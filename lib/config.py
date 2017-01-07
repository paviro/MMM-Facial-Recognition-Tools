#!/usr/bin/python
# coding: utf8
"""MMM-Facial-Recognition - MagicMirror Module
Face Recognition training script config
The MIT License (MIT)

Copyright (c) 2016 Paul-Vincent Roll (MIT License)
Based on work by Tony DiCola (Copyright 2013) (MIT License)
"""
import inspect
import os
import platform

_platform = platform.system().lower()
path_to_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

if ('FACE_USERS' in os.environ):
    u = os.environ['FACE_USERS']
    users = u.split(',')
    print(users)
else:
    # NOTE: Substitute your own user names here. These are just
    # placeholders, and you will get errors if your training.xml file
    # has more than 10 user classes.
    users = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8", "User9", "User10"]
    print('Remember to set the name list environment variable FACE_USERS')

# Edit the values below to configure the training and usage of the
# face recognition box.
if ('FACE_ALGORITHM' in os.environ):
    RECOGNITION_ALGORITHM = int(os.environ['FACE_ALGORITHM'])
    print("Using FACE_ALGORITM: {0}".format(RECOGNITION_ALGORITHM))
    if RECOGNITION_ALGORITHM < 1 or RECOGNITION_ALGORITHM > 3:
        print("WARNING: face algorithm must be in the range 1-3")
        RECOGNITION_ALGORITHM = 1
        os._exit(1)
else:
    RECOGNITION_ALGORITHM = 1
    print("Using default FACE_ALGORITM: {0}".format(RECOGNITION_ALGORITHM))

# File to save and load face recognizer model.
TRAINING_FILE = 'training.xml'
TRAINING_DIR = './training_data/'

# Size (in pixels) to resize images for training and prediction.
# Don't change this unless you also change the size of the training images.
FACE_WIDTH = 92
FACE_HEIGHT = 112

# Face detection cascade classifier configuration.
# You don't need to modify this unless you know what you're doing.
# See: http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html
HAAR_FACES = 'lib/haarcascade_frontalface.xml'
HAAR_EYES = 'lib/haarcascade_eye.xml'
HAAR_SCALE_FACTOR = 1.3
HAAR_MIN_NEIGHBORS_FACE = 4     # 4 or 3 trainer and tester used different values.
HAAR_MIN_NEIGHBORS_EYES = 2
HAAR_MIN_SIZE_FACE = (30, 30)
HAAR_MIN_SIZE_EYES = (20, 20)

def get_camera():
    try:
        import picam
        capture = picam.OpenCVCapture()
        capture.start()
        return capture
    except Exception:
        import webcam
        return webcam.OpenCVCapture(device_id=0)
