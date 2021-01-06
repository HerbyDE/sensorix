# Adafruit libraries to address the i2c sensor
import Adafruit_ADS1x15
import config


class VoltMeter(object):

    def __init__(self):
        self.i2c_bus = 0x56
        self.min_volt = config.BATTERY_CAPACITY_MIN # Volt. Empty
        self.max_volt = config.BATTERY_CAPACITY_MAX # Volt. Full
        self.volt_gain = 1
        self.adc = Adafruit_ADS1x15.ADS1115()

    def measure_voltage(self):
        measure = self.adc.read_adc(channel=0, gain=self.volt_gain) # Value 17200 eq 12.20V
        voltage_factor = 17200 / 12.2
        actual_voltage = round(measure / voltage_factor, 2)
        if actual_voltage > self.max_volt:
            percentage = 101
        else:
            percentage = round(actual_voltage / self.max_volt, 4) * 100
        return actual_voltage

    def generate_measurement_point(self):
        return f"V,{self.measure_voltage()}"
