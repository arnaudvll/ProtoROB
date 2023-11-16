import rclpy
from rclpy.node import Node
from dynamixel_sdk import *
import serial

class DynamixelControl(Node):
    def __init__(self):
        super().__init__('dynamixel_control')

        # Set the serial port and baud rate
        self.port_name = '/dev/ttyACM0'  # Adjust the port name as needed
        self.baud_rate = 1000000

        self.port_name_ser = '/dev/ttyUSB0'
        self.baud_rate_ser = 115200
        self.ser = serial.Serial(self.port_name_ser, self.baud_rate_ser, timeout=1)

        # Set the Dynamixel motor ID
        self.motor_id = 2

        # Initialize the Dynamixel SDK
        self.packet_handler = PacketHandler(1.0)
        self.port_handler = PortHandler(self.port_name)
        self.port_handler.setBaudRate(self.baud_rate)

        # ADDR_CCW_ANGLE_LIMIT = 8
        # ADDR_CW_ANGLE_LIMIT = 6
        self.ADDR_MOVING_SPEED = 32
        self.ADDR_TORQUE_ENABLE = 24

        self.sensor_mode = False
        self.door_moving = False
        print("En attente de Data ...")

        while(1):
            

            data = self.ser.readline().decode().strip()
            if data:
                print("DATA RECUE :", data)

                print("sensor_mode: ", self.sensor_mode)

                if self.sensor_mode == True and self.door_moving == False: 
                    print("data sensor", data)
                    if (int(data) < 200):
                        self.door_moving = True
                        self.openDoor()
                        self.closeDoor()
                        self.door_moving = False
                        self.sensor_mode = False
                    

                match str(data):
                    case "sensor":
                        self.sensor_mode = True
                    case "open" : 
                        self.openDoor()
                        self.sensor_mode = False
                    case "close":
                        self.closeDoor()
                        self.sensor_mode = False


    def stop_motor(self):
        # Arrêter le moteur lorsque la touche Espace est enfoncée
        dxl_comm_result, dxl_error = self.packet_handler.write2ByteTxRx(self.port_handler, self.motor_id, self.ADDR_MOVING_SPEED, 1024)
        # Attendre avant de changer de direction
        time.sleep(1)
        # Définir le moteur en mode CCW avec une puissance de 50%
        dxl_comm_result, dxl_error = self.packet_handler.write2ByteTxRx(self.port_handler, self.motor_id, self.ADDR_MOVING_SPEED, 1023)


    def openDoor(self):
        # Rotate CW with power level 50%
        dxl_comm_result, dxl_error = self.packet_handler.write2ByteTxRx(self.port_handler, self.motor_id, self.ADDR_MOVING_SPEED, 2046)
        # Bon timer est 23 secondes
        time.sleep(3)
        # Stop the motor
        dxl_comm_result, dxl_error = self.packet_handler.write2ByteTxRx(self.port_handler, self.motor_id, self.ADDR_MOVING_SPEED, 1024)
        # Wait before changing direction
        time.sleep(1)

        if dxl_comm_result != COMM_SUCCESS:
            self.get_logger().info(f"Error: {self.packet_handler.getTxRxResult(dxl_comm_result)}")


    def closeDoor(self):
        # Rotate CCW with power level 50%
        dxl_comm_result, dxl_error = self.packet_handler.write2ByteTxRx(self.port_handler, self.motor_id, self.ADDR_MOVING_SPEED, 1023)
        # Bon timer est 23 secondes
        time.sleep(3)
        # Stop the motor
        dxl_comm_result, dxl_error = self.packet_handler.write2ByteTxRx(self.port_handler, self.motor_id, self.ADDR_MOVING_SPEED, 1024)
        time.sleep(1)
        dxl_comm_result, dxl_error = self.packet_handler.write1ByteTxRx(self.port_handler, self.motor_id, self.ADDR_TORQUE_ENABLE, 0)

        if dxl_comm_result != COMM_SUCCESS:
            self.get_logger().info(f"Error: {self.packet_handler.getTxRxResult(dxl_comm_result)}")
        # 0 - 1024 sens anti horaire - Fermeture
        # 1024 - 2047 sens horaire - Ouverture


    def run(self):
        try:
            rclpy.spin(self)
        finally:
            # Assurez-vous de détruire le nœud avant de quitter
            self.destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = DynamixelControl()
    try:
        node.run()
    finally:
        # Assurez-vous de fermer correctement le contexte ROS
        rclpy.shutdown()

if __name__ == '__main__':
    main()

