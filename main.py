# This is the main sensorix script containing all required i2c connections.

import busio
import adafruit_bmp280
import board
import time

from barometric_pressure import Barometer
from battery_status import VoltMeter


class Sensorix(object):

    def __init__(self):
        self.battery = VoltMeter()
        self.baro = Barometer()

    def read_barometric_data(self):
        sp_measurement = self.baro.read_static_pressure()
        # dp_measurement = self.baro.read_dynamic_pressure()

        return sp_measurement

    def read_battery_data(self):
        # Default I2C address for the A/D converter is 0x48 (48)
        measurement = self.battery.generate_measurement_point()
        return measurement


if __name__ == "__main__":
    sens = Sensorix()
    while True:
        m1 = sens.read_battery_data()
        m2 = sens.read_barometric_data()
        print(f"Battery: {m1}. Baro: {m2}")
        time.sleep(.2)