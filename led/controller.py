import threading
from rpi_ws281x import *
from led.animations.startAnimations import *
from led.animations.standardAnimations import *
from led.animations.customAnimations import *
from led.animations.specialAnimations import *


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
        self.paused_animation = None
        self.animation_event = threading.Event()
        self.isOnline = False
        # Start with clearing the strip on startup
        self.clear_strip()

    def clear_strip(self):
        dark = Color(0,0,0)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, dark)
        self.strip.show()

    def get_online_state(self):
        return self.isOnline

    def set_online_state(self, value: bool):
        """Sets whether or not this device should be considered online by other devices."""
        try:
            if not self.isOnline and value and self.paused_animation is not None:
                self.isOnline = True
                self._resume_animation()
                return True
            elif self.isOnline and not value and self.paused_animation is None:
                self.isOnline = False
                self._pause_animation()
                return True
            else:
                self.isOnline = value
                return True
        except Exception as e:
            print("Error setting Online State:", str(e))
            return False

    def _pause_animation(self):
        self.paused_animation = self.current_animation
        self._stop_current_animation()

    def _resume_animation(self):
        if self.paused_animation is not None:
            self._start_animation(self.paused_animation)
        self.paused_animation = None

    def _stop_current_animation(self):
        """Stops the currently running animation if any."""
        if self.current_animation is not None:
            self.current_animation.stop()
            self.current_animation = None
        self.animation_event.set()  # Signal that animation has stopped

    def _start_animation(self, animation):
        """Starts a new animation after stopping the current animation."""
        self._stop_current_animation()
        self.animation_event.wait()  # Wait for animation to stop
        self.animation_event.clear()  # Reset the event for the next animation
        self.current_animation = animation
        animation_thread = threading.Thread(target=self.current_animation.start)
        animation_thread.start()

    def _is_animation_started(self):
        """Returns True if an animation is currently running."""
        return self.current_animation is not None

    def get_brightness(self):
        """Returns the current strip's brightness level (between 0-255)."""
        if self.isOnline:
            return self.strip.getBrightness()
        else:
            return "The LED-Strip is turned OFF!"

    def set_brightness(self, value):
        try:
            if self.isOnline:
                brightness = int(value)
                if brightness > -1 and brightness < 256:
                    self.strip.setBrightness(brightness)
                    self.strip.show()
                    return True
                else: 
                    print("Value not between allowed range")
                    return False
            else:
                return "The LED-Strip is turned OFF!"
        except Exception as e:
            print(e) 
            return False

    def set_white(self):
        if self.isOnline:
            animation = SetWhite(self.strip)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"
    
    def fill_color(self, red, green, blue):
        if self.isOnline:
            animation = FillColor(self.strip, red, green, blue)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"
        
    def custom_fill(self, red, green, blue, percentage):
        if self.isOnline:
            animation = CustomFill(self.strip, red, green, blue, percentage)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"

    def blink(self, red, green, blue, blinking_speed):
        if self.isOnline:
            animation = Blink(self.strip, red, green, blue, blinking_speed)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"

    def fade(self, from_red, from_green, from_blue, to_red, to_green, to_blue, steps, fading_speed):
        if self.isOnline:
            animation = Fade(self.strip, from_red, from_green, from_blue, to_red, to_green, to_blue, steps, fading_speed)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"

    def sparkle(self, red, green, blue, sparkle_count):
        if self.isOnline:
            animation = Sparkle(self.strip, red, green, blue, sparkle_count)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"
    
    def scanner_effect(self, red, green, blue, scan_speed, tail_length):
        if self.isOnline:
            animation = ScannerEffect(self.strip, red, green, blue, scan_speed, tail_length)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"
    
    def yoyo_theater(self, red, green, blue, yoyo_speed):
        if self.isOnline:
            animation = YoyoTheater(self.strip, red, green, blue, yoyo_speed)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"
        
    def breathing_effect(self, red, green, blue, breathing_speed):
        if self.isOnline:
            animation = Breathing_Effect(self.strip, red, green, blue, breathing_speed)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"
        
    def color_wipe(self, red, green, blue):
        if self.isOnline:
            animation = Color_Wipe(self.strip, red, green, blue)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"
        
    def theater_chase(self, red, green, blue):
        if self.isOnline:
            animation = Theater_Chase(self.strip, red, green, blue)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"

    def strobe(self, red, green, blue):
        if self.isOnline:
            animation = Strobe(self.strip, red, green, blue)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"

    def color_chase(self, red, green, blue):
        if self.isOnline:
            animation = Color_Chase(self.strip, red, green, blue)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"

    def rainbow_cycle(self):
        if self.isOnline:
            animation = Rainbow_Cycle(self.strip)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"

    def rainbow_comet(self):
        if self.isOnline:
            animation = Rainbow_Comet(self.strip)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"

    def theater_chase_rainbow(self):
        if self.isOnline:
            animation = Theater_Chase_Rainbow(self.strip)
            self._start_animation(animation)
            return self._is_animation_started()
        else:
            return "The LED-Strip is turned OFF!"
