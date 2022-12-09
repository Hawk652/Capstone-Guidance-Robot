# User Interface Subsystem

## Functionality of the Subsystem
The user interface subsystem takes in voice input from the user and outputs audible feedback to the user. This subsystem will allow the user to input various commands to the AuR, such as "Go to room #" or "Stop". This subsystem will additionally notify the user when they have reached their destination or when an error has occurred. The user interface subsystem will be the primary means through which the user will interact with the AuR.

## Specifications and Constraints
| No. | Specifications and Constraints | Origin |
|-|-|-|
| 1 | Shall use voice assistant technology for user interface | Ethics |

## Buildable Schematic
![schematic](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/03a6a551ad9f161dd7dff29d745d47c6f72b98c4/Documentation/Images/user_interface_schematic.png)

The only wired connection to the user interface subsystem is the power connection. All data is transferred wirelessly.

## Mounting
![mount](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/03a6a551ad9f161dd7dff29d745d47c6f72b98c4/Documentation/Images/NestMiniMount.png)

The Google Nest Mini will be mounted to the AuR using the structure shown in the image above. The overall structure will be mounted using screws.

## Analysis

### Interface
The primary component of the user interface subsystem will be a commercially-available voice assistant. A voice assistant was chosen as the primary interface due to ease of user access. A touchscreen, the primary alternative to a voice assistant, would require the user to maneuver around a potentially moving robot in order to interface with it. This scenario would potentially be hazardous to a user, so the team has decided to implement a voice assistant instead. The voice assistant the team has chosen to use is a Google Nest Mini. This device was chosen due to its low price point, relatively low power draw, and local processing capabilities. The local processing capabilities allow the voice assistant to directly communicate with the AuR instead of using an external server as an intermediary [1].
The user interface subsystem will send users' voice commands to the main control system for realization.

### Power
![simulation](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/03a6a551ad9f161dd7dff29d745d47c6f72b98c4/Documentation/Images/user_interface_simulation.png)
The Google Nest Mini requires 1.8 A at a voltage of 5 V [2]. This will be supplied by the power subsystem.


## BOM
| Item | Quantity | Price Per Item | Total Price |
|-|-|-|-|
| Google Nest Mini | 1 | $50 | $50 |
| | | Total Subsystem Cost: | $50 |

## References

[1] Google, “Local fulfillment &nbsp;|&nbsp; actions on google smart home &nbsp;|&nbsp; google developers,” Google. [Online]. Available: https://developers.google.com/assistant/smarthome/concepts/local. [Accessed: 16-Nov-2022].

[2] Google, “Google Nest and home device specifications,” Google Nest Help. [Online]. Available: https://support.google.com/googlenest/answer/7072284. [Accessed: 16-Nov-2022]. 
