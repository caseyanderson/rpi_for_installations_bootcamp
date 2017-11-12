from gpiozero import Button
from gpiozero import LED

button = Button(4)
led = LED(17)

try:
    while True:
        led.source = button.values
except KeyboardInterrupt:
    print("interrupted!")
    button.close()
    led.close()
