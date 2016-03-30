"""Raspberry Pi Face Recognition Treasure Box
Face Detection Helper Functions
Copyright 2013 Tony DiCola

Functions to help with the detection and cropping of faces.
"""

import cv2

import config

haar_faces = cv2.CascadeClassifier(config.HAAR_FACES)
eyeCascade = cv2.CascadeClassifier(config.HAAR_EYES)


def detect_face(image):
    """Return bounds (x, y, width, height) of detected face in grayscale image.
    If no face or more than one face are detected, None is returned.
    """
    faces = haar_faces.detectMultiScale(image, scaleFactor=config.HAAR_SCALE_FACTOR, minNeighbors=config.HAAR_MIN_NEIGHBORS_FACE, minSize=config.HAAR_MIN_SIZE_FACE, flags=cv2.CASCADE_SCALE_IMAGE)
    return faces


def detect_eyes(image):
    eyes = eyeCascade.detectMultiScale(image, scaleFactor=config.HAAR_SCALE_FACTOR, minNeighbors=config.HAAR_MIN_NEIGHBORS_EYES, minSize=config.HAAR_MIN_SIZE_EYES, flags=cv2.CASCADE_SCALE_IMAGE)

    return eyes


def crop(image, x, y, w, h):
    """Crop box defined by x, y (upper left corner) and w, h (width and height)
    to an image with the same aspect ratio as the face training data.  Might
    return a smaller crop if the box is near the edge of the image.
    """
    crop_height = int((config.FACE_HEIGHT / float(config.FACE_WIDTH)) * w)
    midy = y + h / 2
    y1 = max(0, midy - crop_height / 2)
    y2 = min(image.shape[0] - 1, midy + crop_height / 2)
    return image[y1:y2, x:x + w]


def resize(image):
    """Resize a face image to the proper size for training and detection.
    """
    return cv2.resize(image, (config.FACE_WIDTH, config.FACE_HEIGHT), interpolation=cv2.INTER_LANCZOS4)
