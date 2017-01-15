#!/usr/bin/env python
# coding: utf8
"""MMM-Facial-Recognition - MagicMirror Module
Face Recognition Testing Script
The MIT License (MIT)

Copyright (c) 2016 Paul-Vincent Roll (MIT License)
Based on work by Tony DiCola (Copyright 2013) (MIT License)

Run this script to test your training data.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import cv2  # OpenCV Library
import lib.face as face
import lib.config as config
import time
import os

model = config.model(config.RECOGNITION_ALGORITHM, config.POSITIVE_THRESHOLD)

print('Loading training data...')
model.load("training.xml")
print('Training data loaded!')

camera = config.get_camera()

time.sleep(1)   # give the camera a second to warm up
while True:
    # camera video feed
    frame = camera.read()

    image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    faces = face.detect_faces(image)
    if faces is not None:
        for i in range(0, len(faces)):
            if faces[i] is None:
                continue
            x, y, w, h = faces[i]
            # x and y coordinates of the face
            x_face = x
            y_face = y
            if config.RECOGNITION_ALGORITHM == 1:
                crop = face.crop(image, x, y, w, h)
            else:
                crop = face.resize(face.crop(image, x, y, w, h))

            label, confidence = model.predict(crop)
            cv2.rectangle(frame, (x, y), (x + w, y + h), 255)
            cv2.putText(frame, str(h), (x + w, y + h + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            if (label != -1 and label != 0):
                # If person is close to the camera use smaller
                # POSITIVE_THRESHOLD
                if h > 190 and confidence < config.POSITIVE_THRESHOLD:
                    cv2.putText(frame,
                                config.users[label - 1],
                                (x - 3, y - 8),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.5,
                                (255, 255, 255),
                                1)
                    cv2.putText(frame,
                                str(confidence),
                                (x - 2, y + h + 15),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5,
                                (255, 255, 255),
                                1)
                    print('User:' + config.users[label - 1])
                elif h <= 190 and confidence < config.POSITIVE_THRESHOLD:
                    # If person is further away from the camera but
                    # POSITIVE_THRESHOLD is still under 40 assume it is
                    # the person
                    cv2.putText(frame, config.users[label - 1], (x - 3, y - 8),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 1)
                    cv2.putText(frame, str(confidence), (x - 2, y + h + 15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    print('User:' + config.users[label - 1])
                elif h < 190:
                    # If person is further away from the camera be a bit
                    # more generous with the POSITIVE_THRESHOLD and add a
                    # not sure statement
                    cv2.putText(frame, "Guess: " + config.users[label - 1],
                                (x - 3, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 255, 255), 1)
                    cv2.putText(frame, str(confidence), (x - 2, y + h + 15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    print('Guess:' + config.users[label - 1])
                else:
                    cv2.putText(frame, "Unknown", (x, y - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 1)
                    print('Unknown face')
            else:
                cv2.putText(frame, "Unknown", (x, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 1)
                print('Unknown face')

            if h > 250:
                # If person is close enough, mark the eyes
                eyes = face.detect_eyes(face.crop(image, x, y, w, h))
                for i in range(0, len(eyes)):
                    x, y, w, h = eyes[i]
                    cv2.rectangle(frame, (x + x_face, y + y_face - 30),
                                  (x + x_face + w + 10, y + y_face + h - 40),
                                  (94, 255, 0))
                    cv2.putText(frame, "Eye " + str(i),
                                (x + x_face, y + y_face - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 1)

    if ('DISPLAY' in os.environ):
        # Display Image
        cv2.imshow('Facial recognition', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('No windowing system, writing face.jpg image')
        cv2.imwrite('face.jpg', frame)
        camera.stop()
        break

# Release camera and close windows
camera.stop()
cv2.destroyAllWindows()
