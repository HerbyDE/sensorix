import os
import sys
import signal
import time
import socket

# Adafruit libraries to address the i2c sensor
import Adafruit_ADS1x15


class ReadPower(object):

    def __init__(self):
        self.i2c_bus = 0x56
        self.min_volt = 11.9 # Volt. Empty
        self.max_volt = 12.65 # Volt. Full
        self.volt_gain = 1
        self.adc = Adafruit_ADS1x15.ADS1115()

    def measure_voltage(self):
        measure = self.adc.read_adc(channel=0, gain=self.volt_gain) # Value 17200 eq 12.20V
        voltage_factor = 17200 / 12.2
        actual_voltage = measure / voltage_factor
        percentage = round(actual_voltage / self.max_volt, 4) * 100

        return percentage

    def transform_to_nmea_sentence(self, key, value):
        sentence = f"POV, {key}, {value}"

        # Generate the checksum as required by the OpenVario Protocol.
        packet = str(bytes(sentence, encoding="utf-8"))
        checksum = 0
        for bt in packet:
            checksum ^= ord(bt)

        return f"${sentence}*{hex(checksum)}"

    def print_measure(self):
        voltage = self.measure_voltage()
        msg = self.transform_to_nmea_sentence(key="V", value=voltage)
        print(msg)


if __name__ == '__main__':
    pr = ReadPower()
    pr.print_measure()
