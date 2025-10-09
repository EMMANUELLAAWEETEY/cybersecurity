#!/bin/bash

# ask for the grade 
read -p "Enter the your grade (0-100):" grade

#grading the user
if[ "$grade" -ge 90 ] && [ "$grade" -lt 100 ];
then
	echo"A"
elif[ "$grade" -ge 80 ] &&[ "$grade" -lt 89 ];
then
	echo"B"
elif[ "$grade" -ge 70 ] && [ "$grade" -lt 69 ];
then
	echo"C"
elif[ "$grade" -ge 60 ] && [ "$grade" -lt 69 ];
then
	echo"D"
elif[ "$grade" -ge 0 ] && [ "$grade" -lt 59 ];
then
	echo"F"
else
	echo"invalid  grade .Please enter a number between 0 and 100"
fi
