# Locomotion Subsystem
![Alt text](https://github.com/Hawk652/Capstone-Guidance-Robot/blob/SamuelMandody-signoff-Locomotion/Documentation/Images/Locomotion.png)

## Function of the Subsystem
The locomotion subsystem is responsible for not only moving the AuR, but also maintaining the velocity set by the group in the constraints by using a closed loop system. This can be verified by the telemetric data provided by the encoders on the motors.

#Constraints
|     No. |Constraint  |  Origin  |
|-|-|-|
|1|  Shall travel at a speed of 0.7 ± .1 m/s           |Standard: ISO/TS 15066      |

## Buildable Schematic
will be added once I get the okay on the Analysis portion.

## Analysis
Based on the documentation provided by the Turtlebot3 manual, it is clear that the currently equipped motors do not provide the necessary torque to reach nor maintain anywhere near the required velocity. The starting point is to determine the amount of pushing force required to move the turtlebot using Newton's Second Law. The mass of the turtlebot is 1.8kg, and the acceleration can vary. It would not make sense to set the acceleration too high due to increased power consumption by the motors on top of the fact that once the turtlebot reaches 1.1 m/s, it will be maintaining that velocity without exceeding it (within reason). Overhead needs to be considered in the case of a load increase to the turtlebot as well as potential gradient changes depending on the area of future application. The current itteration of the AuR will be tested in Brown Hall on the second floor which is considerably flat. After calculating force, we can use the following equation to obtain the exact torque required by both motors combined (torque = (force * wheel radius)/2). Once torque is calculated, the power consumed can be calculated based on the average operating speed of the motor at the required torque. Now that Power has been calculated, the current draw can be determined using (P = IV) plugging in 12V for the voltage seeing as the current 12V motor will be replaceed with another 12V motor.


$f = m * a$

$T = \frac{(f * r_{wheel})}{2}$

$T = K_{T} * I$

$P_{IN} = V * I$

$ω = \frac{v}{r}$

$P_{OUT} = T * ω$

$P_{AVG} = f * v$

## BOM
| Item | Quantity | Price Per Item | Total Price | 
|-|-|-|-| 
| Pittman GM9236S025 | 2 | $350.00 | Already Purchased |
| Pololu Jrk G2 21v3 | 2 |  $59.95 | $119.90 |
| Solder             | 1 |  $10.00 |  $10.00 |
|Flux                | 1 |  $10.00 |  $10.00 |
| | | Total Subsystem Cost: | $578.00|

## References


