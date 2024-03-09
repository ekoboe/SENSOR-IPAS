from machine import Pin, I2C
from mq2 import MQ2
from sh1106 import SH1106_I2C
from utime import sleep

i2c=I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
display = SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)

buzzer = Pin(0,Pin.OUT)

sensor = MQ2(pinData = 26, baseVoltage = 3.3)
print("Calibrating")
sensor.calibrate()
print("Calibration completed")
print("Base resistance:{0}".format(sensor._ro))

while True:
    smoke = round(sensor.readSmoke(),2)
    lpg = round(sensor.readLPG(),2)
    methan = round(sensor.readMethane(),2)
    hydro = round(sensor.readHydrogen(),2)
    
    print("============================")
    print("     SENSOR MQ-2         ")
    print("----------------------------")
    print("Smoke         : ",smoke)
    print("LPG           : ",lpg)
    print("Methane       : ",methan)
    print("Hydrogen      : ",hydro)
    print("----------------------------")
    
    if smoke >= 30:
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
    display.text('Smoke : ',0, 18, 1)
    display.text(str(smoke),63, 18, 1)
    display.text('LPG   : ',0, 28, 1)
    display.text(str(lpg),63, 28, 1)
    display.text('Hydro : ',0, 38, 1)
    display.text(str(hydro),63, 38, 1)
    display.text('Status: ',0, 53, 1)
    display.text(stsBz,63, 53, 1)
    display.hline(0, 63, 127, 1)
    display.hline(0, 0, 127, 1)
    display.hline(0, 14, 127, 1)
    display.hline(0, 50, 127, 1)
    display.vline(0, 0, 63, 1)
    display.vline(127, 0, 63, 1)
    display.show()
    
    sleep(0.5)
    