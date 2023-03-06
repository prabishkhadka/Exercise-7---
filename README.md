# Exercise 7 --
 This repository contains all the exercises of week 8.

Exercise 7

Part A

Programmatically select features by location and update a field for the selected features.

In your Exercise7 folder Download Exercise7 folder, you have a four files (A, B, C, D). You will use Exercise7_A which contains the Washington geodatabase with two feature classes:

CityBoundaries
ParkAndRide 
You want to find out which cities contain park and ride facilities and what percentage of cities have at least one facility.

The CityBoundaries feature class has a field "HasParkAndRide," which is set to "False" by default. Your job is to mark this field "True" for every city containing at least one park and ride facility within its boundaries.
Your script should also calculate the percentage of cities that have a park and ride facility and print this figure for the user.
Assume that each point in the ParkAndRide dataset represents one valid park and ride (ignore the value in the TYPE field).

Part B

In Exercise7 B, find which cities have at least two park and rides within their boundaries.

Mark the "HasTwoParkAndRides" field as "True" for all cities that have at least two park and rides within their boundaries.
Calculate the percentage of cities that have at least two park and rides within their boundaries and print this for the user.
Part C

Select all park and ride facilities with a capacity of more than 500 parking spaces and put them into their own feature class. The capacity of each park and ride is stored in the "Approx_Par" field.

Part D

Write a script that selects all the park and ride facilities in a given city and saves them out to a new feature class. You can test with the city of 'Federal Way'.