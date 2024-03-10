#modified by ekovedc@gmail.com
#@Malang 10 Maret 2024
from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
class ULTRASONNIC:
    
    @staticmethod
    def ultrasonnic():
        
        tAwal = 0
        trigger.low()
        utime.sleep_us(2)
        trigger.high()
        utime.sleep_us(5)
        trigger.low()
        
        while echo.value() == 0:
            signalOff = utime.ticks_us()
        
        while echo.value() == 1:
            signalOn = utime.ticks_us()
        
        tAwal = signalOn - signalOff
        jarakCM = (tAwal * 0.0343) / 2
        jarakCM = round(jarakCM,2)
        
        return jarakCM
