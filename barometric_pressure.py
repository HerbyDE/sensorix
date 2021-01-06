import busio
import board
import adafruit_bmp280

from smbus2 import smbus2


class Barometer(object):

    def __init__(self):
        self.i2c_bus_addr = 0x01
        self.i2c_bus = smbus2.SMBus(bus=self.i2c_bus_addr)
        self.i2c_sp_channel = 0x76
        self.i2c_dp_channel = 0x77
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sp_i2c = adafruit_bmp280.Adafruit_BMP280_I2C(i2c=self.i2c, address=self.i2c_sp_channel)
        # self.dp_i2c = adafruit_bmp280.Adafruit_BMP280_I2C(i2c=self.i2c, address=self.i2c_dp_channel)

        # Configure the default sea level pressure of 1013.25 hPa
        self.sp_i2c.sea_level_pressure = 1013.25
        # self.dp_i2c.sea_level_pressure = 1013.25

    def read_static_pressure(self):
        return self.sp_i2c.sea_level_pressure

    def read_adjusted_pressure(self):
        '''
        This returns the QNH for hight estimation.
        :return:
        '''

        # Raw inputs from i2c bus
        loc_pressure = self.sp_i2c.pressure
        loc_temp = self.sp_i2c.pressure

        # Adjustment coefficients
        temp = [0, 0, 0]
        pres = [0, 0, 0, 0, 0, 0, 0, 0, 0]











    def read_temperature(self):
        return self.sp_i2c.temperature

    # def read_dynamic_pressure(self):
        # return self.dp_i2c