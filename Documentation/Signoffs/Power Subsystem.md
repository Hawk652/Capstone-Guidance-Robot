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
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/power%20schematic%20v3.png)

The system will recieve power from a pair of metal docking contacts. The battery distributes power to the rest of the system through a fuse box. The fuse box provides overcurrent protection to reduce the risk of electrical damage to the AuR's components. A manual switch is added between the fuse box and motors to provide a safety feature to the AuR. The manual switch allows a user to immediately stop the AuR from moving and causing potential physical harm. The OpenCR1 provides 5 Volts to the RaspberryPI3, LIDAR, ESP32, and speakerphone using a built in voltage divider on the OpenCR1. The DDS Module is a componenet part of safety subsystem's design. The DDS Module will provide 5V to the ultrasonic sensors and near field sensors. For further information on the circuit for the sensors, refer to the safey subsystem. 
The voltage sensor will measure the voltage of the battery and send that measurement to the Raspberry PI3 located in the Main Control System


## Analysis
### Operating Current
Here are the operating currents for each of the devices on the AuR. 
| Device              | Operating Current<br>(Amps) |
| ------------------- | --------------------------- |
| Ultrasonic Sensor 1 | 0.008                       |
| Ultrasonic Sensor 2 | 0.008                       |
| Ultrasonic Sensor 3 | 0.008                       |
| Ultrasonic Sensor 4 | 0.008                       |
| Near Field Sensor   | 0.050                       |
| Motors              | 3.089                       |
| OpenCR1             | 0.130                       |
| RaspberryPI3        | 2.000                       |
| LIDAR               | 0.400                       |
| ESP32               | 0.032                       |
| Speakerphone        | 1.500                       |
| Voltage Sensor      | 0.320                       |

Using the equation below to transform current over converters and knowing that parallel currents sum up with each other, the total operating current can be calculated. Additionally, the converters are not perfectly efficient and has some loss. So, a 5% error is added to account for the converters' loss. 

$(Is \div Ip) = (Np \div Ns)$

After summing the current and performing the necessary calculations, the total operating current of the AuR is 5.212 ± 0.261A. It is ideal for the AuR to be provided with about double the calculated operating to accomadate for future modifications and possible error. In conclusion, it is optimal for the battery to provide 10 Amps which is about double the calculated operating current.

### Ripple Voltage
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/ripple%20simulation.png)

The figure above demonstrates a simulation to determine the ripple voltage outputting from the converters. The motor is represented with the motor's resistance and a switch to replicate the motor turning on and off. The 12V/5V converter are the converters being used to provide 5V to some of the AuR's components. Only one converter will be neccessary to simulate the ripple voltage.

![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/ripple%20plot.png)

As seen from the plot, the ripple voltage coming out of the 12V/5V converter is less than 50mVpp. This then shows that the ripple voltage will not be high enough to damage the electrical components. 

## BOM
| Item                          | Quantity | Price Per Item        | Total Price       |
| ----------------------------- | -------- | --------------------- | ----------------- |
| Battery INR-26650-5S2P        | 1        | $135.00               | $135.00           |
| USB Cable                     | 2        | $6.00                 | Already Purchased |
| Li-Po Battery Extension Cable | 1        | $9.00                 | Already Purchased |
| Raspberry Pi 3 Power Cable    | 1        | $8.00                 | Already Purchased |
| Boat Rocker Switch            | 1        | $6.00                 | $5.99             |
| 6 Way Fuse Block              | 1        | $12.00                | $12.00            |
| Metal Contacts                | 1        | $16.95                | $16.95            |
| DIYmall Voltage Sensor        | 1        | $5.59                 | $5.59             |
|                               |          | Total Subsystem Cost: | $174.53           |

