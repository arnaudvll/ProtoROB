from time import time
import cv2
from Reconaissance_faciale.face_reconnaissance import init_known_faces, face_reco_process

class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.known_faces, self.known_names  = init_known_faces()
        self.face_locations = []
        self.face_encodings = []

    def __del__(self):
        self.video.release()

    def get_frame(self):

        image = face_reco_process(self.video, self.face_locations, self.face_encodings, self.known_faces, self.known_names)
        # success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
        # if success:
        #     ret, jpeg = cv2.imencode('.jpg', image)
        #     return jpeg.tobytes()
        # else:
        #     return None