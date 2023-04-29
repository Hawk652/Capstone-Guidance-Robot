
# Analysis of the Power and Charging Subsystem

## Power Subsystem

The constraint below will not be tested due to not being able to implement the new motors for the project due to not having the motor controllers on hand:
 - Shall have a manual override switch
 
The constraints that will be tested are listed below:
 - Shall have a ripple voltage tolerance of 250 mVpp
 - Shall follow proper wire gauging standards

### Testing Method
To replicate the functionality of the battery connected to the power subsystem's circuit, a DC voltage supply is used to provide the power. The DC voltage supply is set to 18 V. Then the DC voltage supply is connected to the fuse box's positive and negative connections. A digital multimeter is used to measure the power output of the buck converters as the power supply sends power to the circuit. Additionally, a 1000 Ohm resistor is connected to the output of the buck converters so current can be measured. To measure the ripple voltage at the output, an oscilliscope was used to measure the output ripple voltage. 

[Ripple Votlage Experimentation Video](https://youtu.be/XyCeCxS2TAs)
 
### Results

The DC voltage and current at the output of the buck converters are listed below:
|  | Output Voltage (Volts) | Output Current (Amps)|
|--|--|--|
| Buck Converter 1 | 12.013 |0.12|
| Buck Converter 2 | 12.008 |0.11|

From measuring the output of both buck converters, the power subsystem will be able to provide the needed power for the additions that were planned for the robot initially. The measured ripple voltage is less than 250 mVpp. This was expected since the designed motors were not used. So, there is very minimal ripple voltage to begin with. The wires used for assembling the circuit were not overloaded.

The following constraints are related to the battery. However, since we did not recieve the desired battery, we will be testing the current LIPO battery on the turtlebot.
 - Shall have a battery life of 3-4 hours.
 - Shall not operate below 15-20% of the battery capacity. 

### Testing Method

To determine how long the battery will last, we ran the turtlebot and observed the capacity at different times. To determine if the turtlebot will operate below 15-20% battery capacity, we had the turtlebot move around until the motors stop moving due to low battery capacity. 

[Operation Below 15-20% Battery Life Experimentation Video](https://youtu.be/qoR8_F9Il6E)

The video explains the experimentation for ripple voltage. 

![Battery Capacity at 100%](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/Battery%20Capacity%201.jpg)

The figure above is taken at when the battery is 100%.

![Battery Capacity at 75%](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/main/Documentation/Images/Power/battery%20Capacity%202.jpg)

The figure above is taken 30 minutes after the first figure. As you can see, the battery life is at 75%. 



### Results

The battery life of the LIPO battery while the turtlebot is functioning is around 2 hours. Additionally, if we added other componenets to the turtlebot, the battery life will be shorter. This means the constatint of 3-4 hours is not met. This is to be expected since the LIPO battery was not meant to be used in the final design. 

## Charging Subsystem

The constraints below will not be achievable due to not having the desired battery on hand and not being able to interface with the current LIPO battery:
 - Shall utilize plugless charging

The specifications and constraints that will be tested are listed below:
 - Shall follow proper wire gauging standards
 
### Testing Method

The charging system's circuit will be tested by connecting to a 120 VAC source such as a wall receptacle. Then a multimeter will then be connected to the metal charging contacts to ensure the correct DC voltage is provided. Additionally, the switch of the circuit will be toggled to ensure the circuit can be turned on and off by the user.

### Results

After connecting the charging circuit to a wall receptacle, the multimeter read the following measurements at the metal charging contacts while connected to a 1000 Ohm resistor:
- Output Voltage: 18.1 VDC
- Output Current: 0.18 A

In conclusion, the charging subsystem's circuit functions correctly and can meet the required specifications. Furthermore, the output DC voltage can be adjusted due to the buck booster being adjustable. The switch to toggle the circuit on and off works properly too. The wires used for assembling the circuit were not overloaded.
