import time
import random
from led.utils import *

def fill_color(strip, red, green, blue):
    """Fills all pixels in a specific color"""
    try:
        if validate_rgb_values(red, green, blue):
            if is_within_range(red, 225, 255) and is_within_range(green, 225, 255) and is_within_range(blue, 225, 255):
                strip.setBrightness(127)
                strip.show()
            color = Color(red, green, blue)
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
            strip.show()
            return True
        else:
            return False
    except Exception as e:
            print(f"Something went wrong: {e}")
            return False

class Blink(Animation):
    """Blink all LEDs on and off."""
    def __init__(self, strip, red, green, blue, blinking_speed):
        super().__init__(self._blink)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue
        self.blinking_speed = int(blinking_speed)

    def _blink(self):
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                self.animationStarted = True
                while not self.stopAnimation:
                    if self.stopAnimation:
                        break
                    fill_color(self.strip, self.red, self.green, self.blue)
                    time.sleep(1 / self.blinking_speed)
                    fill_color(self.strip, 0, 0, 0)
                    time.sleep(1 / self.blinking_speed)
                    if self.stopAnimation:
                        break
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False


class Fade(Animation):
    """Fade the LEDs from one color to another."""
    def __init__(self, strip, from_red, from_green, from_blue, to_red, to_green, to_blue, steps, fading_speed):
        super().__init__(self._fade)
        self.strip = strip
        self.from_red = from_red
        self.from_green = from_green
        self.from_blue = from_blue
        self.to_red = to_red
        self.to_green = to_green
        self.to_blue = to_blue
        self.fading_speed = int(fading_speed)
        self.steps = int(steps)
        self.direction = 1  # 1 for forward, -1 for backward

    def _fade(self):
        try:
            if validate_rgb_values(self.from_red, self.from_green, self.from_blue) and validate_rgb_values(
                    self.to_red, self.to_green, self.to_blue):
                self.animationStarted = True
                while not self.stopAnimation:
                    for step in range(self.steps):
                        if self.stopAnimation:
                            break
                        red = int(self.from_red + (self.to_red - self.from_red) * (step / self.steps))
                        green = int(self.from_green + (self.to_green - self.from_green) * (step / self.steps))
                        blue = int(self.from_blue + (self.to_blue - self.from_blue) * (step / self.steps))
                        fill_color(self.strip, red, green, blue)
                        time.sleep(0.08)
                        if self.stopAnimation:
                            break
                    self.direction *= -1  # Reverse the direction
                    self.from_red, self.to_red = self.to_red, self.from_red
                    self.from_green, self.to_green = self.to_green, self.from_green
                    self.from_blue, self.to_blue = self.to_blue, self.from_blue
                    time.sleep(1 / self.fading_speed)
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False

class Sparkle(Animation):
    """Create a sparkling effect on the LEDs."""
    def __init__(self, strip, red, green, blue, sparkle_count):
        super().__init__(self._sparkle)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue
        self.sparkle_count = int(sparkle_count)

    def _sparkle(self):
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                num_pixels = self.strip.numPixels()
                self.animationStarted = True
                while not self.stopAnimation:
                    for i in range(num_pixels):
                        if self.stopAnimation:
                            break
                        self.strip.setPixelColor(i, 0)
                    self.strip.show()
                    for _ in range(self.sparkle_count):
                        if self.stopAnimation:
                            break
                        pixel_index = random.randint(0, num_pixels)
                        brightness = random.uniform(0.5, 1.5)
                        darkened_color = Color(int(self.red * brightness), int(self.green * brightness), int(self.blue * brightness))
                        self.strip.setPixelColor(pixel_index, darkened_color)
                    self.strip.show()
                    time.sleep(.8)
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False

class ScannerEffect(Animation):
    """Create a scanner animation with a tail."""
    def __init__(self, strip, red, green, blue, scan_speed, tail_length):
        super().__init__(self._scanner_effect)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue
        self.scan_speed = int(scan_speed)
        self.tail_length = int(tail_length)

    def _scanner_effect(self):
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                num_pixels = self.strip.numPixels()
                self.animationStarted = True

                while not self.stopAnimation:
                    for i in range(num_pixels):
                        if self.stopAnimation:
                            break

                        # Turn off all pixels
                        for j in range(num_pixels):
                            self.strip.setPixelColor(j, 0)

                        # Set the current pixel color
                        self.strip.setPixelColor(i, Color(self.red, self.green, self.blue))

                        # Set tail colors
                        for k in range(1, self.tail_length + 1):
                            tail_index = (i - k) % num_pixels
                            tail_brightness = int(255 * (self.tail_length - k) / self.tail_length)
                            self.strip.setPixelColor(tail_index, Color(
                                int(self.red * tail_brightness / 255),
                                int(self.green * tail_brightness / 255),
                                int(self.blue * tail_brightness / 255)
                            ))

                        self.strip.show()
                        time.sleep(1 / self.scan_speed)

                    for i in range(num_pixels - 2, 0, -1):
                        if self.stopAnimation:
                            break

                        # Turn off all pixels
                        for j in range(num_pixels):
                            self.strip.setPixelColor(j, 0)

                        # Set the current pixel color
                        self.strip.setPixelColor(i, Color(self.red, self.green, self.blue))

                        # Set tail colors
                        for k in range(1, self.tail_length + 1):
                            tail_index = (i + k) % num_pixels
                            tail_brightness = int(255 * (self.tail_length - k) / self.tail_length)
                            self.strip.setPixelColor(tail_index, Color(
                                int(self.red * tail_brightness / 255),
                                int(self.green * tail_brightness / 255),
                                int(self.blue * tail_brightness / 255)
                            ))

                        self.strip.show()
                        time.sleep(1 / self.scan_speed)
            else:
                print("Couldn't validate colors")
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False

class YoyoTheater(Animation):
    """Create a animation that goes down the strip with a yoyo and theater style"""
    def __init__(self, strip, red, green, blue, yoyo_speed):
        super().__init__(self._yoyo_theater)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue
        self.yoyo_speed = int(yoyo_speed)
        self.tail_length = 8

    def _yoyo_theater(self):
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                num_pixels = self.strip.numPixels()
                scan_range = num_pixels * 2 - 2
                self.animationStarted = True

                while not self.stopAnimation:
                    for i in range(scan_range):
                        if self.stopAnimation:
                            break
                        for j in range(num_pixels):
                            self.strip.setPixelColor(j, 0)

                        if i < num_pixels:
                            pixel_index = i
                        else:
                            pixel_index = scan_range - i

                        brightness = 255 - int((pixel_index / num_pixels) * (self.tail_length + 1) * 255 / num_pixels)
                        color = Color(int(self.red * (brightness / 255)), int(self.green * (brightness / 255)), int(self.blue * (brightness / 255)))

                        for j in range(self.tail_length):
                            tail_pixel_index = pixel_index - j - 1
                            if tail_pixel_index >= 0:
                                tail_brightness = int((self.tail_length - j) * brightness / (self.tail_length + 1))
                                tail_color = Color(int(self.red * (tail_brightness / 255)), int(self.green * (tail_brightness / 255)), int(self.blue * (tail_brightness / 255)))
                                self.strip.setPixelColor(tail_pixel_index, tail_color)

                        tail_end_index = pixel_index - self.tail_length - 1
                        if tail_end_index >= 0:
                            for j in range(tail_end_index, -1, -1):
                                tail_brightness = int((j + 1) * brightness / (self.tail_length + 2))
                                tail_color = Color(int(self.red * (tail_brightness / 255)), int(self.green * (tail_brightness / 255)), int(self.blue * (tail_brightness / 255)))
                                self.strip.setPixelColor(j, tail_color)

                        self.strip.setPixelColor(pixel_index, color)
                        self.strip.show()

                        time.sleep(self.yoyo_speed / (scan_range * num_pixels))

                    self.strip.setPixelColor(num_pixels - 1, 0)
                    self.strip.show()

            else:
                print("Couldn't Validate Colors")
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False

class Breathing_Effect(Animation):
    def __init__(self, strip, red, green, blue, breathing_duration):
        super().__init__(self._breathing_effect)
        self.strip = strip
        self.red = red
        self.green = green
        self.blue = blue
        self.breathing_duration = int(breathing_duration)

    def _breathing_effect(self):
        """Create a breathing effect by gradually changing the brightness of the color."""
        try:
            if validate_rgb_values(self.red, self.green, self.blue):
                color = Color(self.red, self.green, self.blue)
                brightness_steps = 50
                brightness_increment = 255 / brightness_steps
                self.animationStarted = True
                while not self.stopAnimation:
                    # Increase brightness
                    for i in range(brightness_steps):
                        if self.stopAnimation:
                            break
                        if i>1:
                            brightness = int(brightness_increment * i)
                        else:
                            brightness = int(brightness_increment * (i + 1))
                        self.strip.setBrightness(brightness)
                        self.strip.show()
                        time.sleep(self.breathing_duration / brightness_steps)
                        for j in range(self.strip.numPixels()):
                            if self.stopAnimation:
                                break
                            self.strip.setPixelColor(j, color)
                    # Decrease brightness
                    for i in range(brightness_steps, -1, -1):
                        if self.stopAnimation:
                            break
                        brightness = int(brightness_increment * i)
                        self.strip.setBrightness(brightness)
                        self.strip.show()
                        time.sleep(self.breathing_duration / brightness_steps)
                        for j in range(self.strip.numPixels()):
                            if self.stopAnimation:
                                break
                            self.strip.setPixelColor(j, color)

                    if self.stopAnimation:
                        break
            else:
                print("Couldn't Validate Colors")
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False
