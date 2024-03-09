from machine import Pin, I2C
from bme_module import BME280Module
from sh1106 import SH1106_I2C
from utime import sleep

i2c=I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
sda = Pin(8)
scl = Pin(9)
buzzer = Pin(0,Pin.OUT)

bme_module = BME280Module(0, scl, sda)
display = SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)


while True:  
    temp, pressure,humdt, altitude = bme_module.get_sensor_readings()       
    print("============================")
    print("     SENSOR BME-280         ")
    print("----------------------------")
    print("Suhu         : ",temp)
    print("Tekanan Udara: ",pressure)
    print("Kelembahan   : ",humdt)
    print("Ketinggian   : ",altitude)
    print("----------------------------")
    
    if temp >= 30:
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
    display.text('Temp   :',0, 18, 1)
    display.text(str(temp),63, 18, 1)
    display.text('Press  :',0, 28, 1)
    display.text(str(pressure),63, 28, 1)
    display.text('Alttd  :',0, 38, 1)
    display.text(str(altitude),63, 38, 1)
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
    