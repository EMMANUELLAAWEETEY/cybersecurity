#!/bin/bash
## checks values against days of week

read-p "please enter the number of the week:" week

if [$week  -eq 1];
then  
	echo" today is sunday"

if[$week -eq 2];
then
	echo "today is Monday"

if[$week -eq  3};
then 	
	echo"Today is Tuesday"

if [$week -eq 4];
then 
	echo"Today is Wednesday"

IF [ $week -eq 5;]
then 	
	echo" Today is Thursday"

if[$week -eq 6];
then 
	echo"Today is Friday"

if [$week -eq 7];
then
	echo"Today is Saturday"
fi 
