import time
import config
import socket

from sensors.barometric_pressure import Barometer
from sensors.battery_status import VoltMeter
from sensors.oled_display import OLEDDisplayDriver

from utils import transform_to_nmea_sentence
from interfaces.xcsoar_tcp_stream_server import ReactiveSocketServer


class Sensorix(object):

    def __init__(self):
        # self.battery = VoltMeter()
        self.baro = Barometer()

    def read_barometric_data(self):
        sp_measurement = self.baro.read_static_pressure()
        # dp_measurement = self.baro.read_dynamic_pressure()

        return sp_measurement

    # def read_battery_data(self):
        # Default I2C address for the A/D converter is 0x48 (48)
        # measurement = self.battery.generate_measurement_point()
        # return measurement


if __name__ == "__main__":
    sens = Sensorix()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        # voltage = sens.battery.generate_measurement_point()
        baro_data = sens.baro.generate_barometric_output()

        baro_nmea = transform_to_nmea_sentence(baro_data)
        # volt_nmea = transform_to_nmea_sentence(voltage)

        sock.sendto(bytes(baro_nmea.encode("utf-8")), ("127.0.0.1".encode("utf-8"), 4353))
        # sock.sendto(bytes(volt_nmea.encode("utf-8")), ("127.0.0.1".encode("utf-8"), 4353))

        # print(volt_nmea)
        print(baro_nmea)

        OLEDDisplayDriver().draw()

        time.sleep(1/config.SENSOR_SAMPLING_RATE_PER_SECOND) # Waining block to control the sampling rate.
