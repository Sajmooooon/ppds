# PPDS 04
Fourth assignment from the PPDS course.

# Description
In this problem we simulate a nuclear power plant with 3 sensors and 8 operators.
Each sensor performs an update every 50 - 60ms and 2 of the 3 sensors perform a data update every
10-20ms and one of the three every 20-25ms. The sensors continuously update the measured values and each of them has
dedicated space in the storage.
Operators in the plant view the readings from the sensors on a monitor, the monitor is read-only. 
The data accumulation on the monitor is sent continuously in a cycle where one update takes 40-50 ms. 
The monitors are only triggered when all sensors have sent valid data to the repository.

