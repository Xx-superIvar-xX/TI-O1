#Aansluiting is als volgt [LED Matrix naar Pico]:

 # VCC  pin naar VBUS (5V)
 # GND  pin naar GND
 # DIN  pin naar GPIO3
 # CS   pin naar GPIO5
 # CLK  pin naar GPIO2

from machine import Pin, SPI, ADC # pyright: ignore[reportMissingImports]
import utime # pyright: ignore[reportMissingImports]
import max7219 # pyright: ignore[reportMissingImports]


spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

# Instantieer matrix8x8 object. Met de laatste parameter geef je aan hoeveel matrices je hebt aangesloten.
display = max7219.Matrix8x8(spi, ss, 1)
display.brightness(10)  # Tussen 0 en 15
display.set_rotation(270)  # Zet de rotatie op 270 graden, dan is pixel (0,0) links bovenin.

# Clear the display.
display.fill(0)
display.show()

# Sleep for one second
utime.sleep_ms(1000)

keypad = ADC(Pin(26))

def readkeypad():
    val = keypad.read_u16()
    if val < 1000:
        return "left"
    elif val < 10000:
        return "up"
    elif val < 25000:
        return "down"
    elif val < 35000:
        return "right"
    elif val < 50000:
        return "action"
    else:
        return "nothing"

# Unconditionally execute the loop
def screensaver():
    while True:
        for x in range(8):
            for y in range(8):
                # Clear the display (frame buffer)
                display.fill(0)
                # Set a pixel at (x, y) to white (in the frame buffer)
                display.pixel(x, y, 1)
                # Show the frame buffer content on the display
                display.show()
                # Set the Scrolling speed. Here it is 100mS.
                utime.sleep_ms(100)

def main():
    while True:
        
if __name__ == "__main__":
    main()