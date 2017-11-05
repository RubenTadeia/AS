#!/usr/bin/env python
import os

# Opens 3 more terminals to work with the robot
os.system ("gnome-terminal && 'roscore' &");
os.system ("gnome-terminal && 'rosparam set RosAria/port /dev/pioneer/usb_to_serial_port && rosrun rosaria RosAria' &");
os.system ("gnome-terminal && 'rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/RosAria/cmd_vel' &");