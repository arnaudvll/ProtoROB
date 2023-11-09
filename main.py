from Reconaissance_faciale.face_reconnaissance import init_known_faces, face_reco_process
import cv2


known_faces, known_names  = init_known_faces()

# Initialize some variables
face_locations = []
face_encodings = []

video_capture = cv2.VideoCapture(0)


while True:

    image = face_reco_process(video_capture, face_locations, face_encodings, known_faces, known_names)
    # Display the resulting image with detected faces
    cv2.imshow('Video', image)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
    


