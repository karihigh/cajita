# Cajita Chicarica
# NeoTrellis to select colors of NeoPixel strip
# NeoTrellis connected to Feather M4
# NeoPixel 136 strip connected to pin D5
# My version

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

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis object
trellis = NeoTrellis(i2c_bus)
boton = 17
count = 0

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


def blinkread(event):
    if event.number == 0:
        global boton
        boton = 0
    elif event.number == 1:
        global boton
        boton = 1
    elif event.number == 2:
        global boton
        boton = 2
    elif event.number == 3:
        global boton
        boton = 3
    elif event.number == 4:
        global boton
        boton = 4
    elif event.number == 5:
        global boton
        boton = 5
    elif event.number == 6:
        global boton
        boton = 6
    elif event.number == 7:
        global boton
        boton = 7
        
def blinkwrite(boton):
    print(boton)
    if boton == 0:
        print("zero")
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
                g = int(pos * 3)
                b = int(255 - pos*3)
            return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)
                
        def rainbow_cycle(wait):
            global count
            for j in range(255):
                if count < num_pixels:
                    pixel_index = (count * 256 // num_pixels) + j
                    pixels[count] = wheel(pixel_index & 255)
                    count += 1
                    if count >= num_pixels:
                        count = 0
                pixels.show()
                time.sleep(wait)
        rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step

    elif boton == 1:
        print("one")
        pixels.fill(CYAN)
        pixels.show()

    elif boton == 2:
        print("two")
        pixels.fill(ORANGE)
        pixels.show()
        
    elif boton == 3:
        print("three")
        pixels.fill(PINK)
        pixels.show()
        
    elif boton == 4:
        print("four")
        pixels.fill(PURPLE)
        pixels.show()

    elif boton == 5:
        print("five")
        pixels.fill(PINK)
        pixels.show()

    elif boton == 6:
        print("six")
        pixels.fill(ROUGE)
        pixels.show()

    elif boton == 7:
        print("six")
        pixels.fill(ORANGE)
        pixels.show()

    elif boton == 8:
        print("seven")
        pixels.fill(RED)
        pixels.show()

    elif boton == 9:
        print("nine")
        pixels.fill(GREEN)
        pixels.show()

    elif boton == 10:
        print("ten")
        pixels.fill(PURPLE)
        pixels.show()

    elif boton == 11:
        print("eleven")
        pixels.fill(PINK)
        pixels.show()

    elif boton == 12:
        print("twelve")
        pixels.fill(PINK)
        pixels.show()

    elif boton == 13:
        print("thirteen")
        pixels.fill(PINK)
        pixels.show()

    elif boton == 14:
        print("fourteen")

    elif boton == 15:
        pixels.fill(OFF)
        pixels.show()

trellis.pixels.brightness = 0.2

for i in range(16):
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    print(trellis.callbacks[i])
    trellis.callbacks[i] = blinkread

    trellis.pixels[0] = RED
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
    trellis.sync()
    blinkwrite(boton)
    time.sleep(.02)
