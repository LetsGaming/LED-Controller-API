import random
import time
from led.utils import *


class Color_Wipe(Animation):
    def __init__(self, strip, red, green, blue):
        super().__init__(self.color_wipe)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue

    def color_wipe(self):
        """Wipe color across display a pixel at a time."""
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                color = Color(self.red, self.green, self.blue)
                self.animationStarted = True
                while not self.stopAnimation:
                    for i in range(self.strip.numPixels()):
                        if self.stopAnimation:
                            break
                        self.strip.setPixelColor(i, color)
                        self.strip.show()
                        time.sleep(0.05)
                    for i in range(self.strip.numPixels()):
                        if self.stopAnimation:
                            break
                        self.strip.setPixelColor(i, 0)
                        self.strip.show()
                        time.sleep(0.05)
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False


class Theater_Chase(Animation):
    def __init__(self, strip, red, green, blue):
        super().__init__(self.theater_chase)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue

    def theater_chase(self):
        """Movie theater light style chaser animation."""
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                color = Color(self.red, self.green, self.blue)
                self.animationStarted = True
                while not self.stopAnimation:
                    for j in range(10):
                        if self.stopAnimation:
                            break
                        for q in range(3):
                            if self.stopAnimation:
                                break
                            for i in range(0, self.strip.numPixels(), 3):
                                if self.stopAnimation:
                                    break
                                self.strip.setPixelColor(i + q, color)
                            self.strip.show()
                            time.sleep(0.05)
                            if self.stopAnimation:
                                break
                            for i in range(0, self.strip.numPixels(), 3):
                                if self.stopAnimation:
                                    break
                                self.strip.setPixelColor(i + q, 0)
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False


class Strobe(Animation):
    def __init__(self, strip, red, green, blue):
        super().__init__(self.strobe)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue

    def strobe(self):
        """Create a strobe effect by rapidly turning the LEDs on and off."""
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                color = Color(self.red, self.green, self.blue)
                num_pixels = self.strip.numPixels()
                self.animationStarted = True
                while not self.stopAnimation:
                    for i in range(num_pixels):
                        if self.stopAnimation:
                            break
                        self.strip.setPixelColor(i, color)  # Set all pixels to the specified color
                        self.strip.show()
                        time.sleep(.5)
                        for _ in range(5):
                            if self.stopAnimation:
                                break
                            for i in range(num_pixels):
                                if self.stopAnimation:
                                    break
                                self.strip.setPixelColor(i, 0)  # Turn off all pixels
                            self.strip.show()
                            time.sleep(.5)
                            if self.stopAnimation:
                                break
                            for i in range(num_pixels):
                                if self.stopAnimation:
                                    break
                                self.strip.setPixelColor(i, color)  # Turn on all pixels
                            self.strip.show()
                            time.sleep(.5)
                            if self.stopAnimation:
                                break
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False


class Color_Chase(Animation):
    def __init__(self, strip, red, green, blue):
        super().__init__(self.color_chase)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue
        self.current_pixel = 0
        self.tail_length = random.randint(1, 5)  # Random tail length between 1 and 5 pixels

    def color_chase(self):
        """Chase a single color along the LED strip."""
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                color = Color(self.red, self.green, self.blue)
                num_pixels = self.strip.numPixels()
                self.animationStarted = True
                while not self.stopAnimation:
                    # Update tail
                    tail_start = max(self.current_pixel - self.tail_length, 0)
                    tail_end = self.current_pixel - 1
                    for i in range(tail_start, tail_end + 1):
                        self.strip.setPixelColor(i, color)
                    # Update current pixel
                    self.strip.setPixelColor(self.current_pixel, color)
                    if self.current_pixel > 0:
                        self.strip.setPixelColor(self.current_pixel - 1, 0)  # Clear previous pixel
                    self.strip.show()
                    time.sleep(0.08)
                    if self.stopAnimation:
                        break
                    if random.random() < 0.2:  # Randomly introduce a new pixel at the beginning
                        self.strip.setPixelColor(num_pixels - 1, 0)  # Clear last pixel
                        self.current_pixel = 0
                        self.tail_length = random.randint(1, 5)  # Random tail length between 1 and 5 pixels
                    else:
                        self.current_pixel = (self.current_pixel + 1) % num_pixels  # Move current pixel forward
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False
        
class CustomRainbow(Animation):
    def __init__(self, strip, colors):
        super().__init__(self.custom_rainbow_animation)
        self.strip = strip
        self.colors = colors

    def custom_rainbow_animation(self):
        """Displays a rainbow animation on the LED strip using the provided colors."""
        total_colors = len(self.colors)
        color_step = 256 // total_colors
        self.animationStarted = True
        while not self.stopAnimation:
            for i in range(self.strip.numPixels()):
                color_index = (i * color_step) % 256
                self.strip.setPixelColor(i, self.colors[color_index // color_step])
                self.strip.show()
                time.sleep(20 / 1000.0)
