#!/bin/bash


#check if password has both letters and number

read -p  "Enter  your password:" password
echo

length=${#password}
	if (( length >=8));
then
	echo "strong password"

	elif (( length >=6 && length <8));
then 
	echo "moderate password"
else
	echo "weak password"

fi
