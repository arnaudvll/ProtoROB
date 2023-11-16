import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from reconnaissance_faciale.face_reconnaissance import FaceReconnaissance
import cv2


class FaceDetection(Node):
    def __init__(self):
        super().__init__('face_detection')

        # Souscription au topic de controle du mode de pilotage
        self.controlModeSubscription = self.create_subscription(
            String,
            'control_mode',
            self.controlModeChanged,
            10)
        self.controlModeSubscription

    def controlModeChanged(self, control_mode):
        if control_mode.data == 'camera':
            known_faces, known_names  = FaceReconnaissance.init_known_faces()

            # Initialize some variables
            face_locations = []
            face_encodings = []

            video_capture = cv2.VideoCapture(0)


            while True:
                image , state = FaceReconnaissance.face_reco_process(video_capture, face_locations, face_encodings, known_faces, known_names)

                if state == True:
                    break

                # Display the resulting image with detected faces
                cv2.imshow('Video', image)

                # Hit 'q' on the keyboard to quit!
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()

            self.publisher_ = self.create_publisher(String, 'manual_control', 10)
            self.publisher_.publish(String(data='openAndClose'))

        
def main(args=None):
    rclpy.init(args=args)
    face_detection = FaceDetection()

    rclpy.spin(face_detection)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    face_detection.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

