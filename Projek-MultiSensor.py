from machine import Pin, I2C
from bme_module import BME280Module
from gas import GasSensor
from sh1106 import SH1106_I2C
from utime import sleep, sleep_us
import utime

i2c=I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
display = SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)

buzzer = Pin(0,Pin.OUT)

sda = Pin(8)
scl = Pin(9)
bme_module = BME280Module(0, scl, sda)

gas_sensor = GasSensor(26)

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
def ultrasonnic():
    timepassed=0
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance_cm = (timepassed * 0.0343) / 2
    distance_cm = round(distance_cm,2)
    
    return distance_cm

while True:
    temp, pressure,humdt, altitude = bme_module.get_sensor_readings()
    jarak = ultrasonnic()
    gas = round(gas_sensor.read_CO2_sensor(),2)
    
 
    print("============================")
    print("     SENSOR BME-280         ")
    print("----------------------------")
    print("Suhu         : ",temp)
    print("Tekanan Udara: ",pressure)
    print("Kelembahan   : ",humdt)
    print("Ketinggian   : ",altitude)
    print("----------------------------")
    
    print("============================")
    print("     SENSOR HSRF-05         ")
    print("----------------------------")
    print("Jarak        :",jarak)
    print("----------------------------")
    
    print("============================")
    print("     SENSOR MQ-5         ")
    print("----------------------------")
    print("Gas         : ",gas)
    print("----------------------------")
    
    if temp >= 28:
        print("**********")
        stsBz = "ON"
        buzzer.on()
        print(" Alarm ON ")
        print("**********")
        
    elif jarak <= 25:
        print("**********")
        stsBz = "ON"
        buzzer.on()
        print(" Alarm ON ")
        print("**********")
        
    elif gas <= 600:
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
    display.text('Temp  : ',0, 18, 1)
    display.text(str(temp),63, 18, 1)
    display.text('Jarak : ',0, 28, 1)
    display.text(str(jarak),63, 28, 1)
    display.text('Gas   : ',0, 38, 1)
    display.text(str(gas),63, 38, 1)
    display.text('Status: ',0, 53, 1)
    display.text(stsBz,63, 53, 1)
    display.hline(0, 63, 127, 1)
    display.hline(0, 0, 127, 1)
    display.hline(0, 14, 127, 1)
    display.hline(0, 50, 127, 1)
    display.vline(0, 0, 63, 1)
    display.vline(127, 0, 63, 1)
    display.show()
    
    sleep(1)
    