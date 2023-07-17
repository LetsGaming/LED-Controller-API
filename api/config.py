start_animations = {
    'white': {
        'name': 'White',
        'description': '',
        'args': []
    },
    'custom_color': {
        'name': 'Custom Color',
        'description': 'Sets the color of the complete LED Strip',
        'args': ['red', 'green', 'blue']
    },
    'custom_fill': {
        'name': 'Custom Fill',
        'description': 'Fills a certain amount of the pixels with a given color',
        'args': ['red', 'green', 'blue', 'percentage']
    }
}

standard_animations = {
    'rainbow_cycle': {
        'name': 'Rainbow Cycle',
        'description': 'Smoothly transitions colors in a cyclical pattern resembling a rainbow.',
        'args': []
    },
    'rainbow_comet': {
        'name': 'Rainbow Comet',
        'description': 'Simulates a comet-like trail of rainbow colors.',
        'args': []
    },
    'theater_chase_rainbow': {
        'name': 'Theater Chase Rainbow',
        'description': 'Produces a theater chase effect with a rainbow of colors.',
        'args': []
    },
}

custom_animations = {
    'custom_rainbow': {
        'name': 'Custom Rainbow',
        'description': 'Displays a rainbow animation on the LED strip using the provided colors.',
        'args': ['colors'],
    },
    'color_wipe': {
        'name': 'Color Wipe',
        'description': 'Wipes the LED strip with a single color, creating a visually striking effect.',
        'args': ['red', 'green', 'blue']
    },
    'theater_chase': {
        'name': 'Theater Chase',
        'description': 'Creates a theater chase effect with custom colors.',
        'args': ['red', 'green', 'blue']
    },
    'strobe': {
        'name': 'Strobe',
        'description': 'Produces a strobe effect using custom colors.',
        'args': ['red', 'green', 'blue']
    },
    'color_chase': {
        'name': 'Color Chase',
        'description': 'Generates a chasing effect with custom colors.',
        'args': ['red', 'green', 'blue']
    }
}

special_animations = {
    'blink': {
        'name': 'Blink',
        'description': 'Repeatedly blinks the LED strip with a specified color combination.',
        'args': ['red', 'green', 'blue', 'blinking_speed']
    },
    'fade': {
        'name': 'Fade',
        'description': 'Gradually fades the LED strip from one color to another.',
        'args': ['from_red', 'from_green', 'from_blue', 'to_red', 'to_green', 'to_blue', 'steps', 'fading_speed']
    },
    'sparkle': {
        'name': 'Sparkle',
        'description': 'Adds sparkling effects to the LED strip by randomly illuminating individual LEDs.',
        'args': ['red', 'green', 'blue', 'sparkle_count']
    },
    'scanner_effect': {
        'name': 'Scanner Effect',
        'description': 'Creates a scanning effect by moving a single colored pixel back and forth.',
        'args': ['red', 'green', 'blue', 'scan_speed', 'tail_length']
    },
    'yoyo_theater': {
        'name': 'Yoyo Theater',
        'description': 'Creates a yoyo-like effect and lets the string colors bounce around',
        'args': ['red', 'green', 'blue', 'yoyo_speed']
    },
    'breathing_effect': {
        'name': 'Breathing Effect',
        'description': 'Create a breathing effect by gradually changing the brightness of the color.',
        'args': ['red', 'green', 'blue', 'breathing_duration']
    }
}
