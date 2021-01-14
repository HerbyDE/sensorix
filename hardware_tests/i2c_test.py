"""
This class contains all hardware-related tests for the I2C bus and the TCA9548a multiplexer.
This code is distributed as is and no warranty is given regarding functionality, etc.
"""
import smbus2


class I2CTests(object):

    def check_i2c_hardware(self):
        registered_devices = {}
        for bus_no in range(20):
            try:
                bus = smbus2.SMBus(bus_no)
                print(f"Testing BUS {bus_no}")
                for ch in range(128):
                    try:
                        bus.read_byte(ch)
                        registered_devices[bus_no] = ch
                    except:
                        pass
                bus.close()
            except:
                pass
        print(f"{len(registered_devices.keys())} sensor(s) registered on I2C Bus.")
        return registered_devices
