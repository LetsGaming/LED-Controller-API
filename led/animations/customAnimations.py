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
                        self.strip.setPixelColor(i, color)  # Set pixel color to the specified color
                        self.strip.show()  # Update the LED strip with the new color
                        time.sleep(0.05)  # Pause for a short duration
                    for i in range(self.strip.numPixels()):
                        if self.stopAnimation:
                            break
                        self.strip.setPixelColor(i, 0)  # Set pixel color to black (turn off the pixel)
                        self.strip.show()  # Update the LED strip
                        time.sleep(0.05)  # Pause for a short duration
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
                                self.strip.setPixelColor(i + q, color)  # Set color to the pixel
                            self.strip.show()  # Update the LED strip
                            time.sleep(0.05)  # Pause for a short duration
                            if self.stopAnimation:
                                break
                            for i in range(0, self.strip.numPixels(), 3):
                                if self.stopAnimation:
                                    break
                                self.strip.setPixelColor(i + q, 0)  # Set pixel color to black (turn off the pixel)
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
                        self.strip.show()  # Update the LED strip
                        time.sleep(.5)  # Pause for a short duration
                        for _ in range(5):
                            if self.stopAnimation:
                                break
                            for i in range(num_pixels):
                                if self.stopAnimation:
                                    break
                                self.strip.setPixelColor(i, 0)  # Turn off all pixels
                            self.strip.show()  # Update the LED strip
                            time.sleep(.5)  # Pause for a short duration
                            if self.stopAnimation:
                                break
                            for i in range(num_pixels):
                                if self.stopAnimation:
                                    break
                                self.strip.setPixelColor(i, color)  # Turn on all pixels
                            self.strip.show()  # Update the LED strip
                            time.sleep(.5)  # Pause for a short duration
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
        # Animation parameters
        self.MIN_PIXELS = 5        # Minimum number of pixels to start moving
        self.MAX_PIXELS = 15       # Maximum number of pixels to start moving
        self.MIN_DELAY = 0.5       # Minimum delay between new pixel groups (in seconds)
        self.MAX_DELAY = 3.0       # Maximum delay between new pixel groups (in seconds)

    def color_chase(self):
        pixels = []  # List to store the current pixel positions
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                color = Color(self.red, self.green, self.blue)
                num_pixels = self.strip.numPixels()
                while not self.stopAnimation:
                    # Move existing pixels
                    for i in range(len(pixels)):
                        pixels[i] += 1  # Increment pixel position
                        if pixels[i] >= num_pixels:
                            pixels[i] = num_pixels - 1  # Wrap around to the last pixel

                    # Add new pixels randomly
                    num_new_pixels = random.randint(self.MIN_PIXELS, self.MAX_PIXELS)
                    new_pixels = [random.randint(0, num_pixels - 1) for _ in range(num_new_pixels)]
                    pixels.extend(new_pixels)

                    # Clearing all Pixels
                    for i in range(num_pixels):
                        self.strip.setPixelColor(i, 0)
                    self.strip.show()

                    # Render pixels on the LED strip
                    for pixel in pixels:
                        self.strip.setPixelColor(pixel, color)
                    self.strip.show()  # Update the LED strip

                    # Delay before the next update
                    delay = random.uniform(self.MIN_DELAY, self.MAX_DELAY)
                    time.sleep(delay)  # Pause for a random duration
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
