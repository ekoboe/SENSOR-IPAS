#modified by ekovedc@gmail.com
#@Malang 10 Maret 2024
from machine import Pin
import utime

class ULTRASONNIC:    
    
    def __init__(self, trg , ech):
        self.trigger = Pin(trg, Pin.OUT)
        self.echo = Pin(ech, Pin.IN)        
    
    def ultrasonnic(self):       
        tAwal = 0
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()
    
        while self.echo.value() == 0:
            signalOff = utime.ticks_us()
        
        while self.echo.value() == 1:
            signalOn = utime.ticks_us()
        
        tAwal = signalOn - signalOff
        jarakCM = (tAwal * 0.0343) / 2
        jarakCM = round(jarakCM,2)
        
        return jarakCM

