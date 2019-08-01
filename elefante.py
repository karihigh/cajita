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
num_pixels = 34

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
unpixel = pixels[1]
print(unpixel)

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
DM_CYAN = (0, 50, 120)
BLUE = (0, 10, 230)
PURPLE = (80, 0, 240)
ORANGE = (255, 30, 0)
DM_ORANGE = (200, 40, 0)
PINK = (255, 0, 100)
WHITE = (255, 255, 255)
DM_WHITE = (100, 100, 100)
ORDER = neopixel.GRB

pixels.fill(DM_RED)  # turn on the strip
pixels.show()

# listener DO NOT TOUCH
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
    elif event.number == 8:
        global boton
        boton = 8
    elif event.number == 9:
        global boton
        boton = 9
    elif event.number == 10:
        global boton
        boton = 10
    elif event.number == 11:
        global boton
        boton = 11
    elif event.number == 12:
        global boton
        boton = 12
    elif event.number == 13:
        global boton
        boton = 13
    elif event.number == 14:
        global boton
        boton = 14
    elif event.number == 15:
        global boton
        boton = 15

def blinkwrite(boton):
    if boton == 14:
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
        rainbow_cycle(0.01)    # rainbow cycle with 1ms delay per step

    elif boton == 0:
        pixels.fill(DM_RED)
        pixels.show()

    elif boton == 1:
        pixels.fill(BLUE)
        pixels.show()

    elif boton == 2:
        pixels.fill(ORANGE)
        pixels.show()
        
    elif boton == 3:
        pixels.fill(PURPLE)
        pixels.show()

    elif boton == 4:
        def strobe():
            
            global count
            if count < num_pixels:
                pixels.fill(PURPLE)
                pixels.show()
                time.sleep(0.61)
                pixels.fill(GREEN)
                pixels.show()
                time.sleep(0.61)
                count += 1
                if count >= num_pixels:
                    count = 0
        strobe()

    elif boton == 5:
        pixels.fill(PINK)
        pixels.show()

    elif boton == 6:
        pixels.fill(PURPLE)
        pixels.show()

    elif boton == 7:
        pixels.fill(CYAN)
        pixels.show()

    elif boton == 8:
        def chase():
            
            global count
            if count < num_pixels:
                for i in range(num_pixels):  # chase LEDs off
                    pixels[i] = (CYAN)
                    pixels.show()
                    time.sleep(0.876)
                for i in range(num_pixels):  # chase LEDs off
                    pixels[i] = (ORANGE)
                    pixels.show()
                    time.sleep(0.876)
                count += 1
                if count >= num_pixels:
                    count = 0
        chase()    

    elif boton == 9:
        pixels.fill(PINK)
        pixels.show()

    elif boton == 10:
        pixels.fill(RED)
        pixels.show()

    elif boton == 11:
        def strobe():
            
            global count
            if count < num_pixels:
                pixels.fill(RED)
                pixels.show()
                time.sleep(0.423)
                pixels.fill(DM_RED)
                pixels.show()
                time.sleep(0.423)
                count += 1
                if count >= num_pixels:
                    count = 0
        strobe()
    
    elif boton == 12:
        pixels.fill(GREEN)
        pixels.show()
        
    elif boton == 13:
        pixels.fill(PURPLE)
        pixels.show()
    
    elif boton == 15:
        pixels.fill(OFF)
        pixels.show()

trellis.pixels.brightness = 0.2

for i in range(16):
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # print(trellis.callbacks[i])
    trellis.callbacks[i] = blinkread

    trellis.pixels[0] = RED
    trellis.pixels[1] = BLUE
    trellis.pixels[2] = ORANGE
    trellis.pixels[3] = PURPLE
    trellis.pixels[4] = CYAN
    trellis.pixels[5] = PINK
    trellis.pixels[6] = PURPLE
    trellis.pixels[7] = CYAN
    trellis.pixels[8] = ORANGE
    trellis.pixels[9] = PINK
    trellis.pixels[10] = RED
    trellis.pixels[11] = RED
    trellis.pixels[12] = GREEN
    trellis.pixels[13] = PURPLE
    trellis.pixels[14] = DM_WHITE
    trellis.pixels[15] = OFF
    time.sleep(.05)

print("Cajita Chicarica is on")

while True:
    trellis.sync()
    blinkwrite(boton)
    time.sleep(.02)