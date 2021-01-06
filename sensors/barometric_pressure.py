import busio
import board
import adafruit_bmp280
import config

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
        self.sp_i2c.sea_level_pressure = config.SEA_LEVEL_PRESSURE
        # self.dp_i2c.sea_level_pressure = 1013.25

    def read_static_pressure(self):
        """
        This returns the QNH. To the raw measurement we add the pressure relative to MSL,
        which is 1 hPa per 30ft. BMP280 returns the height in meter. Thus, we convert the 1 hPa per 30ft into
        1 hPa per meter.
        :return:
        """
        adj_pressure = self.sp_i2c.pressure + self.sp_i2c.altitude / (30 * 0.3048)
        output = round(adj_pressure, ndigits=2)
        return output

    def read_dynamic_pressure(self):
        return 0.00

    def read_temperature(self):
        """
        This function returns the temperature in degree celsius based on the BMP280 sensor output.
        :return:
        """
        return round(self.sp_i2c.temperature, ndigits=2)

    def read_barometric_height(self):
        """
        Returns the barometric height in meters.
        :return:
        """
        return round(self.sp_i2c.altitude, ndigits=2)

    def generate_barometric_output(self):

        static_pressure = self.read_static_pressure()
        dynamic_pressure = self.read_dynamic_pressure()
        temp = self.read_temperature()
        # baro_height = self.read_barometric_height()

        nmea_sequence = f"P,{static_pressure},Q,{dynamic_pressure},T,{temp}"
        return nmea_sequence
