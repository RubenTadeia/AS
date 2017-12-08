#!/bin/bash

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


#############
# FUNCTIONS
#############

roscoreIntro()
{
	printf ""$lightMagenta"####################"$NC""; echo ""
	printf ""$red"Roscore Starting"; echo "";
	printf ""$lightMagenta"####################"$white""; echo "";echo "";
	roscore
}

#############
# FUNCTIONS
#############

main()
{
	if [ "$1" = "first" ];
		then
			echo "hello";
			roscoreIntro
	fi	
}

#############
# MAIN SCRIPT
#############
main