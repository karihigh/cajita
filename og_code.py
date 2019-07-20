# Microcontrolador Feather M4
# NeoTrellis: botonera de 16 botones conectada al controlador. 
# Cada botón tiene un LED (Pixel)
# Cinta led conectada a pin 5 (Pixels)

# liberías
import time
import board
from board import SCL, SDA
import busio
# esta es la librería para los leds
import neopixel
# esta es la librería para la botonera
from adafruit_neotrellis.neotrellis import NeoTrellis
from digitalio import DigitalInOut, Direction

# esto es para agregarle un botón extra a la caja de on y off que no estoy usando
button_LED = DigitalInOut(board.D13)
button_LED.direction = Direction.OUTPUT
button_LED.value = True

# definir pin y cantidad de pixeles en una lista
pixel_pin = board.D5
num_pixels = 120

# definir el objeto de pixeles
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# definir objeto del trellis
trellis = NeoTrellis(i2c_bus)

# definición de colores RGB
OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
YELLOW_GREEN = (127, 255, 0)
CYAN = (0, 255, 255)
LIGHT_BLUE = (0, 127, 255)
BLUE = (0, 0, 255)
PURPLE = (127, 0, 255)
ORANGE = (255, 80, 0)
PINK = (255, 0, 255)
ROUGE = (255, 0, 127)
WHITE = (100, 100, 100)
WHITE_WARM = (120, 100, 80)
WHITE_COOL = (80, 100, 120)
WHITE_GREEN = (80, 120, 100)

# Una lista de colores
COLORS = [ 
    RED, ORANGE, YELLOW, YELLOW_GREEN,
    GREEN, CYAN, LIGHT_BLUE, BLUE,
    PURPLE, PINK, ROUGE, WHITE,
    WHITE_WARM, WHITE_COOL, WHITE_GREEN, OFF
]

# .fill define el color de los leds, .show los enciende.
pixels.fill(COLORS[1])  # turn on the strip
pixels.show()

# Función que atenúa los colores definidos para cuando se apreta un botón
def dimmed_colors(color_values):
    (red_value, green_value, blue_value) = color_values
    return (red_value // 10, green_value // 10, blue_value // 10)

# Función que recibe cuando se apreta un botón y cuando se suelta (definida en línea 110)
# EDGE_RISING es cuando se apreta
# EDGE_FALLING es cuando suelta
def blink(event):
    # turn the trellis LED on when a rising edge is detected
    # do the chase for the NeoPixel strip

    # si el evento es RISING,
    if event.edge == NeoTrellis.EDGE_RISING:
        # dimmea el pixel del trellis 
        trellis.pixels[event.number] = dimmed_colors(COLORS[event.number])
        # hace un for por cada pixel definido arriba y le asigna el color a OFF
        for chase_off in range(num_pixels): 
            # define color (el .fill es reemplazado por la función chase_off)
            pixels[chase_off] = (OFF)
            # enciende con .show
            pixels.show()
            # agrega un delay
            time.sleep(0.005)
        # luego hace otro for por cada pixel (de atrás hacia adelante) y le asigna el color del botón
        for chase_on in range(num_pixels - 1, -1, -1):  # chase LEDs on
            pixels[chase_on] = (COLORS[event.number])
            pixels.show()
            time.sleep(0.03)

    # cuando el evento es FALLING, vuelve a poner los leds de los botones a full color
    # esto permite un feedback cuando se apretan los botones
    elif event.edge == NeoTrellis.EDGE_FALLING:
        trellis.pixels[event.number] = COLORS[event.number]

# esto le asigna la funcionalidad a cada botón
# aisgna el brillo a los pixeles de los botones
trellis.pixels.brightness = 0.2
# para cada botón (16) le asigna el evento de press y release
for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # cada vez que hay un callback, ejecuta la función "blink" que se usa arriba
    trellis.callbacks[i] = blink

    # light the trellis LEDs on startup
    # prende los pixels de la botonera según el orden del array de colores definido arriba
    trellis.pixels[i] = COLORS[i]
    time.sleep(.05)

# unos prints buena ondas
print("  Ambient Color Control Pad")
print("    ---press a button to change the ambient color---")

# siempre verdad nunca inverdad, el trellis.sync está siempre escuchando a los botones
while True:

    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 milliseconds or so
    time.sleep(.02)

# la gran pregunta es: 
# cómo puedo leer en la consola, hacer un print() del event.number (línea 80)

# esto me da error porque dice que "number" no está definido y no puedo encontrar ese número
# print(event.number)

# lo que quiero hacer son loops independientes por cada event.number pero que siempre esté escuchando
# si hago loops ahora, se queda para siempre en ese y si apreto otro botón no pasa nada
# creo que la lógica que tengo que escribir es: 

# while event.number == 1
#   for (shuper efecto)
# escucha por mientras si es que algo cambia
# if event.number == 2
#   for (otro shuper efecto)
# etc etc etc