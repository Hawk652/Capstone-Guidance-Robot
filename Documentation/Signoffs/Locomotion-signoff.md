# Locomotion Subsystem
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/SamuelMandody-signoff-Locomotion/Documentation/Images/Locomotion.png)

## Function of the Subsystem
The locomotion subsystem will be tasked with propelling the AuR via the motor and providing local displacement and instantaneous velocity via the attached motor encoder. 


## Buildable Schematic
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/SamuelMandody-signoff-Locomotion/Documentation/Images/Locomotion_schematic.png)

The values for required voltage and resistive load used in the buildable schematic were derived from the specification documents for both the openCR1.0 and the DYNAMIXEL XM430-W210-R.

## Analysis
The motors each have a standby current of 40 mA and the model still needs to be simulated under load to determine the average current draw when in use. The motors are hooked up to the 12 V rail of the OpenCR1.0 board. The locomotion subsystem sends instantaneous velocity which is constantly being measured by the onboard motor encoders to the main control subsystem via UART connection. Once the data is processed by the main control subsystem and translated into location, appropriately timed electrical pulses are sent to the motors to move the AuR towards its destination.

## BOM
| Item | Quantity | Price Per Item | Total Price | 
|-|-|-|-| 
| DYNAMIXEL XM430-W210-R | 2 | $289.00 | Already Purchased |
| | | Total Subsystem Cost: | $578.00|

## References


