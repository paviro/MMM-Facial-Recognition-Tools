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

path_to_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# force the use of a usb webcam on raspberry pi (on other platforms this is always true automatically)
useUSBCam = False

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
HAAR_SCALE_FACTOR = 1.3
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE = (30, 30)


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
