# This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
# Use with other I2C sensors would be similar.
import time
import board
import busio
import adafruit_bmp280
import adafruit_tca9548a

# Create I2C bus as normal
i2c = busio.I2C(board.SCL, board.SDA)

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# For each sensor, create it using the TCA9548A channel instead of the I2C object
bmp280_1 = adafruit_bmp280.Adafruit_BMP280_I2C(tca[0])
bmp280_2 = adafruit_bmp280.Adafruit_BMP280_I2C(tca[1])

# Loop and profit!
while True:
    print(f"Pressure 1: {bmp280_1}. Pressure 2: {bmp280_2}")
    time.sleep(0.2)