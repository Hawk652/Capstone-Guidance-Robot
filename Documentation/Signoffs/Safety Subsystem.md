
# Safety Subsystem

![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/finalfinal_finalsafetyblockonly%20(5).jpeg)

#  Function of the Subsystem


 The safety Subsystem will be tasked with obstacle avoidance, a manual override, and utilizing the LIDAR’s mapping capabilities. The sensors and button will be attached to the top of  the robot, that way it can utilize “seeing” capabilities. The sensors will gather information within the range (0.5 meters) of  robot and send this information to the Arduino or Raspberry PI.  To ensure that there will be no obstacle undetected, the LIDAR and Proximity sensor, ultrasonic  will be utilized to ensure redundancy. When an obstacle is detected within the range by the proximity sensor, ultrasonic sensor and the LIDAR, the information will be transmitted to the Main Control subsystem.  The LIDAR will be using its mapping capabilities to determine if the robot is too close to walls, doors, and corners. The proximity sensor will be using a 360 obstacle avoidance technique to determine the location of the obstacle. The DDS module will take the signal from a crystal oscillator and use it as a clock to create a buffer output waveform at a specific frequency that is set by the onboard microcontroller.  The Grove - Ultrasonic Distance Sensor will be using a range of  3cm - 350cm by using a non-contact form of measurement. 

#  Constraints
|     No. |Constraint  |  Origin  |
|-|-|-|
|1|  Shall have manual override (power will be cut from the motor)           |Supervisor:          Dr. Van Neste        |
|2          |Shall maintain a distance of 0.5 m from obstacles and people           |Broader Implication         |

#  Buildable Schematics
##  Subsytsem Schematic

![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/finalfinalschematicblock.png)
 

This schematic illustrates all the components that will be interacting with one another in this system. Each of these sections will be covered throughout this document. 

## Pinout of the Subsystem
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/finalpinoutschematic.png)
##  Near Field Sensor (Proximity Sensor)
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/2coilsschematicimage.jpg)
The Proximity Sensor will be the main safety sensor for this subsystem. This sensor will be able to detect objects in an omnidirectional field of view. This sensor will be accomplished by the implementation of coils. By using their electric fields, the sensors will be able to detect very small changes in their distance. Below are the specific values that will be used for each component and are necessary for the sensor to function properly. These specific values have been researched in “Capacitive omnidirectional position sensor using a quarter wave resonator,” and discussed with Dr. Van Neste to ensure that these should be correct. 

### Table of Components 
|Component| Value| Unit|
|-|-|-|
|D1-D4   |1N4001|-|
|C1,C2  |4.7|μF|
|R1,R2| 1|kΩ|
|L1,L2,L3 |300|μH|
|R4,R5 |2|kΩ|
|R6,R7 |20|kΩ|

## Image of PCB 
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/2coilschematic.png)

front side
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/2coilschematicback.png)

back side

### 3d Model of Attachement to Robot
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/CoilBracketMount.png)

### Reasoning for Proximity Sensor
After extensive research and discussions with Dr. Van Neste, this sensor seemed to be the best for the Autonomous Guidance Robot. Currently, there are not any sensors on the market that would be within the price range of this project. The best option was to build an omnidirectional sensor with the help of Dr. Van Neste. This sensor will enable the robot to detect any obstacles or people that might stand in the way of the robot and be able to avoid the detections that have been obtained. 

#  Ultrasonic Sensor
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/Grove-Ultrasonic-Distance-Sensor-pinoutFinal.jpg)

The Grove - Ultrasonic Distance Sensor will be implented as the ultrasonic sensor for this subsystem.This item will be a backup sensor for the Proximity sensor. 

![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/trasnmitterimageofHC_SR04.jpg)

The reasoning for this is because the Proximity sensor will have a better range and has a radial sensing method than the ultrasonic sensor. The ultrasonic sensor determines an object's distance by sending a form of sonar waves out and determines the distance from the receiving signal that reflects off of an object that is within the range of the sensor, which is 3cm to 350cm. 

## Pinout of Ultrasonic Sensor
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/safety/Grover_Ranger_pinout.png)

|Component| Value| Unit|
|-|-|-|
|Operating Voltage|DC 3.2~5.2V|-|
|Operating Current |8|mA|
|Operating Frequency| 40|KHz|
|Min Range |3 |cm|
|Max Range |350|cm|
|Accuracy|2|mm|
|Measuring Angle |<15|°|
|Dimmension|50 x25 x16|mm|
 
# DDS Module 
The DDS module is going to create a sinusoidal wave to get the coil to resonate. This module will generate a sine waveform then this signal will be sent to the coil.

# LIDAR
The LIDAR component will be implemented for the robot's safety and surroundings. The LIDAR will determine where the walls, corners, and doors are. The robot will be aware of the floor layout and will be able to differentiate obstacles compared to structures. The details on how this device works and how it will be implemented in the rest of the system will be in the Localization Subsystem.

# Raspberry Pi
The brain of the robot will be the Rasperry Pi. This means that all of the components in this subsystem will send all of their information back to the Raspberry Pi. The details on how this device works and how it will be implemented in the rest of the system will be in the Main Control Subsystem.

# Main Switch

The main switch's functionality will be to quickly cut off power to the robot for emergency purposes. This switch wil be located on the outside of the robot that way the robot can be shut off manually. The switch will be discussed further in the Power Subsystem.

#   Analysis


The safety Subsystem (SubsystemBlockDiagram) is a schematic of how the subsystem will connect with one another and to the Main control subsystem. The main switch will be connecting directly to the Battery (12V), this will turn off everything in an event of an emergency. The DDS module runs off of the same voltage and will go through a DC/DC converter to reduce the voltage to be 5V.  Once the voltage as been converted to 5V the power of  the rest the Safety subsystem. The LIDAR,
Grove - Ultrasonic Distance Sensor, Proximity Sensor, and the Raspberry Pi will be all be connected  in parallel with one another. The LIDAR is further discussed in detail within the Localization subsystem. The Grove - Ultrasonic Distance Sensor is used to ensure that the robot will detect an object within a range of 3cm - 350cm. The output of the subsystem will be sent to the Raspberry Pi. The proximity sensor will be using three electric magnetic resonators to detect changes in the electric field. By using the electric field sensor it can detect objects in close proximity, therefore creating a collision avoidance sensor.  
  

#    BOM
|Item| Quantity| Price Per Item| Total Price
|-|-|-|-|
|DDS Module   |4|$50|$200 |        |
|Grove - Ultrasonic Distance Sensor  |4|$3.95| $15.80    |
|LDS-01(LIDAR)| 1 |$200|Already Purchased
|Copper Wire |1|$54.82| $ 54.82   |
|Raspberry Pi |1|$35 |Already Purchased  |
|Total Price|||$270.62|
#    Reference

“Capacitive omnidirectional position sensor using a quarter wave resonator,” IEEE Xplore. [Online]. Available: https://ieeexplore.ieee.org/document/9827944. [Accessed: 21-Nov-2022]. 

“Data Sheet - SparkFun Electronics.” [Online]. Available: https://cdn.sparkfun.com/datasheets/Sensors/Proximity/apds9960.pdf. [Accessed: 22-Nov-2022]. 

“Grove - ultrasonic distance sensor,” Seeed Studio, 29-Dec-2022. [Online]. Available: https://www.seeedstudio.com/Grove-Ultrasonic-Distance-Sensor.html. [Accessed: 03-Feb-2023]. 


