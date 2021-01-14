"""
This class contains all hardware-related tests for the I2C bus and the TCA9548a multiplexer.
This code is distributed as is and no warranty is given regarding functionality, etc.
"""
import pigpio
import smbus2


class I2CTests(object):

    def __init__(self):
        pass

    def check_i2c_bus(self):
        pi = pigpio.pi()  # connect to local Pi

        for bus in range(1, 20):
            print(f"Testing BUS {bus}")
            try:
                for channel in range(3, 78):
                    sensor = pi.i2c_open(bus, channel)
                    try:
                        pi.i2c_read_byte(sensor)
                        print(f">>  CH {channel} - Device found!")
                    except:
                        print(f"    CH {channel} - No device.")
                        pass
                    pi.i2c_close(sensor)
            except:
                pass

        pi.stop()  # disconnect from Pi
        print(">> I2C test successful.")

    def check_i2c_hardware(self):
        for bus_no in range(1, 20):
            try:
                bus = smbus2.SMBus(bus_no)
                for ch in range(3, 78):
                    try:
                        bus.read_byte(ch)
                        print(f"Deivce found at {bus_no} - {ch}")
                    except:
                        pass
            except:
                pass

    def check_i2c_mux(self):
        pass


if __name__ == "__main__":
    I2CTests().check_i2c_hardware()
