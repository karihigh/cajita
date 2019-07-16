# Cajita Chicarica
# NeoTrellis to select colors of NeoPixel strip
# NeoTrellis connected to Feather M4

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
DM_RED = (100, 0, 0)
YELLOW = (235, 150, 0)
GREEN = (0, 255, 20)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (80, 0, 240)
ORANGE = (255, 50, 0)
PINK = (255, 0, 100)
WHITE = (255, 255, 255)

ORDER = neopixel.GRB

'''
COLORS = [  # pixel colors
    OFF, RED, GREEN, BLUE,
    WHITE_WARM, PINK, CYAN, ORANGE,
    LIGHT_BLUE, YELLOW, ROUGE, WHITE_COOL,
    WHITE, YELLOW_GREEN, PURPLE, OFF
]
'''

pixels.fill(DM_RED)  # turn on the strip
pixels.show()


def dimmed_colors(color_values):
    (red_value, green_value, blue_value) = color_values
    return (red_value // 10, green_value // 10, blue_value // 10)


# this will be called when button events are received
def blink(event):
    # turn the trellis LED on when a rising edge is detected
    # do the chase for the NeoPixel strip

    if event.number == 0:
        # este print me aparece dos veces en la consola cuando apreto un botón
        print("zero")
        trellis.pixels[event.number] = dimmed_colors(DM_RED)
        for chase_on in range(num_pixels):
            pixels[chase_on] = DM_RED
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = DM_RED
    elif event.number == 1:
        print("one")
        trellis.pixels[event.number] = dimmed_colors(YELLOW)
        for chase_on in range(num_pixels):
            pixels[chase_on] = YELLOW
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = YELLOW
    elif event.number == 2:
        print("two")
        trellis.pixels[event.number] = dimmed_colors(PINK)
        for chase_on in range(num_pixels):
            pixels[chase_on] = PINK
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = PINK
    elif event.number == 3:
        print("three")
        trellis.pixels[event.number] = dimmed_colors(GREEN)
        for chase_on in range(num_pixels):
            pixels[chase_on] = GREEN
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = GREEN
    elif event.number == 4:
        print("four")
        trellis.pixels[event.number] = dimmed_colors(BLUE)
        for chase_on in range(num_pixels):
            pixels[chase_on] = BLUE
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = BLUE
    elif event.number == 5:
        print("five")
        trellis.pixels[event.number] = dimmed_colors(CYAN)
        for chase_on in range(num_pixels):
            pixels[chase_on] = CYAN
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = CYAN
    elif event.number == 6:
        print("six")
        trellis.pixels[event.number] = dimmed_colors(RED)
        for chase_on in range(num_pixels):
            pixels[chase_on] = RED
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = RED
    elif event.number == 7:
        print("six")
        trellis.pixels[event.number] = dimmed_colors(WHITE)
        for chase_on in range(num_pixels):
            pixels[chase_on] = WHITE
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = WHITE
    elif event.number == 8:
        print("seven")
        trellis.pixels[event.number] = dimmed_colors(PURPLE)
        for chase_on in range(num_pixels):
            pixels[chase_on] = PURPLE
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = PURPLE
    elif event.number == 9:
        print("nine")
        trellis.pixels[event.number] = dimmed_colors(PURPLE)
        for strobe in range(num_pixels):
            pixels[strobe] = PURPLE
            pixels.show()
            time.sleep(0.05)
            pixels[strobe] = OFF
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = PURPLE
    elif event.number == 10:
        print("ten")
    elif event.number == 11:
        print("eleven")
    elif event.number == 12:
        print("twelve")
    elif event.number == 13:
        print("thirteen")
    elif event.number == 14:
        print("fourteen")

        def wheel(pos):

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

        while True:
            rainbow_cycle(0.01)    # rainbow cycle with 1ms delay per step

    elif event.number == 15:
        print("fifteen")
        trellis.pixels[event.number] = dimmed_colors(OFF)
        for chase_on in range(num_pixels):
            pixels[chase_on] = OFF
            pixels.show()
            time.sleep(0.05)
        trellis.pixels[event.number] = OFF

'''
    if event.edge == NeoTrellis.EDGE_RISING:
        trellis.pixels[event.number] = dimmed_colors(COLORS[event.number])
        for chase_off in range(num_pixels):  # chase LEDs off
            pixels[chase_off] = (OFF)
            pixels.show()
            time.sleep(0.005)

        for chase_on in range(num_pixels):  # chase LEDs on
            pixels[chase_on] = (COLORS[event.number])
            pixels.show()
            time.sleep(0.005)

    # turn the trellis LED back to full color when a rising edge is detected
    elif event.edge == NeoTrellis.EDGE_FALLING:
        trellis.pixels[event.number] = COLORS[event.number]

'''

# boot up animation on trellis
trellis.pixels.brightness = 0.8
for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink

    # light the trellis LEDs on startup
    trellis.pixels[0] = DM_RED
    trellis.pixels[1] = YELLOW
    trellis.pixels[2] = PINK
    trellis.pixels[3] = GREEN
    trellis.pixels[4] = BLUE
    trellis.pixels[5] = CYAN
    trellis.pixels[6] = RED
    trellis.pixels[7] = WHITE
    trellis.pixels[8] = PURPLE
    trellis.pixels[9] = OFF
    trellis.pixels[10] = OFF
    trellis.pixels[11] = OFF
    trellis.pixels[12] = OFF
    trellis.pixels[13] = OFF
    trellis.pixels[14] = OFF
    trellis.pixels[15] = OFF
    time.sleep(.05)

print("Cajita Chicarica is on")

while True:

    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 milliseconds or so
    time.sleep(.02)