
# Safety Subsystem



#  Function of the Subsystem


 The safety Subsystem will be tasked with obstacle avoidance, a manual override, and utilizing the LIDAR’s mapping capabilities. The sensors and button will be attached to the top of  the robot, that way it can utilize “seeing” capabilities. The sensors will gather information within the range (0.5 meters) of  robot and send this information to the Arduino or Raspberry PI.  To ensure that there will be no obstacle undetected, the LIDAR and Proximity sensor, ultrasonic  will be utilized to ensure redundancy. When an obstacle is detected within the range by the proximity sensor, ultrasonic sensor and the LIDAR, the information will be transmitted to the Main Control subsystem.  The LIDAR will be using its mapping capabilities to determine if the robot is too close to walls, doors, and corners. The proximity sensor will be using a 360 obstacle avoidance technique to determine the location of the obstacle. The DDS module will take the signal from a crystal oscillator and use it as a clock to create a buffer output waveform at a specific frequency that is set by the onboard microcontroller.  The HC-SR04 Ultrasonic sensor will be using a range of  2cm - 400cm by using a non-contact form of measurement. 

#  Constraints
|     No. |Constraint  |  Origin  |
|-|-|-|
|1|  Shall have manual override (power will be cut from the motor)           |Supervisor:          Dr. Van Neste        |
|2          |Shall maintain a distance of 0.5 m from obstacles and people           |Broader Implication         |

#  Buildable schematic


![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/SubsystemBlockDiagram.png)

![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/SafetySubsystem.png)

|Component| Value| Unit|
|-|-|-|
|D1-D6   |1N4001|-|
|C1,C2,C3  |4.7|μF|
|R1,R2,R3| 1|kΩ|
|L1,L2,L3,L4,L5,L6, Choke L7,Choke L8 |300|μH|
|R4,R5,R6,R7,R8,R9 |2|kΩ|
|Feedback R10,R11,R12 |20|kΩ|

#   Analysis

The safety Subsystem (SubsystemBlockDiagram) is a schematic of how the safety subsystem will connect with one another and to the Main control subsystem. The main switch will be connecting directly to the Battery (12V) this will turn off everything in an event of an emergency. The DDS module runs off of the same voltage and will go through a DC/DC converter to reduce the voltage to be 5V.  Once the voltage as been converted to 5V the power of  the rest the Safety subsystem. The LIDAR, HC - SR04 Ultrasonic sensor, Proximity Sensor, and the Raspberry Pi will be all be connected  in parallel with one another. The LIDAR is further discussed in detail within the Localization subsystem. The HC - SR04 ultrasonic sensor is used to ensure that the robot will detect an object within a range of 2cm - 400cm. The output of the subsystem will be sent to the Raspberry Pi. The proximity sensor will be using three electric magnetic resonators to detect changes in the electric field. By using the electric field sensor it can detect objects in close proximity, therefore creating a collision avoidance sensor.  
  

#    BOM
|Item| Quantity| Price Per Item| Total Price
|-|-|-|-|
|DDS Module   |3|$50|$150 |        |
|HC­SR04 Ultrasonic Sensor  |1|$14.99| $14.99     |
|LDS-01(LIDAR)| 1 |$200|Already Purchased
|Copper Wire |1|$17| $ 17   |
|Raspberry Pi |1|$35 |Already Purchased  |

#    Reference

“Capacitive omnidirectional position sensor using a quarter wave resonator,” IEEE Xplore. [Online]. Available: https://ieeexplore.ieee.org/document/9827944. [Accessed: 21-Nov-2022]. 

“Data Sheet - SparkFun Electronics.” [Online]. Available: https://cdn.sparkfun.com/datasheets/Sensors/Proximity/apds9960.pdf. [Accessed: 22-Nov-2022]. 

HC-SR04 datasheet. [Online]. Available: https://datasheetspdf.com/pdf-file/1380136/ETC/HC-SR04/1. [Accessed: 21-Nov-2022]. 
