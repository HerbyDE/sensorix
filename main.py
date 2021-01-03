# This is the main sensorix script containing all required i2c connections.

import busio
import adafruit_bmp280
import board
import time

from battery_status import VoltMeter
from barometric_pressure import Barometer
from battery_status import VoltMeter


class Sensorix(object):

    def __init__(self):
        self.battery = VoltMeter()
        self.baro = Barometer()

    def read_batometric_data(self):
        sp_measurement = self.baro.read_static_pressure()
        dp_measurement = self.baro.read_dynamic_pressure()

        return sp_measurement, dp_measurement

    def read_outside_temperature(self):
        measurement = self.baro.read_temperature()
        return measurement

    def read_battery_data(self):
        # Default I2C address for the A/D converter is 0x48 (48)
        measurement = self.battery.generate_measurement_point()
        return measurement


if __name__ == "__main__":
    sens = Sensorix()
    while True:
        measurement = sens.read_battery_data()
        print(measurement)
        time.sleep(1)