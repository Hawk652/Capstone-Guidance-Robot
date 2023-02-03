# Locomotion Subsystem
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/SamuelMandody-signoff-Locomotion/Documentation/Images/Locomotion.png)

## Function of the Subsystem
The locomotion subsystem is responsible for not only moving the AuR, but also maintaining the velocity set by the group in the constraints by using a closed loop system between the proposed motors, the encoders attached to those motors, and the controllers that will recieve feedback from the encoders. The feedback will go back to the Main Control subsystem to assist with the SLAM algorithm as well as re-adjust the duty cycle of the power signal being sent to the motors to maintain proper velocity.

## Constraints
|     No. |Constraint  |  Origin  |
|-|-|-|
|1| Shall travel at a speed of 0.7 ± .1 m/s | Standard: ISO/TS 15066|

## Analysis
Based on the documentation provided by the Turtlebot3 manual, it is clear that the currently equipped motors do not provide the necessary torque to reach a velocity above .26 m/s. The replacement motors which we have been donated by the Mechanical Engineering Department should be more than powerful enough to reach and maintain the proposed velocity.

The starting point is to determine the amount of pushing force required to move the turtlebot using Newton's Second Law of Motion:

$f = m * a$

The mass of the unmodified turtlebot is 1.8kg. After removing the stock Dynamixel motors which weigh 40g a piece and replacing them with the Pittman GM9236S025, the mass comes out to be around 3.062kg. It would be safe to assume that the acceleration to the specified velocity will be close to instant for calculation's sake. $2.1434N = 3.062kg * 0.7\frac{m}{s^2}$

After calculating force, the following equation can be used to obtain the exact torque required by both motors combined using the force from the last equation along with the radius of the wheels of the AuR:

$T = (f * r_{wheel})$

$0.707322Nm = (1.26N * .033m)$

The following equation will yield the current draw of the motors where $K_{T}$ is the torque constant of the motor found in the datasheet for the Pittman motor [1]:

$I = \frac{T}{K_{T}}$

$3.09A = \frac{0.03537Nm}{0.0229\frac{Nm}{A}}$

Last but not least, the power that the motors will be consuming running at their 12V operating point can be calculated using the following equation:

$P_{IN} = V * I$

$37.08W = 12V * 3.09A$

Based on the calculations above alongside the specifications provided to us via the datasheet of the motors, the group is certain that the motors that were provided will fit the needs of the AuR. They will not be operating out of spec and they also allow for overhead within the system for any future upgrades that would increase the mass of the AuR. The only downside to changing the stock motors is that now motor controllers are required to drive and regulate the speed of the motors. The Dynamixel motors that came stock on the turtlebot were an all in one closed loop system. Based on the calculations above, the Pololu Jrk G2 21v3 motor controller will be a perfect fit. Not only does it support a wide 4.5V-28V operating range, it can also deliver continuous current outputs of up to 2.6A. Each motor will be drawing ~1.545A. It also offers closed loop speed control to make use of the onboard motor encoders. Last but not least, the controllers are at a very solid price point for all that they offer at $59.50 per unit.[2]

## Pinout of the Motor Controller
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/SamuelMandody-signoff-Locomotion/Documentation/Electrical/Schematics/motor_controller_pinout.png)

This is the pin layout of the Jrk G2 21v3 motor controller.

## Buildable Schematic
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/SamuelMandody-signoff-Locomotion/Documentation/Electrical/Schematics/Locomotion_schematic.png)

This is how the locomotion subsystem will be powered and where the data that is retrieved is going. 

## BOM
| Item | Quantity | Price Per Item | Total Price | 
|-|-|-|-| 
| Pittman GM9236S025 | 2 | $350.00 | Already Purchased |
| Pololu Jrk G2 21v3 | 2 |  $59.95 | $119.90 |
| Solder             | 1 |  $10.00 |  $10.00 |
|Flux                | 1 |  $10.00 |  $10.00 |
| | | Total Subsystem Cost: | $139.90|

## References
[1] GM9236S025, "GM9236S025.pdf" GM9236S025.pdf. [Online]. Available: http://www.gearseds.com/files/GM9236S025.pdf. [Accessed: 01-Feb-2023]
[2] Jrk G2 21v3 USB Motor Controller, "Jrk G2 21v3 USB Motor Controller with Feedback" Jrk G2 21v3 USB Motor Controller. [Online]. Available: https://www.pololu.com/product/3142 [Accessed: 01-Feb-2023]
