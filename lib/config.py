#!/usr/bin/env python
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
import cv2

(CV_MAJOR_VER, CV_MINOR_VER) = cv2.__version__.split(".")[:2]

_platform = platform.system().lower()
path_to_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

RECOGNITION_ALGORITHM = 1
POSITIVE_THRESHOLD = 80


def set_recognition_algorithm(algorithm):
    if algorithm < 1 or algorithm > 3:
        print("WARNING: face algorithm must be in the range 1-3")
        RECOGNITION_ALGORITHM = 1
        os._exit(1)
    RECOGNITION_ALGORITHM = algorithm
    # Threshold for the confidence of a recognized face before it's
    # considered a positive match.  Confidence values below this
    # threshold will be considered a positive match because the lower
    # the confidence value, or distance, the more confident the
    # algorithm is that the face was correctly detected.  Start with a
    # value of 3000, but you might need to tweak this value down if
    # you're getting too many false positives (incorrectly recognized
    # faces), or up if too many false negatives (undetected faces).
    # POSITIVE_THRESHOLD = 3500.0
    if RECOGNITION_ALGORITHM == 1:
        POSITIVE_THRESHOLD = 80
    elif RECOGNITION_ALGORITHM == 2:
        POSITIVE_THRESHOLD = 250
    else:
        POSITIVE_THRESHOLD = 3000


if ('FACE_USERS' in os.environ):
    u = os.environ['FACE_USERS']
    users = u.split(',')
    print(users)
else:
    # NOTE: Substitute your own user names here. These are just
    # placeholders, and you will get errors if your training.xml file
    # has more than 10 user classes.
    users = ["User1", "User2", "User3", "User4", "User5",
             "User6", "User7", "User8", "User9", "User10"]
    print('Remember to set the name list environment variable FACE_USERS')

# Edit the values below to configure the training and usage of the
# face recognition box.
if ('FACE_ALGORITHM' in os.environ):
    set_recognition_algorithm(int(os.environ['FACE_ALGORITHM']))
    print("Using FACE_ALGORITM: {0}".format(RECOGNITION_ALGORITHM))
else:
    set_recognition_algorithm(1)
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
#HAAR_FACES = 'lib/haarcascade_frontalface_alt.xml'
#HAAR_FACES = 'lib/haarcascade_frontalface_alt2.xml'
#HAAR_FACES = 'lib/haarcascade_frontalface_default.xml'
HAAR_FACES = 'lib/haarcascade_frontalface.xml'
HAAR_EYES = 'lib/haarcascade_eye.xml'
HAAR_SCALE_FACTOR = 1.05
HAAR_MIN_NEIGHBORS_FACE = 4     # 4 or 3 trainer/tester used different values.
HAAR_MIN_NEIGHBORS_EYES = 2
HAAR_MIN_SIZE_FACE = (30, 30)
HAAR_MIN_SIZE_EYES = (20, 20)


def get_camera(preview=True):
    try:
        from . import picam
        capture = picam.OpenCVCapture(preview)
        capture.start()
        return capture
    except Exception:
        from . import webcam
        return webcam.OpenCVCapture(device_id=0)


def is_cv2():
    if CV_MAJOR_VER == 2:
        return True
    else:
        return False


def is_cv3():
    if CV_MAJOR_VER == 3:
        return True
    else:
        return False


def model(algorithm, thresh):
    # set the choosen algorithm
    model = None
    if is_cv3():
        # OpenCV version renamed the face module
        if algorithm == 1:
            model = cv2.face.createLBPHFaceRecognizer(threshold=thresh)
        elif algorithm == 2:
            model = cv2.face.createFisherFaceRecognizer(threshold=thresh)
        elif algorithm == 3:
            model = cv2.face.createEigenFaceRecognizer(threshold=thresh)
        else:
            print("WARNING: face algorithm must be in the range 1-3")
            os._exit(1)
    else:
        if algorithm == 1:
            model = cv2.createLBPHFaceRecognizer(threshold=thresh)
        elif algorithm == 2:
            model = cv2.createFisherFaceRecognizer(threshold=thresh)
        elif algorithm == 3:
            model = cv2.createEigenFaceRecognizer(threshold=thresh)
        else:
            print("WARNING: face algorithm must be in the range 1-3")
            os._exit(1)
    return model


def user_label(i):
    """ Generate the user lable. Lables are 1 indexed.
    """
    i = i - 1
    if i < 0 or i > len(users):
        return "User" + str(int(i))
    return users[i]
