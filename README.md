# Facial Recognition Door Project

## Project Description

We are a team of three students from CPE Lyon: Adrien Pouxviel, Arnaud Ville, and Clément Poirié. Our goal is to realize the prototype of a solution according to a predefined list of materials and instructions.

The list of elements to be used is as follows:

- Implementation of an ESP32
- Integration of a distance sensor
- Use of a dynamixel motor
- Programming with the ROS2 middleware
- Development of a mobile application

The allocated time for the completion of this project spanned over a period of 20 hours. Our approach is to create a door equipped with a facial recognition system, thus allowing exclusive access to authorized individuals. Facial recognition serves as the authentication mechanism necessary for unlocking the door. Additionally, we have incorporated features such as the presence detection opening mode and the opening mode via phone command.

## Features

- **Facial Recognition:** Implementation of a facial recognition algorithm aimed at accurately identifying authorized individuals.
- **Distance Sensor:** Integration of a sensor to determine the presence or absence of a person in front of the door.
- **IHR Mobile Application:** Design of a mobile application acting as a human-machine interface. It allows remote opening and closing of the door, streaming camera feed visualization, and modification of the opening mode between facial recognition and presence detection.

## Technologies Used

- **Programming Languages:** Python and Arduino
- **Middleware:** ROS2 Humble
- **Libraries:**
    - OpenCV for image capture and image processing.
    - face_recognition for facial detection and recognition.

- **Hardware:**
    - A camera
    - A PVC plate specifically resized for the door creation.
    - Custom hinges designed and printed by us using a 3D printer.
    - A VL53L0X-V2 distance sensor.
    - An Ax12 dynamixel motor.
    - Lego bricks


## Le système
![both barbie](Reconnaissance_faciale/data/system_schematic.png)

## Résultats