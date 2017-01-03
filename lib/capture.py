"""MMM-Facial-Recognition - MagicMirror Module
Positive Image Capture Script
The MIT License (MIT)

Copyright (c) 2016 Paul-Vincent Roll (MIT License)
Based on work by Tony DiCola (Copyright 2013) (MIT License)

Run this script to capture positive images for training the face recognizer.
"""

import fnmatch
import glob
import os
import sys

import cv2

import config
import face


def is_letter_input(letter):
    input_char = raw_input()
    return input_char.lower()


def walk_files(directory, match='*'):
    """Generator function to iterate through all files in a directory recursively
    which match the given filename match parameter.
    """
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, match):
            yield os.path.join(root, filename)


def capture():
    camera = config.get_camera()
    # Create the directory for positive training images if it doesn't exist.
    if not os.path.exists(config.TRAINING_DIR + CAPTURE_DIR):
        os.makedirs(config.TRAINING_DIR + CAPTURE_DIR)
    # Find the largest ID of existing positive images.
    # Start new images after this ID value.
    files = sorted(glob.glob(os.path.join(config.TRAINING_DIR + CAPTURE_DIR, '[0-9][0-9][0-9].pgm')))
    count = 0
    if len(files) > 0:
        # Grab the count from the last filename.
        count = int(files[-1][-7:-4]) + 1
    print 'Capturing positive training images.'
    print 'Press enter to capture an image.'
    print 'Press Ctrl-C to quit.'
    while True:
        try:
            raw_input()
            print 'Capturing image...'
            image = camera.read()
            # Convert image to grayscale.
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            # Get coordinates of single face in captured image.
            result = face.detect_single(image)
            if result is None:
                print 'Could not detect single face!  Check the image in capture.pgm' \
                        ' to see what was captured and try again with only one face visible.'
                continue
            x, y, w, h = result
            # Crop image as close as possible to desired face aspect ratio.
            # Might be smaller if face is near edge of image.
            crop = face.crop(image, x, y, w, h)
            # Save image to file.
            filename = os.path.join(config.TRAINING_DIR + CAPTURE_DIR, '%03d.pgm' % count)
            cv2.imwrite(filename, crop)
            print 'Found face and wrote training image', filename
            count += 1
        except KeyboardInterrupt:
            camera.stop()
            break


def convert():
    # Create the directory for positive training images if it doesn't exist.
    if not os.path.exists(config.TRAINING_DIR + CAPTURE_DIR):
        os.makedirs(config.TRAINING_DIR + CAPTURE_DIR)
    # Find the largest ID of existing positive images.
    # Start new images after this ID value.
    files = sorted(glob.glob(os.path.join(config.TRAINING_DIR + CAPTURE_DIR, '[0-9][0-9][0-9].pgm')))
    count = 0
    if len(files) > 0:
        # Grab the count from the last filename.
        count = int(files[-1][-7:-4]) + 1
    for filename in walk_files(RAW_DIR, '*.jpg'):
        image = filename
        image = cv2.imread(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # Get coordinates of single face in captured image.
        result = face.detect_single(image)
        if result is None:
            print 'Could not detect single face!'
            continue
        x, y, w, h = result
        # Crop image as close as possible to desired face aspect ratio.
        # Might be smaller if face is near edge of image.
        crop = face.crop(image, x, y, w, h)
        # Save image to file.
        filename = os.path.join(config.TRAINING_DIR + CAPTURE_DIR, '%03d.pgm' % count)
        cv2.imwrite(filename, crop)
        print 'Found face and wrote training image', filename
        count += 1
