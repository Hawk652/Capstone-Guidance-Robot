
# Analysis of the Power and Charging Subsystem

## Power Subsystem

The constraints below will not be achievable due to not having the desired battery on hand:
 - Shall have a battery life of 3-4 hours.
 - Shall not operate below 15-20% of the battery capacity. 

The constraint below will not be tested due to not being able to implement the new motors for the project due to not having the motor controllers on hand:
 - Shall have a ripple voltage tolerance of 250 mVpp
 
The constraints that will be tested are listed below:
 - Shall have a manual override switch
 - Shall follow proper wire gauging standards

### Testing Method
To replicate the functionality of the battery connected to the power subsystem's circuit, a DC voltage supply is used to provide the power. The DC voltage supply is set to 18 V with a current of 3 A. Then the DC voltage supply is connected to the fuse box's positive and negative connections. A digital multimeter is used to measure the power output of the buck converters as the power supply sends power to the circuit. Additionally, a 1000 Ohm resistor is connected to the output of the buck converters so current can be measured. 

To test if the manual override switch functions properly, a multimeter is connected to the circuit to measure if any power is still being outputted.
 
### Results

The DC voltage and current at the output of the buck converters are listed below:
|  | Output Voltage (Volts) | Output Current (Amps)|
|--|--|--|
| Buck Converter 1 | 12.013 |0.12|
| Buck Converter 2 | 12.008 |0.11|

From measuring the output of both buck converters, the power subsystem will be able to provide the needed power for the additions that were planned for the robot initially. Furthermore, the output of Buck Converter 1 is measured 0 V when the switch is flipped. So, the manual override switch functions as needed. The wires used for assembling the circuit were not overloaded.


## Charging Subsystem

The specifications and constraints that will be tested are listed below:
 - Shall utilize plugless charging
 - Shall follow proper wire gauging standards
 - Provide a proper amount of power
 
### Testing Method

The charging system's circuit will be tested by connecting to a 120 VAC source such as a wall receptacle. Then a multimeter will then be connected to the metal charging contacts to ensure the correct DC voltage is provided. Additionally, the switch of the circuit will be toggled to ensure the circuit can be turned on and off by the user.

### Results

After connecting the charging circuit to a wall receptacle, the multimeter read the following measurements at the metal charging contacts while connected to a 1000 Ohm resistor:
- Output Voltage: 18.1 VDC
- Output Current: 0.18 A

In conclusion, the charging subsystem's circuit functions correctly and can meet the required specifications. Furthermore, the output DC voltage can be adjusted due to the buck booster being adjustable. The switch to toggle the circuit on and off works properly too. The wires used for assembling the circuit were not overloaded.
