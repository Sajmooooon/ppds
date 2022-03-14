from random import randint
from time import sleep
from fei.ppds import Mutex, Semaphore, Thread, Event, print


class Lightswitch:
    def __init__(self):
        self.counter = 0
        self.mutex = Mutex()

    def lock(self, sem):
        self.mutex.lock()
        counter = self.counter
        self.counter += 1
        if self.counter == 1:
            sem.wait()
        self.mutex.unlock()
        return counter

    def unlock(self, sem):
        self.mutex.lock()
        self.counter -= 1
        if self.counter == 0:
            sem.signal()
        self.mutex.unlock()


def init():
    access_data = Semaphore(1)
    turnstile = Semaphore(1)
    ls_monitor = Lightswitch()
    ls_sensor = Lightswitch()
    valid_data_0 = Event()
    valid_data_1 = Event()
    valid_data_2 = Event()

    for monitor_id in range(8):
        Thread(monitor, monitor_id, valid_data_0,  valid_data_1, valid_data_2,
               turnstile, ls_monitor, access_data)
    for sensor_id in range(3):
        Thread(sensor, sensor_id, turnstile, ls_sensor, valid_data_0,
               valid_data_1, valid_data_2, access_data)


def monitor(monitor_id, valid_data_0,  valid_data_1, valid_data_2, turnstile,
            ls_monitor, access_data):
    valid_data_0.wait()
    valid_data_1.wait()
    valid_data_2.wait()
    while True:
        read_duration = randint(40, 50) / 1000
        sleep(read_duration)
        turnstile.wait()
        number_reading_monitors = ls_monitor.lock(access_data)
        turnstile.signal()
        print(f'monitor "{monitor_id}": '
              f' number_reading_monitors={number_reading_monitors}' 
              f' read_duration = {read_duration}\n')
        ls_monitor.unlock(access_data)


def sensor(sensor_id, turnstile, ls_sensor, valid_data_0,  valid_data_1,
           valid_data_2, access_data):
    while True:
        sleep(randint(50, 60) / 1000)
        turnstile.wait()
        turnstile.signal()
        number_recording_sensors = ls_sensor.lock(access_data)
        if sensor_id == 2:
            record_duration = randint(20, 25) / 1000
        else:
            record_duration = randint(10, 20) / 1000
        print(f'sensor "{sensor_id}":'
              f' number_recording_sensors={number_recording_sensors},'
              f' record_duration={record_duration}\n')
        sleep(record_duration)
        if sensor_id == 0:
            valid_data_0.signal()
        elif sensor_id == 1:
            valid_data_1.signal()
        else:
            valid_data_2.signal()
        ls_sensor.unlock(access_data)


init()
