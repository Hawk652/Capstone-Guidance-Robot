# User Interface Subsystem

## Functionality of the Subsystem
The user interface subsystem takes in voice input from the user and outputs audible feedback to the user. This subsystem will allow the user to input various commands to the AuR, such as "Go to room #" or "Stop". This subsystem will additionally notify the user when they have reached their destination or when an error has occurred. The user interface subsystem will be the primary means through which the user will interact with the AuR.

## Specifications and Constraints
| No. | Specifications and Constraints | Origin |
|-|-|-|
| 1 | Shall use voice assistant technology for user interface | Ethics |

## Buildable Schematic
![schematic](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/03a6a551ad9f161dd7dff29d745d47c6f72b98c4/Documentation/Images/user_interface_schematic.png)

The only hardware components of the user interface are the combination microphone and speaker. These will be connected via USB to the main control subsystem's Raspberry Pi. Both power and data with be transferred over this USB connection.

## Mounting
![dimensions](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/JacobWilkinson-signoff-userinterface/Documentation/Images/user_interface_speaker_dimensions.png?raw=true)

The microphone and speaker will be mounted to the AuR using a 3d-printed mount. The above image shows the dimensions of the device.

## Analysis

### Interface
The primary hardware component of the user interface subsystem will be a a conference microphone and speaker combination. This device will connect to the main control's raspberry pi, which will run Rhasspy, a voice assistant. Rhasspy was chosen because of its open source nature, configurability, and local processing capabilities [1]. We chose to use a voice assistant instead of another interface due to ease of user access. A touchscreen, the primary alternative to a voice assistant, would require the user to maneuver around a potentially moving robot in order to interface with it. This scenario would potentially be hazardous to a user, so the team has decided to implement a voice assistant instead.

### Power
The microphone and speaker are powered over a single usb type A connection. Unfortunately no documentation on the exact power specifications of the microphone and speaker were available, but the USB standard defines a voltage of 5 volts and a maximum current of 0.5 amps.

## BOM
| Item | Quantity | Price Per Item | Total Price |
|-|-|-|-|
| USB Speakerphone Microphone | 1 | $42.99 | $42.99 |
| | | Total Subsystem Cost: | $42.99 |

## References

[1] Rhasspy, “Rhasspy Documentation” Rhasspy Documentation. [Online]. Available: https://rhasspy.readthedocs.io/en/latest/. [Accessed: 01-Feb-2023].