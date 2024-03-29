# Power Subsystem

## Function of the Subsystem
The function of the power subsystem is to recieve power from the docking station subsystem and distribute the power to the other subsytems. The power subsystem also has a battery monitoring system that will notify the main control subsystem when the battery charge fall below a certain threshold. 

## Specifications and Constraints

| No. | Specifications and Constraints | Origin | 
|-|-|-| 
| 1 | Shall have plugless charging | Supervisor: Dr. Van Neste 
| 2 | Shall have a ripple voltage tolerance of 250 mVpp | Raspberry PI3
| 3 | Shall follow proper wire gauging standards | NEC 310.16(b)
| 4 | Shall not operate below 15-20% of the battery capacity | Ethics

## Buildable Schematic 
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/power%20schematic.png)

The system will recieve power from a pair of metal docking contacts. The battery distributes power to the rest of the system through a fuse box. The fuse box provides overcurrent protection to reduce the risk of electrical damage to the AuR's components. Buck converters are added to step down the voltage from 18V to 12V and reduces the ripple voltage cause by the motors. A manual switch is added between the fuse box and motors to reduce the safety risk of the AuR. The manual switch allows a user to immediately stop the AuR from moving and causing potential physical harm. The OpenCR1 provides 5 Volts to the RaspberryPI3, LIDAR, ESP32, and speakerphone using a built in voltage divider on the OpenCR1. The DDS Module is a componenet part of safety subsystem's design. The DDS Module will provide 5V to the ultrasonic sensors and near field sensors. For further information on the circuit for the sensors, refer to the safey subsystem. 
The voltage sensor will measure the voltage of the battery and send that measurement to the Raspberry PI3 located in the Main Control System


## Analysis
### Operating Current
Here are the operating currents for each of the devices on the AuR. 
| Device              | <br>Max<br>Operating Current<br>(Amps) | Operating Voltage<br>(VDC) |
| ------------------- | -------------------------------------- | --------------------------- |
| Ultrasonic Sensor 1 | 0.008                                  | 5                           |
| Ultrasonic Sensor 2 | 0.008                                  | 5                           |
| Ultrasonic Sensor 3 | 0.008                                  | 5                           |
| Ultrasonic Sensor 4 | 0.008                                  | 5                           |
| Near Field Sensor   | 0.050                                  | 5                           |
| RaspberryPI3        | 2.000                                  | 5                           |
| LIDAR               | 0.400                                  | 5                           |
| ESP32               | 0.032                                  | 5                           |
| Speakerphone        | 1.500                                  | 5                           |
| Voltage Sensor      | 0.320                                  | 12                          |
| Motors              | 3.089                                  | 12                          |
| OpenCR1             | 0.130                                  | 12                          |

Using the equation below to transform current over converters and knowing that parallel currents sum up with each other, the total operating current can be calculated. 

$$\frac{I_p}{I_s} = \frac{N_s}{N_p}$$

$$I_s  = \text{secondary current (current on 5V)}$$

$$I_p = \text{primary current (current on 12V)}$$

$$N_s  = \text{secondary voltage (5V)}$$

$$N_p = \text{primary voltage (12V)}$$


$I_{s1} = 0.008 +0.008 +0.008 +0.008 +0.050 = 0.082 A$

$I_{p1} = I_{s1}(\frac{N_s}{N_p}) = 0.082(\frac{5}{12}) =  0.03412A$


$I_{s2} = 2.000 + 0.400+0.032+1.500 = 3.932  A$

$I_{p2} = I_{s2}(\frac{N_s}{N_p}) = 3.932(\frac{5}{12}) =  1.638A$


$I_M=\text{Motor Current} = 3.089A$

$I_{OCR}=\text{OpenCR1 Current} = 0.130A$

$I_{VS}=\text{Voltage Sensor Current} = 0.320A$


$\text{Total Max Operating Current} = I_M+I_{OCR}+I_{VS}+I_{p1}+I_{p2}$

$\text{Total Max Operating Current} = 3.089+0.130+0.320+0.03412+1.638$

$\text{Total Max Operating Current} = 5.212A$


Additionally, the converters are not perfectly efficient and has some loss. So, a 5% error is added to account for the converters' loss. 


$\text{Percent Error} = 0.05 * 5.212A = 0.261A$

After summing the current and performing the necessary calculations, the total operating current of the AuR is **5.212 ± 0.261A**. It is ideal for the AuR to be provided with about double the calculated operating to accomadate for future modifications and possible error. In conclusion, it is optimal for the battery to provide 10 Amps which is about double the calculated operating current.

### Ripple Voltage
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/ripple%20simulation%20v3.png)

The figure above shows the setup for simulating ripple voltage caused by the dc motor and how the designed filters reduce the noise caused by the motor. The goal of simulating the ripple voltage is to determine if the designed filters are able to keep the system within the constraint of having less than 250 mVpp for ripple voltage. The constraint is set at 250 mVpp due to the LIDAR and Raspberry PI3's max ripple tolerance of 5 ± 5\% V, which equates to 250 mVpp. So, the ripple voltage sent to components other than the dc motor must not exceed 250 mVpp to reduce risk of electrical damage. 

**Ripple Voltage Caused By Motor**
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/ripple%20motor%20v3.png)

To create the motor, an inductor with series resistance is connected to a IGBT to represent motors turning on and off. A flyback diode is added to the motor's circuit to remove the sudden voltage spike caused when an inductor's current is cutoff. As seen from the graph, the simulated ripple voltage created by the motor is about 300 mVpp. This ripple voltage is higher than the constraint of 250 mVpp, which means that filters will be necessary.

**Voltage Output of 12V/5V Voltage Regulator**
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/ripple%20voltage%20regulator%20v2.png)

The simulated ripple voltage outputted by the Voltage Regular is about 140 mVpp. Thus, the Voltage Regulator is able to keep the ripple voltage within the 250 mVpp constraint. So, no additional filters are necessary for the sensors.

**Voltage Output of OpenCR1 12V/5V Converter**
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/ripple%20OpenCr1%20v3.png)

The simulated ripple voltage outputted by the OpenCR1 Converter is about 41 mVpp. Thus, the OpenCR1 Converter is able to keep the ripple voltage within the 250 mVpp constraint. So, no additional filters will need to be added at the OpenCR1's output. 

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
| Buck Converters (2 pack)      | 1        | $16.99                | $16.99            |
|                               |          | Total Subsystem Cost: | $191.52           |

## References
“360 laser distance sensor LDS-01 (LIDAR),” _ROBOTIS_. [Online]. Available: https://www.robotis.us/360-laser-distance-sensor-lds-01-lidar/. [Accessed: 16-Feb-2023].

“Grove - ultrasonic distance sensor,” _Seeed Studio_, 29-Dec-2022. [Online]. Available: https://www.seeedstudio.com/Grove-Ultrasonic-Distance-Sensor.html. [Accessed: 16-Feb-2023].

“Raspberry pi 3 model B+.” [Online]. Available: https://static.raspberrypi.org/files/product-briefs/200206+Raspberry+Pi+3+Model+B+plus+Product+Brief+PRINT&DIGITAL.pdf. [Accessed: 16-Feb-2023].
