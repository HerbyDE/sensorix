import smbus2
import busio
import board

from adafruit_bmp280 import Adafruit_BMP280_I2C
from adafruit_tca9548a import TCA9548A
from adafruit_bmp3xx import BMP3XX_I2C

class BarometricSensors(object):

    def __init__(self, wired_sensors: dict):
        self.bmp280_1 = None
        self.bmp388 = None
        self.bmp280_2 = None
        self.i2c_bus = busio.I2C(scl=board.SCL, sda=board.SDA)
        self.i2c_mux = TCA9548A(i2c=self.i2c_bus, address=0x70)
        self.input_sensors = {
            11: 119,
        }
        self.wired_sensors = dict()
        pass

    def identify_sensors(self):
        for k, v in self.input_sensors.items():
            print(f"Configuring BUS {k} - CH {v}")
            try:
                if "static_pressure" not in self.wired_sensors.keys():
                    self.wired_sensors["static_pressure"] = Adafruit_BMP280_I2C(i2c=self.i2c_mux[k-10], address=hex(v))
                else:
                    self.wired_sensors["tek_pressure"] = Adafruit_BMP280_I2C(i2c=self.i2c_mux[k - 10], address=hex(v))
            except:
                try:
                    self.wired_sensors["dynamic_pressure"] = BMP3XX_I2C(i2c=self.i2c_mux[k - 11], address=hex(v))
                except:
                    print(f"Unknown sensor detected at BUS {k} - CH {v}.")

        print(self.wired_sensors)
        return self.wired_sensors