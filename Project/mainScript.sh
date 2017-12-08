#!/bin/bash

clear

projectPath='~/git/AS/Project/'

#############
# GLOBAL VAR
#############

red='\033[0;31m'
lightRed='\e[91m'
green='\e[32m'
lightYellow='\e[93m'
blue='\e[34m'
lightMagenta='\e[95m'
white='\e[97m'
lightCyan='\e[96m'
cyanBackground='\e[46m'
NC='\033[0m'
reset='\e[0m'
first="first"

#############
# FUNCTIONS
#############

main()
{
	# Iniciar o roscore
	gnome-terminal -e "bash -c \""$projectPath""functions.sh" $first; exec bash\"";

	# Ligar ao rosaria
	# printf ""$red"Vamos ligar agora ao robot Rosaria!"; echo ""; echo "";
	# printf ""$white"Pressione qualquer tecla para continuar!"$NC""; echo "";echo "";
	# read waiting_one;
	# gnome-terminal -e "bash -c \"rosparam set RosAria/port /dev/pioneer/usb_to_serial_port && rosrun rosaria RosAria; exec bash\""
	
	# Ligar ao rosaria
# 	printf ""$red"Vamos ligar agora ao robot Rosaria!"; echo ""; echo "";
# 	printf ""$white"Pressione qualquer tecla para continuar!"$NC""; echo "";echo "";
# 	read waiting_two;
# 	gnome-terminal -e "bash -c \"rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/RosAria/cmd_vel; exec bash\""
}

#############
# MAIN SCRIPT
#############
main