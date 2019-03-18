
class Image:
    """Images can be displayed on the Micro:Bit's LED matrix."""

    def __init__(self, string = None, width=None, height=None, buffer=None):
        """Can be initialised in different ways:
        Image() = Blank 5x5 canvas
        Image(string) = image from passing in a string, a single character returns an image of that character
        Image(width, height) = Blank image with specific width and height
        Image(width, height, buffer) = image created from buffer contents"""
        a = string
    
    def width(self):
        """gets the number of columns in an image"""
        return 5
    
    def height(self):
        """gets the number of rows in an image"""
        return 5
    
    def set_pixel(self,x,y,value):
        """sets the brightness of a pixel at the given position
        Cannot be used on inbuilt images."""
        a = 0
    
    def get_pixel(self,x,y):
        """returns the brightness of the pixel located at x,y"""
        return 9
    
    def shift_left(self,n):
        """returns a new image created by shifting the image left by n columns"""
        return Image()

    def shift_right(self,n):
        """returns a new image created by shifting the image right by n columns"""
        return Image()
    
    def shift_up(self,n):
        """returns a new image created by shifting the image up by n rows"""
        return Image()
    
    def shift_down(self,n):
        """returns a new image created by shifting the image down by n rows"""
        return Image()
    
    def crop(self,x,y,w,h):
        """return a new image by cropping the picture to a width of w and a height of h, starting with the pixel at column x and row y."""
        return Image()
    
    def copy(self):
        """return an exact copy of the image"""
        return self
    
    def invert(self):
        """return a new image by inverting the brightness of the pixels in the source image."""
        return Image()

    def fill(self, value):
        """Return a new image by inverting the brightness of the pixels in the source image.
        Cannot be used on inbuilt images."""
        return Image()
    
    def blit(self, src, x, y, w, h, xdest=0, ydest=0):
        """Copy the rectangle defined by x, y, w, h from the image src into this image at xdest, ydest. Areas in the source rectangle, but outside the source image are treated as having a value of 0."""
        a = 0

    HEART = ""
    HEART_SMALL = ""

    HAPPY = ""
    SMILE = ""
    SAD = ""
    CONFUSED = ""
    ANGRY = ""
    ASLEEP = ""
    SURPRISED = ""
    SILLY = ""
    FABULOUS = ""
    MEH = ""

    YES = ""
    NO = ""

    CLOCK12 = ""
    CLOCK11 = ""
    CLOCK10 = ""
    CLOCK9 = ""
    CLOCK8 = ""
    CLOCK7 = ""
    CLOCK6 = ""
    CLOCK5 = ""
    CLOCK4 = ""
    CLOCK3 = ""
    CLOCK2 = ""
    CLOCK1 = ""

    ARROW_N = ""
    ARROW_NE = ""
    ARROW_E = ""
    ARROW_SE = ""
    ARROW_S = ""
    ARROW_SW = ""
    ARROW_W = ""
    ARROW_NW = ""
    
    TRIANGLE = ""
    TRIANGLE_LEFT = ""
    CHESSBOARD = ""
    DIAMOND = ""
    DIAMOND_SMALL = ""
    SQUARE = ""
    SQUARE_SMALL = ""
    
    RABBIT = ""
    COW = ""

    MUSIC_CROTCHET = ""
    MUSIC_QUAVER = ""
    MUSIC_QUAVERS = ""

    PITCHFORK = ""

    XMAS = ""

    PACMAN = ""
    TARGET = ""
    TSHIRT = ""
    ROLLERSKATE = ""
    DUCK = ""
    HOUSE = ""
    TORTOISE = ""
    BUTTERFLY = ""
    STICKFIGURE = ""
    GHOST = ""
    SWORD = ""
    GIRAFFE = ""
    SKULL = ""
    UMBRELLA = ""
    SNAKE = ""


class _Button():
    """Physical button on the Microbit board"""

    def is_pressed(self):
        """Returns True if the button is being pressed"""
        return True
    
    def was_pressed(self):
        """Returns True if the button has been pressed since this was last called"""
        return True
    
    def get_presses(self):
        """Returns the number of times the button has been pressed since this method was last called, then resets the count"""
        return 10

    def __init__(self):
        a = 0

class _Buttons():
    """Holder of the buttons"""
    def __init__(self):
        self.button_a = _Button()
        self.button_b = _Button()

class _MicroBitDigitalPin:
    """Digital pin on the Micro:Bit board"""

    def read_digital(self):
        """Return 1 if the pin is high, and 0 if it's low"""
        return 1
    
    
    def write_digital(self,value):
        """Set the pin to High if the value is 1, or else set it to 0"""
        a = value

    def __init__(self):
        a = 0

class _MicroBitAnalogDigitalPin:
    """Analog (PWM) pin on the Micro:Bit board"""

    def read_analog(self):
        """Reads the voltage applied to the pin, and return it as an integer between 0 (0V), and 1024 (3.3V)"""
        return 1023
    
    
    def write_analog(self,value):
        """Output a PWM signal on the pin, with a duty cycle proportional to provided value, where 0 = 0%, and 1023 = 100%"""
        a = value
    
    
    def set_analog_period(self,period):
        """Set the period of the PWM signal being output to period in ms. Minimum valid is 1ms"""
        a = period
    
    
    def set_analog_period_microseconds(self,period):
        """Set the period of the PWM signal being output to period in microseconds. Minimum valid is 256"""
        a = period
    
    def __init__(self):
        a = 0

class _MicroBitTouchPin:
    """Touch sensitive pin on the Micro:Bit board"""

    def is_touched(self):
        """Return True if the pin is being touched, otherwise False"""
        return True

    def __init__(self):
        a = 0

class _MicroBitAnalogDigitalPinReadOnly:
    """Read only PWM pin"""

    def read_analog(self):
        """Reads the voltage applied to the pin, and return it as an integer between 0 (0V), and 1024 (3.3V)"""
        return 1023
    
    def __init__(self):
        a = 0

class microbit:
    """Base Micro:Bit class from which everything else can be accessed."""
    
    def panic(self, error_code):
        """Enter a panic mode. Requires restart. Pass in an arbitrary integer <= 255 to indicate a status"""
        s = error_code

    def reset(self):
        """Restart the board."""
        a = 0

    def sleep(self,milliseconds):
        """Wait for n milliseconds. One second is 1000 milliseconds, so:"""
        a = milliseconds

    def running_time(self):
        """Return the number of milliseconds since the board was switched on or restarted."""
        return 10

    def temperature(self):
        """Return the temperature of the micro:bit in degrees Celcius."""
        return 26.2

    def __init__(self):
        self.Buttons = _Buttons()
        self.pin0 = _MicroBitTouchPin()
        self.pin1 = _MicroBitTouchPin()
        self.pin2 = _MicroBitTouchPin()

        self.pin3 = _MicroBitAnalogDigitalPin()
        self.pin4 = _MicroBitAnalogDigitalPin()
        self.pin5 = _MicroBitDigitalPin()
        self.pin6 = _MicroBitDigitalPin()
        self.pin7 = _MicroBitDigitalPin()
        self.pin8 = _MicroBitDigitalPin()
        self.pin9 = _MicroBitDigitalPin()

        self.pin10 = _MicroBitAnalogDigitalPin()

        self.pin11 = _MicroBitDigitalPin()
        self.pin12 = _MicroBitAnalogDigitalPin()
        self.pin13 = _MicroBitDigitalPin()
        self.pin14 = _MicroBitDigitalPin()
        self.pin15 = _MicroBitDigitalPin()
        self.pin16 = _MicroBitDigitalPin()

        self.pin19 = _MicroBitDigitalPin()
        self.pin20 = _MicroBitDigitalPin()
        
        