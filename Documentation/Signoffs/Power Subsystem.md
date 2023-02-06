# Power Subsystem

## Function of the Subsystem
The function of the power subsystem is to recieve power from the docking station subsystem and distribute the power to the other subsytems. The power subsystem also has a battery monitoring system that will notify the main control subsystem when the battery charge below a certain threshold. 

## Specifications and Constraints

| No. | Specifications and Constraints | Origin | 
|-|-|-| 
| 1 | Shall have plugless charging | Supervisor: Dr. Van Neste 
| 2 | Shall have a ripple voltage tolerance of 50 mVpp | Supervisor: Dr. Van Neste
| 3 | Shall follow proper wire gauging standards | NEC 310.16(b)
| 4 | Shall not operate below 15-20% of the battery capacity | Ethics

## Buildable Schematic 
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/power%20schematic%20v2.png)
The system will recieve power from a pair of metal docking contacts. The battery distributes power to the rest of the system through a fuse box. The fuse box provides overcurrent protection to reduce the risk of electrical damage to the AuR's components. A manual switch is added between the fuse box and motors to provide a safety feature to the AuR. The manual switch allows a user to immediately stop the AuR from moving and causing potential physical harm. The OpenCR1 provides 5 Volts to the RaspberryPI3, LIDAR, ESP32, and speakerphone using a built in voltage divider on the OpenCR1. The DDS Module is a componenet part of safety subsystem's design. The DDS Module will provide 5V to the ultrasonic sensors and near field sensors. For further information on the circuit for the sensors, refer to the safey subsystem. 


## Analysis
Since the components most vulnerable to ripple voltage are being fed 5V through an integratted filter, there should be no significant ripple voltage to harm the sensors, microcomputer, and other components of the AuR.

## BOM
| Item                          | Quantity | Price Per Item        | Total Price       |
| ----------------------------- | -------- | --------------------- | ----------------- |
| Li-PO Battery                 | 1        | $30.00                | Already Purchased |
| USB Cable                     | 2        | $6.00                 | Already Purchased |
| Li-Po Battery Extension Cable | 1        | $9.00                 | Already Purchased |
| Raspberry Pi 3 Power Cable    | 1        | $8.00                 | Already Purchased |
| Manual Swith                  | 1        | $6.00                 | $6.00             |
| 6 Way Fuse Block              | 1        | $12.00                | $12.00            |
| Metal Contacts                | 1        | $16.95                | $16.95            |
|                               |          | Total Subsystem Cost: | $34.95            |

