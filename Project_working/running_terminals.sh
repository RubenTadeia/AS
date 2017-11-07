newTask="Neste terminal fica a correr o algoritmo"

gnome-terminal -e "bash -c \"roscore; exec bash\""
gnome-terminal -e "bash -c \"rosparam set RosAria/port /dev/pioneer/usb_to_serial_port && rosrun rosaria RosAria; exec bash\""
gnome-terminal -e "bash -c \"rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/RosAria/cmd_vel; exec bash\""
gnome-terminal -e "bash -c \"echo $newTask; exec bash\""