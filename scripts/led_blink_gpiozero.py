# a python3 version of Arduino's Blink example

from gpiozero import LED
from time import sleep

led = LED(17)

try:
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
except KeyboardInterrupt:
        print('interrupted!')
        led.close() # cleans up pin
