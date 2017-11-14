## blink

### setup

Install the [gpiozero](https://gpiozero.readthedocs.io/en/stable/#) library: `sudo apt-get install python3-gpiozero`


### equipment
* 1x Resistor (270 or 330 Ohms or similar)
* 1x LED


### hookup pattern

Note: Illustrations sourced from [here](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/).

Confirm that you have a functional LED by wiring it up inline with a resistor between `3V3` and `GND`. See below for an illustration of this hookup pattern:

<img src="/media/led-3v3-hookup.png" width="630" height="375">

After confirming that your LED works, move the wire that was previously attached at `3V3` to `GPIO` pin 17 (labeled as `G17` on the `PiWedge`). See below for an illustration of this hookup pattern:

<img src="/media/led-gpio17-hookup.png" width="630" height="375">

<br/>

### on the way to blink

Rather than `scp`-ing files between our Macbook and Pi it's more convenient to add scripts to a GitHub repo and then simply pull from there to your Pi. I have added scripts that we will use during this workshop to a new folder in our GitHub repo [here](https://github.com/mediadesignpractices/fieldc_cheatsheets/tree/master/scripts). If you have not already done so, take a moment to clone the GitHub repo onto your Raspberry Pi now.


#### ls

One can print the contents of a folder to the terminal with the Unix command `ls`. Execute `ls` in the `scripts` directory now.

There are other parameters that one can use with `ls` to alter its behavior. One command that you should commit to memory is `ls -la`. Execute `ls -la` in the scripts directory now.

`ls -la` shows `all (or -a)` of the contents of a folder in `long (or -l)` format, which includes lots of useful information: the exact size of the file, who owns the file, who has the right to look at it, and when it was last modified.

Right now we just need to focus on the permissions component of the `ls -la` output, which generally looks like the following: `-rw-r--r--`. For our current purposes all we need to understand is that such a file is not executable, though it needs to be in order to be run via python.

Make the scripts in this folder executable by editing (to suit your needs) and executing the following line per file: `sudo chmod +x filename.py`

Confirm that the files are executable by running `ls -la` in the `scripts` directory once more. All we care about right now is that the permissions line ends with an `x` like so: `-rwxr-xr-x`


#### try, except, and handling errors

`errors` are one's friend when programming, as they give a programmer clues towards what is problematic about his or her code. Frequently we discuss `Syntactical Errors`, or those errors caused by typos or misspellings. Nonetheless, it's also possible to encounter errors during execution of a script. These errors are referred to as `Exceptions` and may or may not be ignorable (errors referred to as `fatal` are those errors which are not ignorable).

It is considered best practice to anticipate the errors one's code may encounter during execution and design a way for the program to `handle` those errors. The `try` statement specifies exception handlers for a group of statements. In other words, one tries to execute some code with a `try` statement and then provides various procedures to `handle` errors as listed in the `except` statement.

The simplest example of handling a `non-fatal` error can be seen below:

```python

try:
    while True:
        print("do stuff!")
except KeyboardInterrupt:
        print('interrupted!')
        print("Goodbye!")
```

In the above example we have the basic structure of a `try except` block that handles a `KeyboardInterrupt` (i.e. `[CTL+C]`). In other words, one can put a line of code to happen forever in a infinite `while` loop (`while True:`) and simply end the loop by hitting `[CTL+C]`.

Another example (from the [led_blink_gpiozero.py](https://github.com/mediadesignpractices/fieldc_cheatsheets/blob/master/scripts/led_blink_gpiozero.py) code) can seen below:

```python

from gpiozero import LED
from time import sleep

led = LED(17)

try:
    while True:
        print
        led.on()
        sleep(1)
        led.off()
        sleep(1)
except KeyboardInterrupt:
        print('interrupted!')
        led.close() # free Pin 17
        print("Goodbye!")
```

In the above example an LED blinks on and off forever, however as soon as a `KeyboardInterrupt` occurs the `while` loop is terminated and the program cleans up the pin allocated to the LED (`led.close()`).

At a minimum I add `KeyboardInterrupt` as an exception in Python code, particularly when prototyping.



### simple blink

1. Run [led_blink_gpiozero.py](https://github.com/mediadesignpractices/fieldc_cheatsheets/blob/master/scripts/led_blink_gpiozero.py): `ipython3 led_blink_gpiozero.py`
2. After reveling in the wonder of a Python3 version of Arduino's blink example, terminate the `while` loop with `[CTL+C]`.
3. Try changing the duration of either or both `sleep` lines to increase/decrease the amount of time the LED is on/off and run the script again.



### blink for a random duration

[random_blink_gpiozero.py](https://github.com/mediadesignpractices/fieldc_cheatsheets/blob/master/scripts/random_blink_gpiozero.py) is a slightly more complex version of [led_blink_gpiozero.py](https://github.com/mediadesignpractices/fieldc_cheatsheets/blob/master/scripts/led_blink_gpiozero.py). A few notes:

* we import the `random` module to gain access to various random number generators. Currently we use `random.uniform()` to generate a number between 0.1 and 3 (storing that number in `interval` for use in both `sleep` statements) but there are lots of other generators provided by the `random` module. One can leverage iPython3's `.<TAB>` functionality to list all methods associated with `random`. Even better, after locating a generator that sounds promising, bring up the help docs by adding a `?` to the end of the command and hitting `[ENTER]`.
* we `concatenate` (combine) a string statement on line 12 with the following: `print( "interval is " + str(interval))`. This give one a way to see the labeled numerical output of `random.uniform()` in the terminal. One has to `string cast` the value stored in `interval` from `float`to `string` prior to concatenation.
* the lazy way to insert `newlines` between blocks of `print()` statements is to included an empty `print()`, which occurs here on line 17. There is probably a better way to do this.
* `led.close()` is used here as part of the exception block in our `try` statement, allowing one to simultaneously terminate the while loop and cleanup pin allocations.

<br/>

## button

### equipment
* 1x button (momentary or toggle)


### hookup pattern

Note: Illustrations sourced from [here](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/).

<img src="/media/button.png" width="630" height="375">


### simple button

The `gpiozero` module provides lots of nice convenience methods. For example, using a button to print one of two messages to the terminal can be achieved simply with the following (from [simple_button.py](https://github.com/mediadesignpractices/fieldc_cheatsheets/blob/master/scripts/simple_button.py) in the GitHub repo):

```python
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

```


#### button + LED

Finally, the simplest way to use a button to control an `LED` is to map the values of the button (`LOW` or `HIGH`) to said LED, like so (from [button_LED.py](https://github.com/mediadesignpractices/fieldc_cheatsheets/blob/master/scripts/button_LED.py)):

```python
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

```


## control LARGE things!

By repurposing the `button_LED.py` code from above, and replacing the `LED` with an `AC/DC Control Relay Device`, like [this](https://dlidirect.com/collections/frontpage/products/iot-power-relay) one, one can create causal relationships between Media, Electrical things, and the activity of a person.d
