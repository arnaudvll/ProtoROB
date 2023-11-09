# !/usr/bin/env python
'''
----------------------------------------------------------------------------
Facial Recognition Camera Class
----------------------------------------------------------------------------
Description: This Python class, 'Camera', is designed for facial recognition 
using OpenCV. It initializes a video capture device, loads known faces and 
names, and processes frames for facial recognition.
----------------------------------------------------------------------------
Author: Clément Poirié
Date: 9/11/2023
Version: 1.0
----------------------------------------------------------------------------
Usage:
- Make sure to have the 'face_recognition', 'cv2', and 'numpy' libraries
  installed.
- Set up a directory with known faces for recognition in the 'known_faces'
  directory.
- Run the script and it will display the video stream with recognized faces.
----------------------------------------------------------------------------
References:
- https://blog.miguelgrinberg.com/post/video-streaming-with-flask
'''

from time import time  
import cv2  
from Reconaissance_faciale.face_reconnaissance import init_known_faces, face_reco_process

class Camera(object):
    def __init__(self):
        # Initialize the camera object
        self.video = cv2.VideoCapture(0)  # Capture video from the default camera (the webcam)
        self.known_faces, self.known_names = init_known_faces()  # Load known faces and names for recognition 
        self.face_locations = []  # Initialize a list for storing face locations
        self.face_encodings = []  # Initialize an list for storing face encodings

    def __del__(self):
        # Destructor method to release the video capture device when the object is deleted
        self.video.release()

    def get_frame(self):
        # Method to capture and process a video frame for facial recognition

        # Call the face recognition process function with the current video frame
        image = face_reco_process(self.video, self.face_locations, self.face_encodings, self.known_faces, self.known_names)

        # Encode the processed image to JPEG format
        ret, jpeg = cv2.imencode('.jpg', image)
        # Convert the image to bytes and return for streaming
        return jpeg.tobytes()

