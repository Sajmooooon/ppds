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

# Pseudocode

```
FUNCTION init()
    access_data = Semaphore(1)
    turnstile = Semaphore(1)
    ls_monitor = Lightswitch()
    ls_sensor = Lightswitch()
    valid_data_0 = Event()
    valid_data_1 = Event()
    valid_data_2 = Event()

    FOR monitor_id = 0 to 7
        Thread(monitor, monitor_id)
    ENDFOR

    FOR sensor_id = 0 to 2
        Thread(sensor, sensor_id)
    ENDFOR
ENDFUNCTION

FUNCTION monitor(monitor_id)
    valid_data_0.wait()
    valid_data_1.wait()
    valid_data_2.wait()
    WHILE True:
        read_duration = rand(40 to 50 ms)
        sleep(read_duration)
        turnstile.wait()
        number_reading_monitors = ls_monitor.lock(access_data)
        turnstile.signal()
        PRINT ('monitor "%02d": number_reading_monitors=%02d read_duration=%03d\n')
        ls_monitor.unlock(access_data)
    ENDWHILE
ENDFUNCTION

FUNCTION sensor(sensor_id):
    WHILE True:
        sleep(50 to 60 ms)
        turnstile.wait()
        turnstile.signal()
        number_recording_sensors = ls_sensor.lock(access_data)
        IF sensor_id is equal 2
            record_duration = rand(20 to 25 ms)
        ELSE
            record_duration = rand(10 to 20 ms)
        ENDIF
        PRINT ('sensor "%02d": number_recording_sensors=%02d record_duration=%03d\n')
        sleep(record_duration)
        IF sensor_id is equal 0
            valid_data_0.signal()
        ELSE IF sensor_id is equal 1
            valid_data_1.signal()
        ELSE
            valid_data_2.signal()
        ENDIF
        ls_sensor.unlock(access_data)
    ENDWHILE
ENDFUNCTION

```