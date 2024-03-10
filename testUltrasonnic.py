from machine import Pin,I2C
from sh1106 import SH1106_I2C
from ultrsonic import ULTRASONNIC
from utime import sleep

i2c=I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
display = SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
buzzer = Pin(0, Pin.OUT)

usonic = ULTRASONNIC()

while True:    
    jarak = usonic.ultrasonnic()
    
    print("============================")
    print("     SENSOR HSRF-05         ")
    print("----------------------------")
    print("Jarak        :",jarak)
    print("----------------------------")
    
    if jarak <= 25:
        print("**********")
        stsBz = "ON"
        buzzer.on()
        print(" Alarm ON ")
        print("**********")
    else:
        print("**********")
        stsBz = "OFF"
        buzzer.off()
        print(" Alarm OFF ")
        print("**********")
    
    display.fill(0)    
    display.text('MONITORING',23, 3, 1)
    display.text('Jarak  : ',0, 18, 1)
    display.text(str(jarak),63, 18, 1)
    display.text('Status :',0, 53, 1)
    display.text(stsBz,63, 53, 1)
    display.hline(0, 63, 127, 1)
    display.hline(0, 0, 127, 1)
    display.hline(0, 14, 127, 1)
    display.hline(0, 50, 127, 1)
    display.vline(0, 0, 63, 1)
    display.vline(127, 0, 63, 1)
    display.show()

    sleep(1)
