# coding: utf8
"""PaViRO MagicMirror-Extensions - Face recognition
Face Recognition Testing Script
Copyright 2015 Paul-Vincent Roll
Based on work by Tony DiCola (Copyright 2013)

Run this script to test your training data.
"""
import cv2  # OpenCV Library
import lib.face as face
import lib.config as config

# Load training data into model
print('Loading training data...')

if config.RECOGNITION_ALGORITHM == 1:
    print "ALGORITHM: LBPH"
    model = cv2.createLBPHFaceRecognizer(threshold=config.POSITIVE_THRESHOLD)
elif config.RECOGNITION_ALGORITHM == 2:
    print "ALGORITHM: Fisher"
    model = cv2.createFisherFaceRecognizer(threshold=config.POSITIVE_THRESHOLD)
else:
    print "ALGORITHM: Eigen"
    model = cv2.createEigenFaceRecognizer(threshold=config.POSITIVE_THRESHOLD)

model.load("training.xml")
print('Training data loaded!')

capture = cv2.VideoCapture(0)

while True:
    # Capture video feed
    ret, frame = capture.read()
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    faces = face.detect_face(image)
    if faces is not None:
        for i in range(0, len(faces)):
            x, y, w, h = faces[i]
            # x und y cordinaten des Gesichts speichern um ausschnittsabsuchungen wieder zu normalisieren
            x_face = x
            y_face = y
            if config.RECOGNITION_ALGORITHM == 1:
                crop = face.crop(image, x, y, w, h)
            else:
                crop = face.resize(face.crop(image, x, y, w, h))

            label, confidence = model.predict(crop)
            cv2.rectangle(frame, (x, y), (x + w, y + h), 255)
            cv2.putText(frame, str(h), (x + w, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            if (label != -1):
                # If person is close to the camera use smaller POSITIVE_THRESHOLD
                if h > 190 and confidence < config.POSITIVE_THRESHOLD:
                    cv2.putText(frame, config.personen[label - 1], (x - 3, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 1)
                    cv2.putText(frame, str(confidence), (x - 2, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                # If person is further away from the camera but POSITIVE_THRESHOLD is still under 40 assume it is the person
                elif h < 190 and confidence < config.POSITIVE_THRESHOLD:
                    cv2.putText(frame, config.personen[label - 1], (x - 3, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 1)
                    cv2.putText(frame, str(confidence), (x - 2, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                # If person is further away from the camera be a bit more generous with the POSITIVE_THRESHOLD and add a not sure statement
                elif h < 190:
                    cv2.putText(frame, "Vermute: " + config.personen[label - 1], (x - 3, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
                    cv2.putText(frame, str(confidence), (x - 2, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                else:
                    cv2.putText(frame, "Unbekannt", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 1)

            else:
                cv2.putText(frame, "Unbekannt", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 1)

            # If person is close enough
            if h > 250:
                eyes = face.detect_eyes(face.crop(image, x, y, w, h))
                for i in range(0, len(eyes)):
                    x, y, w, h = eyes[i]
                    cv2.rectangle(frame, (x + x_face, y + y_face - 30), (x + x_face + w + 10, y + y_face + h - 40), (94, 255, 0))
                    cv2.putText(frame, "Auge " + str(i), (x + x_face, y + y_face - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Display Image
    cv2.imshow('Facial recognition', frame)

    # exit by pressing q
    if cv2.waitKey(1) == ord('q'):
        break

# Release capture and close windows
capture.release()
cv2.destroyAllWindows()
