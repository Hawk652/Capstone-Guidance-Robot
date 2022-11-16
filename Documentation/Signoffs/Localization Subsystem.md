# Localization Subsystem

## Function of the Subsystem
The localization subsystem (Fig. 1) will be tasked with gathering and processing positional data points from sensors. The sensors shall all be mounted onboard the Turtlebot 3. The sensors that will gather data for this subsystem will be the LiDar and the ESP32UWB DW3000. The LiDar will gather data points from all reflective surfaces around it for the SLAM algorithm to determine the AuR's current location. The UWB (Ultra Wideband) module will determine the distance between itself and 2 other UWB modules using triangulation. The other 2 UWB modules will serve as a destination marker. Using all the prior mentioned data, the AuR will be able to determine its current location. The AuR will use the updated current position data along with the route data generated from the navigation subsystem to determine the deviation of the route. 

## Specifications and Constraints

| No. | Specifications and Constraints | Origin | 
|-|-|-| 
| 1 | Shall guide users to within 1 m of their desired room | Supervisor: Dr. Van Neste 
| 2 | Shall maintain a distance of 0.5 m from obstacles and people | Broader Implication
| 3 | Shall not deviate from the expected path by more than 15 cm | Broader Implication
| 4 | Shall detect the AuR's position to a precision of 15cm | Customer: Dr. Andy Pardue

## Buildable Schematic 
The values for required voltage and resistive load used in Fig. 2. were derived from the specification documents for the individual components.

## Analysis

### UWB  Beacons:
A UWB beacon-based solution was chosen for higher resolution localization since it is accurate to within 15 cm which aids the constraints of being within 15 cm of its path and within 1 m of its destination [1]. The UWB beacons will be ESP32 UWB DW3000 modules.

Trilateration can be used to find the coordinates of an object based on its distance relative to three beacons [2]:

$(x- x_{1})^{2}+(y- y_{1})^{2} = r_{1}{}^{2}$

$(x- x_{2})^{2}+(y- y_{2})^{2} = r_{2}{}^{2}$

$(x- x_{3})^{2}+(y- y_{3})^{2} = r_{3}{}^{2}$

In order to find the distance from the device to a given beacon this Two Way Ranging(TWR) equation is used, where c is the speed of light d is the distance from the given beacon, RR is the Received Response time, Poll Sent time, SR is the Sent Response time, RP is the Received Poll time, RF is the Received Final time, SF is the Sent Final time and ToF is the Time of Flight [3]:

$ToF=\frac{(RR-SP)-(SR-RP) +(RF-SR)-(SF-RR)}{4}$

These equations work by calculating the time between messages and using the speed of light to determine the distance between beacons.

### Turtlebot:

#### LIDAR:
LiDar sensors collect depth information about the environment using a laser. A laser is pulsed from the sensor and photons are reflected back to the sensor [4]. This allows the sensor to know the distance between itself and the surface from which the photons were reflected. The sensor spins and collects many points in order to gather depth information surrounding the sensor.

#### SLAM and ROS:
As the AuR moves, data points are collected by the LiDar sensor and processed by a SLAM algorithm built into the ROS2, which is on board the TurtleBot3 [1]. The SLAM algorithm takes data points from the LiDar and creates a model of the environment [5]. The SLAM algorithm uses incoming points to estimate the location of the TurtleBot3 by comparing the value of the points to their expected values and making corrections as needed. This process is described by the probability:

$P(x_k, m|z0_k, u0_k, x_0)$

Accuracy of SLAM is dependant on the quality of the LiDar sensor but can have error as low as "5 cm given that LiDar sensor depth accuracy already has 2-3 cm error" [6]. The type of SLAM algorithm used will also impact the accuracy of the model. This information means the constraints of being within 15 cm of the path and 1m of the destination, when used in conjunction with the UWB, can be fulfilled.

### Power:
The analysis of the power for the localization subsystem resulted in failure. The failure was caused by the team's lack of knowledge of including several of the turtlebot's components in a circuit simulation. The team will need further advisement on the circuit simulation for the localization subsystem.

## BOM
| Item | Quantity | Price Per Item | Total Price | 
|-|-|-|-| 
| Turtlebot 3 Waffle Pi | 1 | $1.647.00 | Already Purchased | 
| ESP32UWB DW3000 | 5 | $40.00 | $200 | 
| | | Total Subsystem Cost: | $200|

## References
[1] Y.  Name,  “ROBOTIS  e-Manual,”  ROBOTIS  e-Manual.  https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/  (accessed  Nov. 09, 2022).  
[2] M. E. Rusli, M. Ali, N. Jamil, and M. M. Din, “An Improved Indoor  positioning Algorithm Based on RSSI-Trilateration Technique for Internet of Things (IOT),” 2016 International Conference on Computer and Communication Engineering (ICCCE), Jul. 2016, doi: 10.1109/iccce.2016.28.  
[3] M.  Simek,  “Two  Way  Ranging  (TWR),”  Sewio  RTLS.  https://www.sewio.net/uwb-technology/two-way-ranging/  
[4] “What  is  LiDar,  and  How  Does  it  Work?,”  J.D.  Power.  https://www.jdpower.com/cars/shopping-guides/what-is-LiDar-and-how-does-it-work (accessed Nov. 09, 2022).  
[5] “The  definitive  guide  to  SLAM  &  mobile  mapping  technologies,” www.navvis.com.  https://www.navvis.com/technology/slam  (accessed Nov. 09, 2022).  
[6] Team  Ouster,  “Guide  to  evaluating  SLAM,”  ouster.com.  https://ouster.com/blog/guide-to-evaluating-slam/  (accessed  Nov.  9,  2022).  
[7] Z. Li, X. Li, G. Mou, D. Jiang, X. Bao, and Y. Wang, “Design of  localization System Based on Ultra-Wideband and Long Range Wire-less,” 2019 IEEE 11th International Conference on Advanced Infocomm Technology (ICAIT), Oct. 2019, doi: 0.1109/icait.2019.8935892.

