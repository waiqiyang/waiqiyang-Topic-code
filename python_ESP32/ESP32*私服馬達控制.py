#將servo.py模組上傳至ESP32
from servo import Servo #從servo模組匯入Servo類別
from machine import Pin #
import time #匯入time模組

my_servo = Servo(Pin(22)) #建立在ESP32第22腳位的物件
#可使用套件中的write_angle()指令來控制私服馬達
my_servo.write_angle(0)
time.sleep(1)
#花()秒時間轉動至0度

my_servo.write_angle(90)
time.sleep(1)



