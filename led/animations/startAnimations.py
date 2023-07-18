from led.utils import *

class SetWhite(Animation):
    """Set all pixels to white and halfs the brightness."""
    def __init__(self, strip):
        super().__init__(self._set_white)
        self.strip = strip

    def _set_white(self):
        try:
            white = Color(255,255,255)
            self.animationStarted = True
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, white)
            self.strip.setBrightness(127)
            self.strip.show()
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False

class FillColor(Animation):
    """Fills all pixels in a specific color"""
    def __init__(self, strip, red, green, blue):
        super().__init__(self._fill_color)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue

    def _fill_color(self):
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                
                if is_within_range(self.red, 225, 255) and is_within_range(self.green, 225, 255) and is_within_range(self.blue, 225, 255) and self.strip.getBrightness() > 127:
                    self.strip.setBrightness(127)
                    self.strip.show()
                color = Color(self.red, self.green, self.blue)
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, color)
                self.strip.show()
                return True
            else:
                return False
        except Exception as e:
                print(f"Something went wrong: {e}")
                return False

class CustomFill(Animation):
    """Fills a certain amount of the pixels with a given color"""
    def __init__(self, strip, red, green, blue, percentage):
        super().__init__(self._custom_fill)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue
        self.percentage = percentage

    def _custom_fill(self):
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                color = Color(self.red, self.green, self.blue)
                # Calculate the number of pixels to fill based on the percentage
                num_pixels = int(self.strip.numPixels() * (int(self.percentage) / 100.0))

                self.animationStarted = True
                # Fill the strip with the specified color
                for i in range(num_pixels):
                    self.strip.setPixelColor(i, color)
                    self.strip.show()

                # Turn off remaining pixels
                for i in range(num_pixels, self.strip.numPixels()):
                    self.strip.setPixelColor(i, Color(0, 0, 0))
                self.strip.show()
                return True
            else:
                return False

        except Exception as e:
            print(f"Something went wrong: {e}")
            return False
