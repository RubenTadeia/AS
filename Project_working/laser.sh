rostopic list

<<ShouldSee
→ With just roscore running should appear at least:
/rosout
/rosout_agg

→ With laser we should see:
RosAria/laser/scan
ShouldSee


rostopic echo RosAria/laser/scan -n1
<<Explaining
Prints the information from the laser to all selected angles. -90 degrees do 90 degrees. With one degree increment
Explaining


rostopic info RosAria/laser/scan
<<Explaining
We see the type of message and the subscriber

Type: RosAria/sensor_msg/LaserScan
Explaining 

rosmsg show RosAria/sensor_msg/LaserScan
<<Explaining
flaot32[] ranges
Explaining 

roscd
<<Explaining
I run this command:
    catkin_create_pkg laser_values

But you don't need to do it.
Since I'have uploaded this package in the folder Project_working/ros_packages
Explaining 

roslaunch laser_values laser.launch
