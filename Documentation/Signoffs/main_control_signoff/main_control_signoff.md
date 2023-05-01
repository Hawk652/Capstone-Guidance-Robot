# Main Control Subsystem

## Functionality of the Subsystem
<img src="https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/main_control/Concept%20Block%20Diagram%20(revized).png" alt="Figure 1" width="500" style="display: block; margin-left: auto; margin-right: auto;"/>

The main control subsystem's function is to receive inputs from the AuR's other subsystems and use those inputs to determine the AuR's actions. The subsystem is responsible for navigation and pathfinding as well as connecting all of the subsystems together.

## Specifications and Constraints
| No. | Specifications and Constraints | Origin |
|-|-|-|
| 3 | Shall operate on one floor only | Supervisor: Dr. Van Neste |
| 6 | Shall not operate below 15-20% of the battery capacity | Ethics |

## Buildable Schematic
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/main_control/Main%20Conrtol%20Circuit%20Schematic_3.PNG)

## Analysis

### Flow Chart
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/main_control/Main%20control%20flowchart%20(1).png)

### Navigation
The main control will receive location data and route deviation data from the localization subsystem as well as locomotion data from the rotary encoder. This data will be used to build and update a map model of the building. The user input will be processed in conjunction with the localization data to construct a path from the AuR's location to its desired destination. This will take place using tools provided by the ROS2 OS.
### User Input/Output
The main control will receive an input from the user interface subsystem and process that input into a usable format. The processed data will be a destination which the main control will use for its pathfinding process. An output is generated based on the status of the AuR and sent to the user interface subsystem.
### Error Processing
The main control will receive inputs from the safety, localization, and power subsystems. It will compare these inputs to expected values and if there is a discrepancy, an error will be reported. The error or errors will then be processed and a course of action will be determined based on number of errors, error details, severity of errors, and other data provided to or processed by the main control subsystem.
### Power
The Raspberry Pi3 B+ is connected to 6 devices via the four usb ports with a usb expansion port as well as 8 devices via the GPIO pins. Current output for each of the four onboard usb ports is limited to 500mA meaning the maximum output for four ports together would be 2A, however total current draw from all usb ports is limited to 1.5A[1]. GPIO pins can safely draw 50mA meaning the maximum output for 8 pins togeter would be 400mA or 0.4A. A total current draw of 2A and a voltage of 5V results in a 10 Watt load, which is doubled in order to ensure adequate battery life. This means the power subsystem must provide 20 Watts to the Main Control subsystem.
### OS
The Raspberry Pi3 B+ will be running a version of ROS2 Foxy which is based on Ubuntu 20.04. While the specific hardware requirements are not listed, the version used is a custom image provided by Robotis explicitly for use with the Raspberry Pi 3 B+[2].

## BOM
| Item | Quantity | Price Per Item | Total Price |
|-|-|-|-|
| Raspberry Pi 3 B+ | 1 | $35 | Purchased |
| USB Hub | 1 | $7.99 | $7.99 |
| | | Total Subsystem Cost: | $7.99 |

# References
[1]“Raspberry Pi Documentation - Raspberry Pi hardware,” www.raspberrypi.com. https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#maximum-power-output (accessed Jan. 29, 2023).

[2]Y. Name, “ROBOTIS e-Manual,” ROBOTIS e-Manual. https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup

[3]“Raspberry Pi 3 Model B+.” [Online]. Available: https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-Model-Bplus-Product-Brief.pdf (Accessed: Nov. 20, 2022)
