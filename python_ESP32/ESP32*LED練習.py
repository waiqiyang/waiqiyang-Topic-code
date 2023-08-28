#從 machine 模組中匯入 Pin 物件
from machine import Pin, PWM
#匯入 time 模組
import time

led = Pin(5, Pin.OUT)#LED位置是連接在第五腳位，狀態設置為輸出
'''
# 创建PWM对象以控制亮度
led_pwm = PWM(led_pin)

# 设置初始颜色（关闭LED）
led_pwm.duty(0)  # 设置初始亮度为0，即关闭LED


led_pwm.duty(100)
'''
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)


    