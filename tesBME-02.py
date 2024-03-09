from machine import Pin, I2C
from bme_module import BME280Module
from utime import sleep

sda = Pin(8)
scl = Pin(9)
buzzer = Pin(0,Pin.OUT)
bme_module = BME280Module(0, scl, sda)

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
        print(" Alarm ON ")
        buzzer.on()
        print("**********")
    else:
        print("**********")
        print(" Alarm OFF ")
        buzzer.off()
        print("**********")
        
    sleep(1)



