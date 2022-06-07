import time
from machine import I2C, Pin, ADC
from ssd1306 import SSD1306_I2C


def main():
    i2c = I2C(id=1, sda=Pin(6), scl=Pin(7), freq=1_700_000)
    display = Display(i2c)
    heart = ADC(28)
    plotting_rate = 120  # Hz

    while True:
        new_value = heart.read_u16() // 2**10
        display.shift_in(new_value)
        display.show()
        time.sleep(1 / plotting_rate)


class Display(SSD1306_I2C):
    def __init__(self, i2c):
        super().__init__(128, 64, i2c)
        self.fill(0)
        self.show()
        self.prev_y = 0

    def shift_in(self, value):
        value = 63 - value
        self.scroll(-1, 0)
        self.vline(127, 0, 64, 0)
        self.line(126, self.prev_y, 127, value, 1)
        self.prev_y = value


if __name__ == "__main__":
    main()
