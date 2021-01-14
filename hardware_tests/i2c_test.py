"""
This class contains all hardware-related tests for the I2C bus and the TCA9548a multiplexer.
This code is distributed as is and no warranty is given regarding functionality, etc.
"""
import pigpio


class I2CTests(object):

    def __init__(self):
        pass

    def check_i2c_bus(self):
        pi = pigpio.pi()  # connect to local Pi

        for bus in range(1, 20):
            for channel in range(3, 77):
                print(f"Checking {bus}: {channel}")
                if channel is not 70:  # 0x70 is the MUX port.
                    sensor = pi.i2c_open(hex(bus), hex(channel))
                    try:
                        pi.i2c_read_byte(sensor)
                        print(f">> Device found at {hex(bus)}: {hex(channel)}!")
                    except:
                        pass
                    pi.i2c_close(sensor)

        pi.stop()  # disconnect from Pi
        print(">> I2C test successful.")

    def check_i2c_mux(self):
        pass


if __name__ == "__main__":
    I2CTests().check_i2c_bus()
