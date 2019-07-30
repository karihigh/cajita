# Cajita Chicarica
# NeoTrellis to select colors of NeoPixel strip
# NeoTrellis connected to Feather M4
# NeoPixel 136 strip connected to pin D5

import time
import board
from board import SCL, SDA
import busio
import neopixel
from adafruit_neotrellis.neotrellis import NeoTrellis
from digitalio import DigitalInOut, Direction

button_LED = DigitalInOut(board.D13)
button_LED.direction = Direction.OUTPUT
button_LED.value = True

pixel_pin = board.D5
num_pixels = 136

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis object
trellis = NeoTrellis(i2c_bus)

# color definitions
OFF = (0, 0, 0)
RED = (255, 0, 0)
ROUGE = (210, 0, 50)
DM_RED = (20, 0, 0)
YELLOW = (235, 150, 0)
GREEN = (0, 255, 20)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (80, 0, 240)
ORANGE = (255, 50, 0)
PINK = (255, 0, 100)
WHITE = (255, 255, 255)

ORDER = neopixel.GRB

pixels.fill(DM_RED)  # turn on the strip
pixels.show()

# this will be called when button events are received
def blink(event):
    # turn the trellis LED on when a rising edge is detected
    # do the chase for the NeoPixel strip

    if event.number == 0:
        print("zero")
        for chase_off in range(num_pixels):
            pixels[chase_off] = DM_RED
            pixels.show()
            time.sleep(0.005)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = DM_RED
            pixels.show()
            time.sleep(0.005)

    elif event.number == 1:
        print("one")
        for chase_off in range(num_pixels):
            pixels[chase_off] = CYAN
            pixels.show()
            time.sleep(0.005)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = BLUE
            pixels.show()
            time.sleep(0.005)

    elif event.number == 2:
        print("two")
        for chase_off in range(num_pixels):
            pixels[chase_off] = CYAN
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = BLUE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 3:
        print("three")
        for chase_off in range(num_pixels):
            pixels[chase_off] = RED
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = ROUGE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 4:
        print("four")
        for chase_off in range(num_pixels):
            pixels[chase_off] = OFF
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = WHITE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 5:
        print("five")
        for chase_off in range(num_pixels):
            pixels[chase_off] = OFF
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = WHITE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 6:
        print("six")
        for chase_off in range(num_pixels):
            pixels[chase_off] = OFF
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = WHITE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 7:
        print("six")
        for chase_off in range(num_pixels):
            pixels[chase_off] = PINK
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = ROUGE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 8:
        print("seven")
        for chase_off in range(num_pixels):
            pixels[chase_off] = PINK
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = PURPLE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 9:
        print("nine")
        for chase_off in range(num_pixels):
            pixels[chase_off] = PINK
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = PURPLE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 10:
        print("ten")
        for chase_off in range(num_pixels):
            pixels[chase_off] = PINK
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = PURPLE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 11:
        print("eleven")
        for chase_off in range(num_pixels):
            pixels[chase_off] = PINK
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = ROUGE
            pixels.show()
            time.sleep(0.05)

    elif event.number == 12:
        print("twelve")
        for chase_off in range(num_pixels):
            pixels[chase_off] = GREEN
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = CYAN
            pixels.show()
            time.sleep(0.05)
    elif event.number == 13:
        print("thirteen")
        for chase_off in range(num_pixels):
            pixels[chase_off] = GREEN
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = CYAN
            pixels.show()
            time.sleep(0.05)
    elif event.number == 14:
        print("fourteen")
        for chase_off in range(num_pixels):
            pixels[chase_off] = GREEN
            pixels.show()
            time.sleep(0.05)
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = CYAN
            pixels.show()
            time.sleep(0.05)

    elif event.number == 15:
        print("fifteen")
        for chase_on in range(num_pixels):
            pixels[chase_on] = OFF
            pixels.show()
            time.sleep(0.05)

# boot up animation on trellis
trellis.pixels.brightness = 0.2
for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink

    # light the trellis LEDs on startup
    trellis.pixels[0] = DM_RED
    trellis.pixels[1] = BLUE
    trellis.pixels[2] = BLUE
    trellis.pixels[3] = WHITE

    trellis.pixels[4] = PINK
    trellis.pixels[5] = PINK
    trellis.pixels[6] = PINK
    trellis.pixels[7] = WHITE

    trellis.pixels[8] = GREEN
    trellis.pixels[9] = GREEN
    trellis.pixels[10] = GREEN
    trellis.pixels[11] = WHITE

    trellis.pixels[12] = YELLOW
    trellis.pixels[13] = YELLOW
    trellis.pixels[14] = YELLOW
    trellis.pixels[15] = OFF
    time.sleep(.05)

print("Cajita Chicarica is on")

while True:
    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 milliseconds or so
    time.sleep(.02)


    # Cajita Chicarica
# NeoTrellis to select colors of NeoPixel strip
# NeoTrellis connected to Feather M4
# NeoPixel 136 strip connected to pin D5

import time
import board
from board import SCL, SDA
import busio
import neopixel
from adafruit_neotrellis.neotrellis import NeoTrellis
from digitalio import DigitalInOut, Direction

button_LED = DigitalInOut(board.D13)
button_LED.direction = Direction.OUTPUT
button_LED.value = True

pixel_pin = board.D5
num_pixels = 5

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
print(pixels)

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis object
trellis = NeoTrellis(i2c_bus)

# color definitions
OFF = (0, 0, 0)
RED = (255, 0, 0)
ROUGE = (210, 0, 50)
DM_RED = (20, 0, 0)
YELLOW = (235, 150, 0)
GREEN = (0, 210, 20)
CYAN = (0, 100, 240)
BLUE = (0, 0, 255)
PURPLE = (80, 0, 240)
ORANGE = (255, 30, 0)
PINK = (255, 0, 100)
WHITE = (255, 255, 255)
DM_WHITE = (100, 100, 100)

ORDER = neopixel.GRB

pixels.fill(DM_RED)  # turn on the strip
pixels.show()

# this will be called when button events are received
def blink(event):
    # turn the trellis LED on when a rising edge is detected
    # do the chase for the NeoPixel strip

    if event.number == 0:
        print("zero")
        def wheel(pos):
            # Input a value 0 to 255 to get a color value.
            # The colours are a transition r - g - b - back to r.
            if pos < 0 or pos > 255:
                r = g = b = 0
            elif pos < 85:
                r = int(pos * 3)
                g = int(255 - pos*3)
                b = 0
            elif pos < 170:
                pos -= 85
                r = int(255 - pos*3)
                g = 0
                b = int(pos*3)
            else:
                pos -= 170
                r = 0
                g = int(pos*3)
                b = int(255 - pos*3)
            return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

        def rainbow_cycle(wait):
            for j in range(255):
                for i in range(num_pixels):
                    pixel_index = (i * 256 // num_pixels) + j
                    pixels[i] = wheel(pixel_index & 255)
                pixels.show()
                time.sleep(wait)

        while event.number == 0:
            rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step

    elif event.number == 1:   m
        print("one")
        pixels.fill(CYAN)
        pixels.show()

    elif event.number == 2:
        print("two")
        pixels.fill(ORANGE)
        pixels.show()

    elif event.number == 3:
        print("three")
        pixels.fill(PINK)
        pixels.show()

    elif event.number == 4:
        print("four")
        pixels.fill(PURPLE)
        pixels.show()

    elif event.number == 5:
        print("five")
        pixels.fill(PINK)
        pixels.show()

    elif event.number == 6:
        print("six")
        pixels.fill(ROUGE)
        pixels.show()

    elif event.number == 7:
        print("six")
        pixels.fill(ORANGE)
        pixels.show()

    elif event.number == 8:
        print("seven")
        pixels.fill(RED)
        pixels.show()

    elif event.number == 9:
        print("nine")
        pixels.fill(GREEN)
        pixels.show()

    elif event.number == 10:
        print("ten")
        pixels.fill(PURPLE)
        pixels.show()

    elif event.number == 11:
        print("eleven")
        pixels.fill(PINK)
        pixels.show()

    elif event.number == 12:
        print("twelve")
        pixels.fill(PINK)
        pixels.show()

    elif event.number == 13:
        print("thirteen")
        pixels.fill(PINK)
        pixels.show()

    elif event.number == 14:
        print("fourteen")
        pixels.fill(PINK)
        pixels.show()

    elif event.number == 15:
        pixels.fill(OFF)
        pixels.show()

# boot up animation on trellis
trellis.pixels.brightness = 0.2
for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    # trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink

    # light the trellis LEDs on startup
    trellis.pixels[0] = DM_RED
    trellis.pixels[1] = CYAN
    trellis.pixels[2] = ORANGE
    trellis.pixels[3] = DM_WHITE

    trellis.pixels[4] = PURPLE
    trellis.pixels[5] = PINK
    trellis.pixels[6] = ROUGE
    trellis.pixels[7] = ORANGE

    trellis.pixels[8] = RED
    trellis.pixels[9] = GREEN
    trellis.pixels[10] = PURPLE
    trellis.pixels[11] = DM_WHITE

    trellis.pixels[12] = DM_WHITE
    trellis.pixels[13] = DM_WHITE
    trellis.pixels[14] = DM_WHITE
    trellis.pixels[15] = OFF
    time.sleep(.05)

print("Cajita Chicarica is on")

while True:
    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 milliseconds or so
    time.sleep(.02)