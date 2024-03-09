from machine import Pin, I2C
from sh1106 import SH1106_I2C
from utime import sleep

i2c=I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

display = SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
display.sleep(False)

while True:
    display.fill(0)    
    display.text('IPAS - BOE ',23, 3, 1)
    display.hline(0, 63, 127, 1)
    display.hline(0, 0, 127, 1)
    display.hline(0, 14, 127, 1)
    display.vline(0, 0, 63, 1)
    display.vline(127, 0, 63, 1)
    display.show()
    sleep(1)


