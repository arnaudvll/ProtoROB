import rclpy
from rclpy.node import Node
from dynamixel_sdk import *
import serial
from std_msgs.msg import String


class BluetoothReceiver(Node):
    def __init__(self):
        super().__init__('bluetooth_receiver')

        self.port_name_ser = '/dev/ttyUSB1'
        self.baud_rate_ser = 115200
        self.ser = serial.Serial(self.port_name_ser, self.baud_rate_ser, timeout=1)

        self.sensor_mode = False
        self.door_moving = False

        self.loop()
        
    
    def loop(self):
        print("En attente de Data ...")
        while(1):
            data = self.ser.readline().decode().strip()
            if data:
                print("DATA RECUE :", data)

                if self.sensor_mode == True and self.door_moving == False: 
                    if (int(data) < 200):
                        self.door_moving = True
                        self.publisher_ = self.create_publisher(String, 'manual_control', 10)
                        self.publisher_.publish(String(data='openAndClose'))
                        self.door_moving = False
                        self.sensor_mode = False
                    

                match str(data):
                    case "sensor":
                        self.sensor_mode = True
                    case 'camera':
                        self.publisher_ = self.create_publisher(String, 'control_mode', 10)
                        self.publisher_.publish(String(data='camera'))
                    case "open" : 
                        self.publisher_ = self.create_publisher(String, 'manual_control', 10)
                        self.publisher_.publish(String(data='open'))
                        self.sensor_mode = False
                    case "close":
                        self.publisher_ = self.create_publisher(String, 'manual_control', 10)
                        self.publisher_.publish(String(data='close'))
                        self.sensor_mode = False


def main(args=None):
    rclpy.init(args=args)
    bluetooth_receiver = BluetoothReceiver()

    rclpy.spin(bluetooth_receiver)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    bluetooth_receiver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

