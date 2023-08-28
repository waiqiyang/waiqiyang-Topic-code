from machine import Pin, PWM
import time

#建立PWM物件
buzzer = PWM(Pin(23, Pin.OUT),freq = 0, duty = 512)
buzzer.freq(349)
time.sleep(1)
buzzer.freq(294)
time.sleep(1)

buzzer.deinit()