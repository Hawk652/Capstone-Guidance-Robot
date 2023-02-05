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

The docking station subsystem will recieve power from a 120 VAC from a receptacle. The 120 VAC will be converted into 12 VDC through the use of a wall adapter. The 12 VDC will then be sent to the metal contacts for the AuR to recieve power. A manual switch is added in between the wall adapter and metal contacts to reduce electrical safety risks to users within the area.

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
The current dimensions are based on the turtlebot's current height and width. The charging pad may be adjusted in the future to accomodate any modifications to the turtlebot's dimensions. 

## BOM
| Item                          | Quantity | Price Per Item        | Total Price       |
| ----------------------------- | -------- | --------------------- | ----------------- |
| 12V Wall Adapter              | 1        | 10.00                 | 10.00             |
| Metal Contacts                | 1        | 16.95                 | 16.95             |
|                               |          | Total Subsystem Cost: | 26.95             |



