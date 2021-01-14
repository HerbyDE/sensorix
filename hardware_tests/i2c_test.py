"""
This class contains all hardware-related tests for the I2C bus and the TCA9548a multiplexer.
This code is distributed as is and no warranty is given regarding functionality, etc.
"""
import board
import smbus2
import busio

from adafruit_tca9548a import TCA9548A


class I2CTests(object):

    def __init__(self):
        self.i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
        self.i2c_mux = TCA9548A(i2c=self.i2c, address=0x70)
        self.sens_channels = [0x48, 0x70]

    def check_i2c_hardware(self):
        registered_devices = {}

        for mux_ch in range(0, 7):
            try:
                ext_bus = self.i2c_mux[mux_ch]
                bus = smbus2.SMBus(ext_bus)
                for ch in range(128):
                    try:
                        bus.read_byte(ch)
                        registered_devices[mux_ch] = ch
                        print(f">> Sensor detected at MUX {mux_ch} - CH {ch}")
                    except:
                        pass
            except:
                print(f">> No sensor detected at MUX {mux_ch}.")
        print(f"{len(registered_devices.keys())} sensor(s) registered on I2C Bus.")
        return registered_devices
