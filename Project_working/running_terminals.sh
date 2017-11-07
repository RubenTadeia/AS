<<README
Hello! In order to have your terminator as mine. Run the next command in terminal to open the file:

gedit ~/.config/terminator/config

And copy content of the file that is in "/git/AS/Project_working/usefull_files/terminator_file/config"
to the file you have just opened!
README

algorithm=""
rviz=""
laser=""
ekf="Neste terminal fica a correr o algoritmo do Extended Kalman Filter"


<<Terminal
This code is comment. It works, but does not use the terminator

gnome-terminal -e "bash -c \"roscore; exec bash\""
gnome-terminal -e "bash -c \"rosparam set RosAria/port /dev/pioneer/usb_to_serial_port && rosrun rosaria RosAria; exec bash\""
gnome-terminal -e "bash -c \"rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/RosAria/cmd_vel; exec bash\""
gnome-terminal -e "bash -c \"echo $ekf; exec bash\""
Terminal


terminator -e "bash -c \"roscore; exec bash\""
terminator -e "bash -c \"rosparam set RosAria/port /dev/pioneer/usb_to_serial_port && rosrun rosaria RosAria; exec bash\""
terminator -e "bash -c \"rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/RosAria/cmd_vel; exec bash\""
terminator -e "bash -c \"echo $newTask; exec bash\""