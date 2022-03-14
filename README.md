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

# Implementation
In our implementation, we have added sensor ids from 0 to 2, where sensor P has id 0, sensor T has id 1, and sensor H has id 2.
In the monitor implementation, it was necessary to solve at the beginning that all the sensors should first supply the storage with valid
data. We solved this by means of three events, i.e. at the beginning the monitors waited for a signal from all sensors.
Then, when all sensors have delivered valid data, in a continuous cycle the monitor has a pause of 40 - 50 ms at the beginning
from the start, or from the last update. Then a trunk is used, which is blocked to throw away the
sensors, then access to the storage is gained via the lightswitch lock function, while also increasing the number of monitors reading at any given time.
Next, the read data is simulated, via a printout.
Finally, through the lightswitch unlock function, the data is updated and exited from the storage, while decrementing the number of reading monitors.

In the sensor implementation, as in the monitor implementation, we created a continuous cycle in which, at the beginning
a 50-60 ms update takes place, then they pass through the turnstile until they are blocked by the monitor. Access is gained
storage through the lightswitch lock function, while also increasing the number of writing sensors. Then the data is accessed,
which is simulated by waiting, but in this case if it is sensor P and T (i.e. sensors with id 0 and 1), the wait takes
10-20 ms and if it is sensor H (i.e. sensor with id 2), it takes 20-25 ms. To simulate the data update
we used the output as specified in the assignment. Subsequently, after the data is successfully written, it signals that it is valid, but in this case,
each sensor signals separately based on its id, allowing the monitors to start only after all sensors have written valid 
data. Eventually, it will go away from the repository via the lightswitch unlock funckie and reduce the number of sensors currently enrolling.

