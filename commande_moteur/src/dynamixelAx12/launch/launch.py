from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='dynamixelAx12',
            executable='bluetooth_receiver',
            name='bluetooth_receiver'
        ),
        Node(
            package='dynamixelAx12',
            executable='face_detection',
            name='face_detection'
        ),
        Node(
            package='dynamixelAx12',
            executable='motor_controller',
            name='motor_controller'
        ),
    ])