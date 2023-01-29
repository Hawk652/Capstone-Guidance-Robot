# Main Control Subsystem

## Functionality of the Subsystem
<img src="https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/main_control/MainControlBlockDiagram.png" alt="Figure 1" width="500" style="display: block; margin-left: auto; margin-right: auto;"/>

The main control subsystem's function is to receive inputs from the AuR's other subsystems and use those inputs to determine the AuR's actions. The subsystem is responsible for navigation and pathfinding as well as connecting all of the subsystems together.

## Specifications and Constraints
| No. | Specifications and Constraints | Origin |
|-|-|-|
| 3 | Shall operate on one floor only | Supervisor: Dr. Van Neste |
| 6 | Shall not operate below 15-20% of the battery capacity | Ethics |

## Buildable Schematic
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/main_control/Main%20Conrtol%20Circuit%20Schematic.PNG)

## Analysis

### Flow Chart
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/main_control/Main%20control%20flowchart.png)

### Navigation
The main control will receive location data and route deviation data from the localization subsystem as well as locomotion data from the rotary encoder. This data will be used to build and update a map model of the building. The user input will be processed in conjunction with the localization data to construct a path from the AuR's location to its desired destination. This will take place using tools provided by the ROS2 OS.
### User Input/Output
The main control will receive an input from the user interface subsystem and process that input into a usable format. The processed data will be a destination which the main control will use for its pathfinding process. An output is generated based on the status of the AuR and sent to the user interface subsystem.
### Error Processing
The main control will receive inputs from the safety, localization, and power subsystems. It will compare these inputs to expected values and if there is a discrepancy, an error will be reported. The error or errors will then be processed and a course of action will be determined based on number of errors, error details, severity of errors, and other data provided to or processed by the main control subsystem.
### Power
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/main_control/Main%20Control%20Current%20Graph.PNG)

The Raspberry Pi 3 B receives 5V and 2.5A[1] from the power subsystem.

## BOM
| Item | Quantity | Price Per Item | Total Price |
|-|-|-|-|
| Raspberry Pi 3 B+ | 1 | $35 | Purchased |
| Jumper wires | 1 | $7 | $7 |
| | | Total Subsystem Cost: | $7 |

# References
[1]“Raspberry Pi 3 Model B+.” [Online]. Available: https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-Model-Bplus-Product-Brief.pdf (Accessed: Nov. 20, 2022)


