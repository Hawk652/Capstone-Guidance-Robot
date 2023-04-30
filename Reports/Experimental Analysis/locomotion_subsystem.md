# Analysis of the Locomotion Subsystem

## Locomotion Subsystem
The constraints below will not be achievable due to not receiving motor controllers to drive the motors:
 - Shall travel at a speed of 0.7 m/s ± 0.1 m/s

### Results
Based on the documentation supplied for the turtlebot 3 Waffle Pi, the maximum velocity achievable without upgrading the locomotion subsystem is 0.26 m/s. The robot will not be able to travel any faster unless we received the motor controllers to include the motors that were hand picked for the project. 
In conclusion, the locomotion subsystem will not be altered due to lack of availability of necessary parts and focus will be shifted to other subsystems to ensure that they can meet their required specifications/constraints with the parts that are available to us.

Additionally, we ran an experiment of 5 trials to determine the top speed of the AuR. In these experiments, we marked a distance of 2 meters, accelerated the AuR to its top speed, then measured the time between crossing the two marked positions. This gave an overall average top speed of 0.23 m/s, which is within the expected range.

| Distance | Time |
|----------|------|
| 2m       | 8.52s|
| 2m       | 8.75s|
| 2m       | 8.68s|
| 2m       | 8.56s|
| 2m       | 8.53s|

![Locomotion Experiment](../../Documentation/Images/locomotion/locomotion_experiment.png)
