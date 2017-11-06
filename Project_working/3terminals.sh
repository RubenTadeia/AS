gnome-terminal -e roscore &>/dev/null &
gnome-terminal -e rosparam set RosAria/port /dev/pioneer/usb_to_serial_port && rosrun rosaria RosAria &>/dev/null &
gnome-terminal -e rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/RosAria/cmd_vel &>/dev/null &