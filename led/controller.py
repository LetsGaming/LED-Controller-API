import threading
from rpi_ws281x import *
from led.animations.standardAnimations import *
from led.animations.customAnimations import *
from led.animations.specialAnimations import *
from led.utils import validate_rgb_values, is_within_range


LED_COUNT = 300
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

class LEDController():
    def __init__(self):
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()
        self.current_animation = None
        self.animation_event = threading.Event()

    def get_brightness(self):
        """Returns the current strip's brightness level (between 0-255)."""
        return self.strip.getBrightness()

    def set_brightness(self, value):
        try:
            brightness = int(value)
            if brightness > -1 and brightness < 256:
                self.strip.setBrightness(brightness)
                self.strip.show()
                return True
            else: 
                print("Value not between allowed range")
                return False
        except Exception as e:
            print(e) 
            return False

    def set_white(self):
        """Set all pixels to white."""
        return self.fill_color(255, 255, 255)

    def fill_color(self, red, green, blue):
        """Fills all pixels in a specific color"""
        try:
            if validate_rgb_values(red, green, blue):
                self.stop_current_animation()
                if is_within_range(red, 225, 255) and is_within_range(green, 225, 255) and is_within_range(blue, 225, 255) and self.strip.getBrightness() > 127:
                    self.strip.setBrightness(127)
                    self.strip.show()
                color = Color(red, green, blue)
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, color)
                self.strip.show()
                return True
            else:
                return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False
        
    def custom_fill(self, red, green, blue, percentage):
        """Fills a certain amount of the pixels with a given color"""
        try:
            if validate_rgb_values(red, green, blue):
                self.stop_current_animation()
                color = Color(red, green, blue)
                # Calculate the number of pixels to fill based on the percentage
                num_pixels = int(self.strip.numPixels() * (int(percentage) / 100.0))

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
        
    def stop_current_animation(self):
        """Stops the currently running animation if any."""
        if self.current_animation is not None:
            self.current_animation.stop()
            self.current_animation = None
        self.animation_event.set()  # Signal that animation has stopped

    def start_animation(self, animation):
        """Starts a new animation after stopping the current animation."""
        self.stop_current_animation()
        self.animation_event.wait()  # Wait for animation to stop
        self.animation_event.clear()  # Reset the event for the next animation
        self.current_animation = animation
        animation_thread = threading.Thread(target=self.current_animation.start)
        animation_thread.start()

    def isAnimationStarted(self):
        return self.current_animation.isStarted()

    def blink(self, red, green, blue, blinking_speed):
        animation = Blink(self.strip, red, green, blue, blinking_speed)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def fade(self, from_red, from_green, from_blue, to_red, to_green, to_blue, steps, fading_speed):
        animation = Fade(self.strip, from_red, from_green, from_blue, to_red, to_green, to_blue, steps, fading_speed)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def sparkle(self, red, green, blue, sparkle_count):
        animation = Sparkle(self.strip, red, green, blue, sparkle_count)
        self.start_animation(animation)
        return self.isAnimationStarted()
    
    def scanner_effect(self, red, green, blue, scan_speed, tail_length):
        animation = ScannerEffect(self.strip, red, green, blue, scan_speed, tail_length)
        self.start_animation(animation)
        return self.isAnimationStarted()
    
    def yoyo_theater(self, red, green, blue, yoyo_speed):
        animation = YoyoTheater(self.strip, red, green, blue, yoyo_speed)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def breathing_effect(self, red, green, blue, breathing_speed):
        animation = Breathing_Effect(self.strip, red, green, blue, breathing_speed)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def color_wipe(self, red, green, blue):
        animation = Color_Wipe(self.strip, red, green, blue)
        self.start_animation(animation)
        return self.isAnimationStarted()
    
    def theater_chase(self, red, green, blue):
        animation = Theater_Chase(self.strip, red, green, blue)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def strobe(self, red, green, blue):
        animation = Strobe(self.strip, red, green, blue)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def color_chase(self, red, green, blue):
        animation = Color_Chase(self.strip, red, green, blue)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def rainbow_cycle(self):
        animation = Rainbow_Cycle(self.strip)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def rainbow_comet(self):
        animation = Rainbow_Comet(self.strip)
        self.start_animation(animation)
        return self.isAnimationStarted()

    def theater_chase_rainbow(self):
        animation = Theater_Chase_Rainbow(self.strip)
        self.start_animation(animation)
        return self.isAnimationStarted()
