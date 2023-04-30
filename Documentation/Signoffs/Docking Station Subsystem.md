# Docking Station Subsystem

## Function of the Subsystem
The function of the docking station subsystem is provide a area for the AuR to autonomously recharge power when needed.

## Specifications and Constraints

| No. | Specifications and Constraints | Origin | 
|-|-|-| 
| 1 | Shall have plugless charging | Supervisor: Dr. Van Neste 
| 2 | Shall follow proper wire gauging standards | NEC 310.16(b)


## Buildable Schematic 
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/docking%20station%20schematic.png)

The docking station subsystem will recieve power from a 120 VAC receptacle. The 120 VAC will be converted into 12 VDC through the use of a power supply AC adapter. The 12 VDC will then be sent to buck booster to be step up to 18 VDC to match the battery voltage. Then the 18 VDC is sent to the metal contacts for the AuR to recieve power. A circuit breaker is added in to provide overcurrent protection to the circuit in the case of a short circuit happening. The buck booster converter has a functioning switch implemented which allows a user to cutoff power to the metal contacts. 

The power supply adapter will feed into the circuit through a hole on the side of the docking station's box wall. The circuit breaker  will be mounted using velcro so it does not move around. There is enough room in the box to house the breaker. A hole is created in the lid of the docking station to provide a place for the buck boost converter to mount. This will allow a user to adjust the buck boost converter and switch the circuit on and off with ease. There are two 19 mm x 15 mm holes for the metal docking contacts to be placed in.  

#### 3D Model of Charging Station
The docking station follows the same idea as receptacles by having two indentations to house the active metal contacts within the docking station. By having the metal contacts embedded into the docking station, it would be more difficult for users and other objects to accidentally touch both active metal contacts. The indentations additionally assist in guiding the AuR into the correct position when recharging. A wire can fed through a hole on the side of the charging station and reach the metal contacts from within the docking station.

##### Front Isometric View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/isometric.png)

##### Front View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/front.png)

##### Back Isometric View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/isometric%20back.png)

#### Lid Isometric View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/lid%20isometric.png)

#### Lid Top View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/lid%20top.png)

#### Lid Side View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/lid%20side.png)

## Analysis
The current dimensions are based on the componenets designed to be used and the turtlebot's current height and width. The charging box may be adjusted in the future to accomodate any modifications to the turtlebot's dimensions. A 12V Allkpoper circuit breaker is added to provide overcurrrent protection in the case that a short circuit occurs between the metal contacts. Furthermore, the Allkpoper circuit breaker can easiy be reset instead of having to replace the fuse whenever the breaker is tripped. A buck boost converter will add further protection to the system and provides a switch to operate the circuit. Arc flash shall not occur due to the metal contacts only being supplied 12VDC. Additionally, there is sufficient distance between the metal contacts and a circuit breaker to prevent arc flash from occuring. 

## BOM
| Item                          | Quantity | Price Per Item        | Total Price       |
| ----------------------------- | -------- | --------------------- | ----------------- |
| 12V 2A Power Supply AC Adapter| 1        | $11.75                | $11.75            |
| Metal Contacts                | 1        | $16.95                | $16.95            |
| Allkpoper Circuit Breaker     | 1        | $12.90                | $12.90            |
| Boat Rocker Switch            | 1        | $ 5.99                | Bought through the power subsystem|
| Buck Boost Converter          | 1        | $ 20.88               | $ 20.88           |
|                               |          | Total Subsystem Cost: | $62.48            |



