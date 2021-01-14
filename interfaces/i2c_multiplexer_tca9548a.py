import board
import busio
from adafruit_tca9548a import TCA9548A
from adafruit_bmp280 import Adafruit_BMP280_I2C


class I2CMultiplex(object):
    def __init__(self):
        self.i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
        self.mux = TCA9548A(i2c=self.i2c, address=0x70)  # 0x70 is the standard byte address of the TCA9548a.
    def get_available_sensors(self):
        for ch in self.mux:
            try:
                baro = Adafruit_BMP280_I2C(i2c=ch, address=0x76)
                print(baro.pressure)
            except:
                print(f"No device at {ch}.")


if __name__ == "__main__":
    I2CMultiplex().get_available_sensors()