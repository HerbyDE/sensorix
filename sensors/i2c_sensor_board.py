import smbus2
import busio
import board

from adafruit_bmp280 import Adafruit_BMP280_I2C
from adafruit_tca9548a import TCA9548A
from adafruit_bmp3xx import BMP3XX_I2C

class BarometricSensors(object):

    def __init__(self):
        self.i2c_bus = busio.I2C(scl=board.SCL, sda=board.SDA)
        self.i2c_mux = TCA9548A(i2c=self.i2c_bus, address=0x70)
        self.wired_sensors = dict()

        self.bmp280_1 = Adafruit_BMP280_I2C(i2c=self.i2c_mux[1], address=0x76)
        self.bmp388 = BMP3XX_I2C(i2c=self.i2c_mux[0], address=0x77)
        # self.bmp280_2 = Adafruit_BMP280_I2C(i2c=self.i2c_mux[2], address=0x76)

    def read_dynamic_pressure(self):
        print(self.bmp388.pressure)
        print(self.bmp388.altitude)


