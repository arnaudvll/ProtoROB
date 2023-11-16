import rclpy
from rclpy.node import Node
from dynamixel_sdk import *
from bluepy.btle import Peripheral, DefaultDelegate
import time
from threading import Thread  


class DynamixelControlBluetooth(Node):
    def __init__(self):
        super().__init__('dynamixel_control_bluetooth')

        # Set the serial port and baud rate
        port_name = '/dev/ttyACM0'  # Adjust the port name as needed
        baud_rate = 1000000

        # Set the Dynamixel motor ID
        motor_id = 2

        # Initialize the Dynamixel SDK
        packet_handler = PacketHandler(1.0)
        port_handler = PortHandler(port_name)
        port_handler.setBaudRate(baud_rate)



        # Example: Set motor to a specific position (e.g., 512)
        #goal_position = 1000

        # Write goal position to the motor

        # ADDR_CCW_ANGLE_LIMIT = 8
        # ADDR_CW_ANGLE_LIMIT = 6
        ADDR_MOVING_SPEED = 32
        ADDR_TORQUE_ENABLE = 24

        # 0 - 1024 sens anti horaire - Fermeture
        # 1024 - 2047 sens horaire - Ouverture

        # Rotate CW with power level 50%
        dxl_comm_result, dxl_error = packet_handler.write2ByteTxRx(port_handler, motor_id, ADDR_MOVING_SPEED, 2046)
        time.sleep(2)
        # Stop the motor
        dxl_comm_result, dxl_error = packet_handler.write2ByteTxRx(port_handler, motor_id, ADDR_MOVING_SPEED, 1024)
        
        # Wait before changing direction
        time.sleep(1)

        # Rotate CCW with power level 50%
        dxl_comm_result, dxl_error = packet_handler.write2ByteTxRx(port_handler, motor_id, ADDR_MOVING_SPEED, 1023)
        time.sleep(2)
        # Stop the motor
        dxl_comm_result, dxl_error = packet_handler.write2ByteTxRx(port_handler, motor_id, ADDR_MOVING_SPEED, 1024)


        time.sleep(5)
        dxl_comm_result, dxl_error = packet_handler.write1ByteTxRx(port_handler, motor_id, ADDR_TORQUE_ENABLE, 0)


        if dxl_comm_result != COMM_SUCCESS:
            self.get_logger().info(f"Error: {packet_handler.getTxRxResult(dxl_comm_result)}")

    def run(self):
        rclpy.spin(self)

def main(args=None):
    rclpy.init(args=args)
    node = DynamixelControlBluetooth()
    node.run()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

