import os
import sys
import signal
import time
import socket

# Adafruit libraries to address the i2c sensors
from sensorix.utils import ADS1x15, SSD1306


class ReadPower(object):

    def __init__(self):
        self.i2c_bus = 0x56
        self.min_volt = 3*3.3 # Min 9.9V
        self.max_volt = 3*4.2 # Max 12.6V
        self.volt_gain = 1
        self.adc = ADS1x15.ADS1115()

    def measure_voltage(self):
        measure = self.adc.read_adc(channel=0, gain=self.volt_gain)

        return measure

    def print_measure(self):
        print(self.measure_voltage())


if __name__ == '__main__':
    pr = ReadPower()
    pr.print_measure()
