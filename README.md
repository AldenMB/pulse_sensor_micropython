# Pulse Sensor Micropython

This circuit uses a common [OLED display](https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html) to show the signal from a [pulse sensor](https://pulsesensor.com/) in real time using a Raspberry Pi Pico. Essentially, the microcontroller and screen are acting as a crude oscilloscope. 

# How to use

Simply load `main.py`, `live_pulse.py`, and `ssd1306.py` onto the pico, and wire it up like so:

| Pico     | OLED |
|----------|------|
| GND      | GND  |
| 3V3(OUT) | VCC  |
| GP6      | SDA  |
| GP7      | SCL  |

| Pico     | Pulse |
|----------|-------|
| GND      | -     |
| 3V3(OUT) | +     |
| GP28     | S     |

In addition, you will get a better signal if you put a 0.1 microfarad capacitor between GP28 and GND. Now the circuit should run whenever the microcontroller is powered.

