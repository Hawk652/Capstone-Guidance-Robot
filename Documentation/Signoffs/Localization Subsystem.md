# Localization Subsystem
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/localization_block_diagram.png)
## Function of the Subsystem
The localization subsystem (Fig. 1) will be tasked with gathering and processing positional data points from sensors. The sensors shall all be mounted onboard the Turtlebot 3. The sensors that will gather data for this subsystem will be the LIDAR and the ESP32UWB DW3000. The LIDAR will gather data points from all reflective surfaces around it for the SLAM algorithm to determine the AuR's current location. The UWB (Ultra Wideband) module will determine the distance between itself and 2 other UWB modules using triangulation. The other 2 UWB modules will serve as a destination marker. Using all the prior mentioned data, the AuR will be able to determine its current location. The AuR will use the updated current position data along with the route data generated from the navigation subsystem to determine the deviation of the route. 

## Specifications and Constraints

| No. | Specifications and Constraints | Origin | 
|-|-|-| 
| 1 | Shall guide users to within 1 m of their desired room | Supervisor: Dr. Van Neste 
| 2 | Shall not deviate from the expected path by more than 15 cm | Broader Implication
| 3 | Shall detect the AuR's position to a precision of 15cm | Customer: Dr. Andy Pardue

## Buildable Schematic
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/localization%20circuit%20schematic.png)

The values for required voltage and resistive load used in Fig. 2. were derived from the specification documents for the individual components.

![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/capstonelocalizationkicad.jpg)
The image shows the connections between the components of the localization subsystem.

### Beacon
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/localization%20beacon%20schematic.png)

The schematic only consists of power connections since all the data will be transmitted wirelessly to the main ESP32UWB DW3000 on the AuR. The beacon will have a onboard program that will continuosly verify the location of the AuR in near real time.

![Alt text](https://cdn.discordapp.com/attachments/698697460444299284/1048409944107532360/ESP32_UWB_DW3000.png)

Dimensions are approximate. We were unable to find precise dimensions directly from the manufacturer, so we estimated them from the manufacturer-provided PCB schematic.

![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/localization%20beacon%20box%20lid.png)

![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/localization%20beacon%20box.png)

Here are the 3d models for the housing unit of the beacons. The dimensions of the housing unit is 19.3 x 8.15 x 7.62 $cm^3$. The housing unit will contain a breadboard, a 9v battery, a 9v to 5v dc to dc converter, and an ESP32 UWB development board.

![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/localization%20beacon%20placement.png)

The figure shows the beacons will be placed a little above the door frames in hallways. The beacons will be about 2 m from the floor. The housing units for the beacons will be attached to the wall using command strips. 

### Code Flowchart
![Flowchart](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/flowchart_localization.png)

The above figure is a flowchart showing the general functionality of this subsystem's software. When the AuR is turned on, the localization subsystem initializes itself and validates that all components are responsive. Once it has done this, it waits for a localization request from the main control. When a localization request is receieved, the localization subsystem estimates the AuR's position using the LIDAR and a SLAM, Simultaneous Localization And Mapping, algorithm. Once this is complete, the subsystem finds the RSSI, the Received Signal Strength Indicator, of nearby ultra-wideband beacons in order to triangulate its position in relation to those beacons. Once both localization methods are complete, the localization subsystem will compare the two results. If the results disagree, the localization subsystem will recheck its position using both method. Once both results agree, the localization subsystem will send the location data back to the main control and wait until another request is received.

## Analysis


### UWB  Beacons:
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/Trilateration.png)

A UWB beacon-based solution was chosen for higher resolution localization since it is accurate to within 15 cm which aids the constraints of being within 15 cm of its path and within 1 m of its destination [1]. The UWB beacons will be ESP32 UWB DW3000 modules.

Trilateration can be used to find the coordinates of an object based on its distance relative to three beacons [2]:

$(x- x_{1})^{2}+(y- y_{1})^{2} = r_{1}{}^{2}$

$(x- x_{2})^{2}+(y- y_{2})^{2} = r_{2}{}^{2}$

$(x- x_{3})^{2}+(y- y_{3})^{2} = r_{3}{}^{2}$

In order to find the distance from the device to a given beacon this Two Way Ranging(TWR) equation is used, where c is the speed of light d is the distance from the given beacon, RR is the Received Response time, Poll Sent time, SR is the Sent Response time, RP is the Received Poll time, RF is the Received Final time, SF is the Sent Final time and ToF is the Time of Flight [3]:

$ToF=\frac{(RR-SP)-(SR-RP) +(RF-SR)-(SF-RR)}{4}$

These equations work by calculating the time between messages and using the speed of light to determine the distance between beacons. The coordinates are calculated by the ESP32 and sent from the ESP32 to the Raspberry PI via a wired connection using I2C protocol.

Based on the tests performed and documented by the articles "Performance Comparison between Decawave DW1000 and DW3000 in low-power double side ranging applications"[4] and “Design of  localization System Based on Ultra-Wideband and Long Range Wire-less,”[5] we can meet the constraint of having less than 15 cm of horizontal error. The DW3000 can be configured to operate on a range of channels which refer to the device's operating frequency and bandwidth. An error of 15 cm was achieved with the DW3000's channel 9 configuration. Channel 9 was chosen for its higher frequency which encounters less environmental interference and can therefore provide more acurate measurements when compared to other channels. Channel 9 has a frequency of 7987.2 MHz and a bandwidth of 499.2 MHz[6].

From the system of equations which define trilateration the following can be derived[7]:

$\Delta = x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)$

$Ex = {1\over2\Delta}(y_3 - y_2)(2r_1e_1 + e_1^2 - 2r_3e_3 - e_3^2) - {1\over2\Delta}(y_3 - y_1)(2r_2e_2 + e_2^2-2r_3e_3 - e_3^2)$

$Ey = -{1\over2\Delta}(x_3 - x_2)(2r_1e_1 + e_1^2 - 2r_3e_3 - e_3^2) + {1\over2\Delta}(x_3 - x_1)(2r_2e_2 + e_2^2-2r_3e_3 - e_3^2)$

where $E_x$ and $E_y$ are the horizontal and vertical error of the hallway, $e_i$ is the distance error of the respective beacon, $r_i$ is the distance of the Aur from the respective beacon, and $x_i$ and $y_i$ are the horizontal and vertical coordinates assigned to the respective beacons. Since all distance errors are equal the equations can be simplified to:

$Ex = {1\over2\Delta}(y_3 - y_2)*2e(r_1 - r_3) - {1\over2\Delta}(y_3 - y_1)*2e(r_2 - r_3)$

$Ey = -{1\over2\Delta}(x_3 - x_2)*2e(r_1 - r_3) + {1\over2\Delta}(x_3 - x_1)*2e(r_2 - r_3)$

where $e$ is the $\pm10cm$ distance error provided in the data sheet[6]. Using the equations for $E_x$ and $E_y$ it is possible to find the totally error by using the equation:

$Total \ Error=\sqrt{E_x^2+E_y^2}$

After measuring a width of $238cm$ for the test area in Brown hall the following scenario was setup in Matlab: one beacon placed on one wall designated with coordinates of (0,0) and two beacons on the opposite wall with coordinates of (-243,-238) and (243,-238), approximately 16 feet apart. 100000 random coordinates were generated within the x range of [-243,243] and within the y range of [0,-238]. After using the generated coordinates to calculate the theoretical $r_i$ values, the equations mentioned were applied to these coordinates and the max error of the simulation was found as $~14.3cm$ which satisfies the constraint of localization within a precision of $15cm$

[The Matlab code used](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Software/Error_Calculations.m)

### Turtlebot:

#### LIDAR:
LIDAR sensors collect depth information about the environment using a laser. A laser is pulsed from the sensor and photons are reflected back to the sensor [8]. This allows the sensor to know the distance between itself and the surface from which the photons were reflected. The sensor spins and collects many points in order to gather depth information surrounding the sensor. The depth data gathered by the LIDAR sensor is sent to the Raspberry PI and then to the OpenCR 1.0 via a usb connection. The OpenCR 1.0 will then take the depth data and process it to send back to the Raspberry PI via a usb connection.

#### SLAM and ROS:
As the AuR moves, data points are collected by the LIDAR sensor and processed by a SLAM algorithm built into the ROS2, which is on board the TurtleBot3 [1]. The SLAM algorithm takes data points from the LIDAR and creates a model of the environment [8]. The SLAM algorithm uses incoming points to estimate the location of the TurtleBot3 by comparing the value of the points to their expected values and making corrections as needed. This process is described by the probability:

$P(x_k, m|z0_k, u0_k, x_0)$

Accuracy of SLAM is dependant on the quality of the LIDAR sensor but can have error as low as "5 cm given that LIDAR sensor depth accuracy already has 2-3 cm error" [9]. The type of SLAM algorithm used will also impact the accuracy of the model. This information means the constraints of being within 15 cm of the path and 1m of the destination, when used in conjunction with the UWB, can be fulfilled.

### Power:
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/localization/localization%20current%20graph.png)
The figure above shows the current draw for each component of the localization subsystem.

## BOM
| Item | Quantity | Price Per Item | Total Price | 
|-|-|-|-| 
| OpenCR1.0 | 1 | $215.00 | Already Purchased | 
| Raspberry Pi3 B+ | 1 | $35.00 | Already Purchased |
| LDS-01 | 1 | $200.00 | Already Purchased |
| PLA Filament Roll | 1 | $19.00 | $19.00 |
| 1/4" Hex Nuts(50) | 1 | $8.00 | $8.00 |
| 1/4" Hex Bolts(25) | 1 | $7.00 | $7.00 |
| 9v-5v Step DC-DC Converter(5) | 1 | $10.00 | $10.00 |
| Breadboards(3) | 1 | $10.00 | $10.00 |
| ESP32UWB DW3000 | 5 | $40.00 | $200.00 |
| | | Total Subsystem Cost: | $254.00|

## References
[1] Y.  Name,  “ROBOTIS  e-Manual,”  ROBOTIS  e-Manual.  https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/  (accessed  Nov. 09, 2022).  

[2] M. E. Rusli, M. Ali, N. Jamil, and M. M. Din, “An Improved Indoor  positioning Algorithm Based on RSSI-Trilateration Technique for Internet of Things (IOT),” 2016 International Conference on Computer and Communication Engineering (ICCCE), Jul. 2016, doi: 10.1109/iccce.2016.28.  

[3] M.  Simek,  “Two  Way  Ranging  (TWR),”  Sewio  RTLS.  https://www.sewio.net/uwb-technology/two-way-ranging/

[4]T. Polonelli, S. Schläpfer, and M. Magno, “Performance Comparison between Decawave DW1000 and DW3000 in low-power double side ranging applications,” IEEE Xplore, Aug. 01, 2022. https://ieeexplore.ieee.org/document/9881375 (accessed Nov. 28, 2022).

[5] Z. Li, X. Li, G. Mou, D. Jiang, X. Bao, and Y. Wang, “Design of  localization System Based on Ultra-Wideband and Long Range Wire-less,” 2019 IEEE 11th International Conference on Advanced Infocomm Technology (ICAIT), Oct. 2019, doi: 0.1109/icait.2019.8935892.

[6]DecaWave, “DW3000 Datasheet,” https://www.qorvo.com/. https://www.qorvo.com/products/d/da008142 (accessed Dec. 02, 2022).

[7]M. Farooq-I-Azam, Q. Ni, and M. Dong, “An Analytical Model of Trilateration Localization Error.” https://eprints.lancs.ac.uk/id/eprint/142930/1/PID1236902.pdf (accessed Dec. 09, 2022)..

[8] “What  is  LiDAR,  and  How  Does  it  Work?,”  J.D.  Power.  https://www.jdpower.com/cars/shopping-guides/what-is-LiDAR-and-how-does-it-work (accessed Nov. 09, 2022).  

[9] “The  definitive  guide  to  SLAM  &  mobile  mapping  technologies,” www.navvis.com.  https://www.navvis.com/technology/slam  (accessed Nov. 09, 2022).  

[10] Team  Ouster,  “Guide  to  evaluating  SLAM,”  ouster.com.  https://ouster.com/blog/guide-to-evaluating-slam/  (accessed  Nov.  9,  2022).  

