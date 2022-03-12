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
    valid_data = Event()

    for monitor_id in range(2):
        Thread(monitor, monitor_id, valid_data, turnstile, ls_monitor,
               access_data)
    for sensor_id in range(11):
        Thread(sensor, sensor_id, turnstile, ls_sensor, valid_data,
               access_data)


def monitor(monitor_id, valid_data, turnstile, ls_monitor, access_data):
    valid_data.wait()
    while True:
        sleep(0.5)
        turnstile.wait()
        number_reading_monitors = ls_monitor.lock(access_data)
        turnstile.signal()
        print(f'monitor "{monitor_id}": '
              f' number_reading_monitors={number_reading_monitors}\n')
        ls_monitor.unlock(access_data)


def sensor(sensor_id, turnstile, ls_sensor, valid_data, access_data):
    while True:
        turnstile.wait()
        turnstile.signal()
        number_recording_sensors = ls_sensor.lock(access_data)
        record_duration = randint(10, 15) / 1000
        print(f'sensor "{sensor_id}":'
              f' number_recording_sensors={number_recording_sensors},'
              f' record_duration={record_duration}\n')
        sleep(record_duration)
        valid_data.signal()
        ls_sensor.unlock(access_data)


init()
