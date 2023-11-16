import time
import rclpy
from rclpy.node import Node
from dynamixel_sdk import *
from std_msgs.msg import String


class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')

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

        self.ADDR_MOVING_SPEED = 32
        self.ADDR_TORQUE_ENABLE = 24

        # Souscription au topic de controle du mode de pilotage
        self.controlModeSubscription = self.create_subscription(
            String,
            'control_mode',
            self.controlModeChanged,
            10)
        self.controlModeSubscription

        # Souscription au topic de controle manuel
        self.manualControlSubscription = self.create_subscription(
            String,
            'manual_control',
            self.manualControlReceived,
            10)
        self.manualControlSubscription 


    def controlModeChanged(self, control_mode):
        match control_mode.data:
            case 'sensor_mode':
                self.openDoor()
                self.closeDoor()
            case 'camera_mode':
                a = 1

    def manualControlReceived(self, manual_control):
        print("DATA RECUE :", manual_control)
        match manual_control.data:
            case 'open':
                self.openDoor()
            case 'close':
                self.closeDoor()

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


def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

