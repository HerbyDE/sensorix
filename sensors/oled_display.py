import busio
import board

from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw

class OLEDDisplayDriver(object):
    """
    TODO: Configure OLED screen to show important stats like battery voltage, pressure status, etc.
    """

    def __init__(self):
        self.addr = 0xc3
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = SSD1306_I2C(128, 32, self.i2c, addr=self.addr)

    def draw(self):
        image = Image.new("1", (self.oled.width, self.oled.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)

        self.oled.image(image)
        self.oled.show()

    def clear(self):
        pass


