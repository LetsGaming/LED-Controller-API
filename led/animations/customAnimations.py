import random
import time
from led.utils import *


class Color_Wipe(Animation):
    """Wipe color across display a pixel at a time."""
    def __init__(self, strip, red, green, blue):
        super().__init__(self.color_wipe)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue

    def color_wipe(self):
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
    """Movie theater light style chaser animation."""
    def __init__(self, strip, red, green, blue):
        super().__init__(self.theater_chase)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue

    def theater_chase(self): 
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
    """Create a strobe effect by rapidly turning the LEDs on and off."""
    def __init__(self, strip, red, green, blue):
        super().__init__(self.strobe)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue

    def strobe(self):
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
    """Create a animation that chases down the strip."""
    def __init__(self, strip, red, green, blue):
        super().__init__(self.color_chase)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue

        self.tail_length = 10
        self.wait_ms = 50

    def color_chase(self):
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                color = Color(self.red, self.green, self.blue)
                num_pixels = self.strip.numPixels()
                self.animationStarted = True
                while not self.stopAnimation:
                    if self.stopAnimation:
                        break
                    pixel_list = [-1] * num_pixels

                    # Randomly determine the starting position for the tail
                    start_position = random.randint(0, num_pixels - self.tail_length - 1)
                    for i in range(start_position, start_position + self.tail_length):
                        if self.stopAnimation:
                            break
                        pixel_list[i] = i - start_position

                    for i in range(num_pixels):
                        if self.stopAnimation:
                            break
                        # Shift the pixel list
                        for j in range(num_pixels - 1, 0, -1):
                            if self.stopAnimation:
                                break
                            pixel_list[j] = pixel_list[j - 1]

                        # Add the current pixel to the list
                        pixel_list[0] = i

                        # Display the tail
                        for j in range(self.tail_length):
                            if self.stopAnimation:
                                break
                            if pixel_list[j] >= 0:
                                self.strip.setPixelColor(pixel_list[j], color)

                        # Turn on the current pixel
                        self.strip.setPixelColor(i, color)
                        self.strip.show()

                        # Turn off the last pixel
                        if i >= self.tail_length :
                            self.strip.setPixelColor(i - self.tail_length , 0)
                            self.strip.show()

                        time.sleep(self.wait_ms / 1000.0)
                        if self.stopAnimation:
                            break
                    # Turn off the remaining tail
                    for i in range(self.tail_length):
                        if self.stopAnimation:
                            break
                        if pixel_list[i] >= 0:
                            self.strip.setPixelColor(pixel_list[i], 0)
                    self.strip.show()
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False
        
class CustomRainbow(Animation):
    """Displays a rainbow animation on the LED strip using the provided colors."""
    def __init__(self, strip, colors):
        super().__init__(self.custom_rainbow_animation)
        self.strip = strip
        self.colors = colors

    def custom_rainbow_animation(self):
        total_colors = len(self.colors)
        color_step = 256 // total_colors
        self.animationStarted = True
        while not self.stopAnimation:
            for i in range(self.strip.numPixels()):
                color_index = (i * color_step) % 256
                self.strip.setPixelColor(i, self.colors[color_index // color_step])
                self.strip.show()
                time.sleep(20 / 1000.0)
