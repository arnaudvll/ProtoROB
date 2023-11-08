# ----------------------------------------------------------------------------
# Facial Recognition using face recognition library
# ----------------------------------------------------------------------------
# Description: This script performs real-time facial recognition using the
# OpenCV and face_recognition libraries. It loads known faces from a directory,
# captures video from a webcam, and recognizes and labels detected faces in the
# video stream.
# ----------------------------------------------------------------------------
# Author: Clément Poirié
# Date: 24/10/2023
# Version: 1.0
# ----------------------------------------------------------------------------
# Usage:
# - Make sure to have the 'face_recognition', 'cv2', and 'numpy' libraries
#   installed.
# - Set up a directory with known faces for recognition in the 'known_faces'
#   directory.
# - Run the script and it will display the video stream with recognized faces.
# ----------------------------------------------------------------------------
# References:
# - https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py

import face_recognition
import cv2
import numpy as np
import os

# ----------------------------------------------------------------------------
# This function initializes a list of known faces and their corresponding names
# ----------------------------------------------------------------------------
# No parameters
# Returns the lists of known faces and their names

def init_known_faces():

    # Directory containing images of known faces
    KNOWN_FACES_DIR = 'Reconaissance_faciale/known_faces'

    # Initialize lists to store face encodings and corresponding names
    known_faces = []
    known_names = []

    # Iterate through subdirectories in the KNOWN_FACES_DIR directory
    for name in os.listdir(KNOWN_FACES_DIR):
        for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):

            # Load an image
            image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

            # Get the 128-dimensional face encoding
            encoding = face_recognition.face_encodings(image)[0]

            # Append encodings and names to their respective lists
            known_faces.append(encoding)
            known_names.append(name)

    return (known_faces, known_names)


# ----------------------------------------------------------------------------
# Function for real-time facial recognition processing
# ----------------------------------------------------------------------------
# 5 parameters
#   - video --> The video stream captured from the camera. It can be defined as:
#     video_capture = cv2.VideoCapture(0) to capture video from the default camera (index 0).
#   - face_locations --> A list that stores the locations of detected faces in a frame.
#     It can be defined as: face_locations = []
#   - face_encodings --> A list that holds the 128-dimensional face encodings of the detected faces.
#     These encodings are used to compare detected faces with known faces for recognition.
#     It can be defined as: face_encodings = []
#   - known_faces, known_names --> lists that contains the face encodings of known faces, and the names.
#     These parameters are init_known_faces function object
#     It can be defined as: known_faces, known_names  = init_known_faces()
# Void function no return

def face_reco_process(video, face_locations, face_encodings, known_faces, known_names):
    # Capture a frame from the video
    ret, frame = video.read()

    process_this_frame = True

    if process_this_frame:
        # Resize the frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])  # Convert to RGB format

        # Locate faces in the frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # Calculate encodings of detected faces
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []  # List of detected face names

        for face_encoding in face_encodings:
            # Compare encodings of detected faces with known faces
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"  # Default name if the face is not recognized

            # Calculate the "distance" between known and detected faces
            face_distances = face_recognition.face_distance(known_faces, face_encoding)
            best_match_index = np.argmin(face_distances)  # Select the closest match
            # Assign names to detected faces
            if matches[best_match_index]:
                name = known_names[best_match_index]  # Name of the recognized face
            face_names.append(name)

    process_this_frame = not process_this_frame  # Toggle the frame processing indicator for the next iteration

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Resize face locations to the original frame size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a bounding box around the face
        if name == "Unknown":
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)  # Red box for unrecognized faces
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Green box for recognized faces
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)  # Display the face's name

    # Display the resulting image with detected faces
    cv2.imshow('Video', frame)
