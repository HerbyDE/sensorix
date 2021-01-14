import time
import config
import socket

# from sensors.barometric_pressure import Barometer
from sensors.i2c_sensor_board import BarometricSensors


if __name__ == "__main__":
    BarometricSensors().read_dynamic_pressure()



    """
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

        # OLEDDisplayDriver().draw()

        time.sleep(1/config.SENSOR_SAMPLING_RATE_PER_SECOND) # Waining block to control the sampling rate.
    """
