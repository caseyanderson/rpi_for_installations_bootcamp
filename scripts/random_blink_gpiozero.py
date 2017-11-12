# using random to generate blinking interval

from gpiozero import LED
import random
from time import sleep

led = LED(17)

try:
    while True:
        interval = random.uniform( 0.1, 3)
        print( "interval is " + str(interval))
        print("on!")
        led.on()
        sleep(interval)
        print("off!")
        print()
        led.off()
        sleep(interval)
except KeyboardInterrupt:
        print('interrupted!')
        led.close() # cleans up pin
