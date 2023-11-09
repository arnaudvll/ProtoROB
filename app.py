# !/usr/bin/env python
'''
----------------------------------------------------------------------------
Flask Video Streaming App
----------------------------------------------------------------------------
Description: This Python script utilizes the Flask framework to create a video 
streaming application.
It includes routes for rendering an HTML template at the root URL and streaming video frames
via the '/video_feed' endpoint. The 'gen' function generates a continuous stream of video frames
using the 'Camera' class from the 'init_camera.camera' module, and the OpenCV library is employed
for video processing.
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


from flask import Flask, render_template, Response
from init_camera.camera import Camera
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    # Define a route. When someone accesses the root URL '/',
    # it triggers the 'index' function, which renders an HTML template called 'index.html'.
    return render_template('index.html')

def gen(camera):
    # Define a generator function. It continuously yields frames from the camera.
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    # Another route definition. When someone accesses '/video_feed',
    # it triggers the 'video_feed' function, which returns a Flask Response object.
    # This response uses the generator function 'gen(Camera())' to continuously stream video frames.
    # The MIME type is set to 'multipart/x-mixed-replace' for streaming.
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)