from gpiozero import Button

button = Button(4)

try:
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button is not pressed")
except KeyboardInterrupt:
    print("interrupted!")
    button.close()
