from machine import Pin, ADC
import time

#溫度感測器
adc_pin = Pin(32)
adc = ADC(adc_pin)
adc.width(ADC.WIDTH_12BIT)
adc.atten(ADC.ATTN_11DB)

while True:
    vol = (adc.read()/4095)*3.6
    tem = (vol - 0.5)*100
    print("目前溫度", int(tem))
    time.sleep(1)