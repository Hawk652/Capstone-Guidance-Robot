# Docking Station Subsystem

## Function of the Subsystem
The function of the docking station subsystem is provide a area for the AuR to autonomously recharge power when needed.

## Specifications and Constraints

| No. | Specifications and Constraints | Origin | 
|-|-|-| 
| 1 | Shall have plugless charging | Supervisor: Dr. Van Neste 
| 2 | Shall follow proper wire gauging standards | NEC 310.16(b)


## Buildable Schematic 
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/docking%20station%20schematic%20v3.png)

The docking station subsystem will recieve power from a 120 VAC receptacle. The 120 VAC will be converted into 12 VDC through the use of a power supply AC adapter. The 12 VDC will then be sent to the metal contacts for the AuR to recieve power. A circuit breaker is added in to provide overcurrent protection to the circuit in the case of a short circuit happening. A manual boat rocker switch is added in between the circuit breaker and metal contacts to allow a user to cutoff power to the metal contacts. 

The power suuply adapter will feed into the circuit through a hole on the side of the docking station's box wall. The circuit breaker will be housed in the box of the station. The rocker switch will be mounted at the top of the station's box to provide ease of access. The docking metal contacts are mounted within the indentations created on the station. Room is provided within the docking station to provide adequate space for the wiring. 

#### 3D Model of Charging Station
The docking station follows the same idea as receptacles by having two indentations to house the active metal contacts within the docking station. By having the metal contacts embedded into the docking station, it would be more difficult for users and other objects to accidentally touch both active metal contacts. The indentations additionally assists in guiding the AuR into the correct position when recharging. A wire can fed through a hole on the side of the charging station and reach the metal contacts from under the docking station. Holes are made within the indents to provide easy access to the metal contacts for the wires. 

##### Isometric View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/isometric.png)

##### Top View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/top.png)

##### Side View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/side.png)

##### Close Up of Ramp View
![ALT](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/docking%20station/ramp%20height.png)

## Analysis
The current dimensions are based on the turtlebot's current height and width. The charging pad may be adjusted in the future to accomodate any modifications to the turtlebot's dimensions. A 12V Allkpoper circuit breaker is added to provide overcurrrent protection in the case that a short circuit occurs between the metal contacts. Furthermore, the Allkpoper circuit breaker can easiy be reset instead of having to replace the fuse whenever the breaker is tripped. A boat rocker switch will allow a user to activate or disable the docking station. Arc flash shall not occur due to the metal contacts only being supplied 12VDC. Additionally, there is sufficient distance between the metal contacts and a circuit breaker to prevent arc flash from occuring. 

## BOM
| Item                          | Quantity | Price Per Item        | Total Price       |
| ----------------------------- | -------- | --------------------- | ----------------- |
| 12V 2A Power Supply AC Adapter| 1        | $11.75                | $11.75            |
| Metal Contacts                | 1        | $16.95                | $16.95            |
| Allkpoper Circuit Breaker     | 1        | $12.90                | $12.90            |
|                               |          | Total Subsystem Cost: | $41.60            |



