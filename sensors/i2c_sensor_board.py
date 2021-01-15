import smbus2
import busio
import board
import math

from adafruit_bmp280 import Adafruit_BMP280_I2C
from adafruit_tca9548a import TCA9548A
from adafruit_bmp3xx import BMP3XX_I2C

class BarometricSensors(object):
    """
    This class initializes the barometric sensors connected to the Raspberry Pi unit via I2C.
    There is a total of three sensors: (I) static pressure, (II) dynamic pressure, (III) TEK pressure.
    (I) measures the atmospheric pressure around the glider.
    (II) is connected the the pitot tube and is used for airspeed indication (IAS).
    (III) is used for variometer estimations by using the total energy compensation metric.

    Static and TEK pressure are limited to 1100 hPa max. since the BMP280 is only capable of measuring upto 1100 hPa.
    The dynamic pressure sensor (BMP388) in contrast is capable of measuring up to 1250 hPa.
    If desired all sensors can be exchanged for the BMP388 to allow greater flexibility.
    """

    def __init__(self):
        self.i2c_bus = busio.I2C(scl=board.SCL, sda=board.SDA)
        self.i2c_mux = TCA9548A(i2c=self.i2c_bus, address=0x70)
        self.wired_sensors = dict()

        self.bmp280_1 = Adafruit_BMP280_I2C(i2c=self.i2c_mux[0], address=0x76)
        self.bmp388 = BMP3XX_I2C(i2c=self.i2c_mux[1], address=0x77)
        self.bmp280_2 = Adafruit_BMP280_I2C(i2c=self.i2c_mux[2], address=0x76)

        self.bmp280_1.sea_level_pressure = 1013.25
        self.bmp388.sea_level_pressure = 1013.25
        self.bmp280_2.sea_level_pressure = 1013.25

        self.air_density = 1.204        # kg/m2
        self.dynamic_pressure = 0       # Pa (!)
        self.tek_pressure = 1013.25     # hPa
        self.IAS = 0                    # kph
        self.QNH = 1013.25              # hPa
        self.altitude = 0               # MSL
        self.temperature = 21           # °C

    def calculate_ias(self):
        """
        IAS is calculated based on Prandt‘l pitot tube rules.
        v = pf * sqrt((2 * diff_pressure) / ad)

        v = Airspeed (IAS)
        pf = pitot tube factor (std.: 1.0015)
        diff_pressure = dynamic_pressure - static_pressure
        ad = air density (dynamically calculated based on temperature)
        :return:
        """
        self.air_density = self.bmp280_1.pressure / (287 * (273 + self.temperature))
        self.dynamic_pressure = self.bmp388.pressure - self.bmp280_1.pressure
        self.IAS = 1.0015 * math.sqrt(((2 * self.dynamic_pressure) / self.air_density))

        return round(self.IAS, ndigits=2)

    def read_static_pressure(self):
        """
        The static pressure is taken for the QNH and altitude estimation as well as the temperature recording.
        Temperature is given in degree celsius.
        :return:
        """
        self.altitude = self.bmp280_1.altitude
        self.QNH = self.bmp280_1.pressure + self.altitude / (30 * 0.3048)
        self.temperature = self.bmp280_1.temperature

        return round(self.QNH, ndigits=2)

    def read_dynamic_pressure(self):
        """
        The dynamic pressure is calculated based on the difference between the TEK pressure and the pitot tube pressure
        to avoid a differential pressure sensor. It has to be seen if this solution proves to be suitable but is
        preferred since it saves quite some space in the housing.
        :return:
        """
        tek = self.bmp280_2.pressure
        pitot = self.bmp388.pressure

        self.dynamic_pressure = (pitot - tek) * 100  # Convert hPa in Pa.

        return round(self.dynamic_pressure, ndigits=2)

    def read_TEK_pressure(self):
        self.tek_pressure = self.bmp280_2.pressure + self.altitude / (30 * 0.3048)
        return self.tek_pressure

    def get_barometric_data(self):
        """
        This outputs all relevant information as given in the OpenVario protocol.
        XCSoar uses this information to provide detailed flight insights.
        :return:
        """
        output = {
            "static_pressure": self.read_static_pressure(),
            "dynamic_pressure": self.read_dynamic_pressure(),
            "total_pressure": self.read_TEK_pressure(),
            "temperature": self.temperature,
            "airspeed": self.calculate_ias()
        }

        return output
