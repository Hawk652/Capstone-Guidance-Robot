# Analysis of the Safety Subsystem

## Safety Subsystem
The constraints below will not be achievable due to not having the designed battery and motors:
 - Shall have manual override (power will be cut from the motor)

 The constraint below will be tested because of the implementation of Lidar:
 - Shall maintain a distance of 0.5 m from obstacles and people
 
## LIDAR
### Testing Method
The test was performed by having the turtlebot navigate down the hallway of the first floor of Prescott Hall and having a person stand in the way of the turtlebot's path.

[Object/People Avoidance Experimentation](https://youtu.be/KBJQAzEwXu4)

### Result
The turtlebot was able to avoid collision with a person and wall. Unfortunately, the turtlebot did not meet the constraint of maintaining a distance of 0.5 m. For the turtlebot to maintain the distance of 0.5 m, additional sensors need to be added. 

Furthermore, 0.5 m is too large of a distance for the turtlebot to maintain. The turtlebot would not be able to navigate the hallways if there are obstacles in the way. The 0.5 m constaint should be adjusted since the hallways are too narrow and if there are multiple obstacles too.


## Proximity Sensor
- Was unable to test coils due to test due to delivery issues
- Printed out 3d models for bobbins for the coils
- If I were able to test this I would have tested the reasonance frequency and made sure that all of my turn were consistent. 

## Ultrasonic Sensor
- Was unable to test anything because these parts have not arrived 
- If I were to test this I would have tested the distance by placing an object in front of it, and seeing how long it would have taken for the information to be received. I would perform this task several times to ensure that the data was accurate.
