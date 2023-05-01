%{
Author: Team 7
Function: runs a simulation to find the max error for trilateration using a
specific configuration of UWB beacons.
%}

%Set length of simulation
simlength = 100000;

%Define beacon locations
B_1 = [0 0];
B_2 = [-243 -238];
B_3 = [243 -238];

%Define distance error of beacons(cm)
Derror = 10;

%Find delta
delta = B_1(1)*(B_2(2)-B_3(2))+B_2(1)*(B_3(2)-B_1(2))+B_3(1)*(B_1(2)-B_2(2));

%Creat test vectors
dp = [0 0];
r1 = zeros(1,simlength)
r2 = zeros(1,simlength)
r3 = zeros(1,simlength)

%Run simulation
for i = 1:simlength
dp(1) = randi([0 2*243],1)-243;
dp(2) = -randi([0 238],1);
r1(i) = sqrt((dp(1)-B_1(1))^2+(dp(2)-B_1(2))^2);
r2(i) = sqrt((dp(1)-B_2(1))^2+(dp(2)-B_2(2))^2);
r3(i) = sqrt((dp(1)-B_3(1))^2+(dp(2)-B_3(2))^2);
end

%Calculate x/y errors
Ex = (1/(2*delta)).*((B_3(2)-B_2(2)).*(2*Derror.*(r1-r3))-(B_3(2)-B_1(2)).*(2*Derror.*(r2-r3)));
Ey = (1/(2*delta)).*(-(B_3(1)-B_2(1)).*(2*Derror.*(r1-r3))+(B_3(1)-B_1(1)).*(2*Derror.*(r2-r3)));

%Calculate location error
Terror = sqrt(Ex.^2+Ey.^2)

%Find max error
Merror = max(Terror)
