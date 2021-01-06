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
        '''
        This returns the QNH for hight estimation.
        :return:
        '''

        adj_pressure = self.sp_i2c.pressure * pow(1 - 600 / 44330.0, 5.255)
        return adj_pressure

        '''
        # Raw inputs from i2c bus
        loc_pressure = self.sp_i2c.pressure
        loc_temp = self.sp_i2c.pressure

        # Adjustment coefficients
        temp = [0, 0, 0]
        pres = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Get calibration data from BMP280 sensor
        cal_data = smbus2.SMBus(self.i2c_bus_addr).read_i2c_block_data(self.i2c_sp_channel, 0x88, 24)

        # Modify temperature coefficients as given in the BMP280 data sheet.
        temp[0] = cal_data[1] * 256 + cal_data[0]
        temp[1] = cal_data[3] * 256 + cal_data[2]
        temp[2] = cal_data[5] * 256 + cal_data[4]

        if temp[1] > 32767:
            temp[1] -= 65536
        if temp[2] > 32767:
            temp[2] -= 65536

        # Modify pressure coefficients as given in the BMP280 data sheet.
        pres[0] = cal_data[7] * 256 + cal_data[6]
        for idx in range(0, 8):
            pres[idx+1] = cal_data[2*idx+9] * 256 + cal_data[2*idx+8]
            if pres[idx+1] > 32767:
                pres[idx+1] -= 65536
        '''

    def read_temperature(self):
        return self.sp_i2c.temperature

    # def read_dynamic_pressure(self):
        # return self.dp_i2c