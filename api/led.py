from flask import Blueprint, jsonify, request
from led.controller import LEDController
from api.config import start_animations, standard_animations, custom_animations, special_animations

# Create the Flask blueprint and initialize LEDController
led_api = Blueprint('led_api', __name__)
led_controller = LEDController()

# LED strip control endpoints
@led_api.route('/led/set_online_state', methods=['POST'])
def set_online_state():
    data = request.get_json()
    value = data.get('online')
    if led_controller.set_online_state(value):
        return jsonify(message='Set State of strip.'), 200
    else:
        return jsonify(message='Failed setting state of strip'), 500

@led_api.route('/led/brightness', methods=['POST'])
def set_brightness():
    data = request.get_json()
    brightness = data.get('brightness')
    if led_controller.set_brightness(brightness):
        return jsonify(message='Set Brightness of Strip.'), 200
    else:
        return jsonify(message='Error setting brightness of strip.'), 500

@led_api.route('/led/getBrightness', methods=['GET'])
def get_brightness():
    response = { 'current_brightness': str(led_controller.get_brightness()) }
    return response

@led_api.route('/led/white', methods=['POST'])
def set_white():
    if led_controller.set_white():
        return jsonify(message='Strip color set to white.'), 200
    else:
        return jsonify(message='Failed setting strip color.'), 500

@led_api.route('/led/custom_color', methods=['POST'])
def fill_color():
    data = request.get_json()
    red, green, blue = data.get('red'), data.get('green'), data.get('blue')

    if led_controller.fill_color(red, green, blue):
        return jsonify(message='Filled strip with color.'), 200
    else:
        return jsonify(message='Error filling strip with color.'), 500

@led_api.route('/led/custom_fill', methods=['POST'])
def custom_fill():
    data = request.get_json()
    red, green, blue, percentage = data.get('red'), data.get('green'), data.get('blue'), data.get('percentage')
    if led_controller.custom_fill(red, green, blue, percentage):
        return jsonify(message='Filled amount of strip pixels with color.'), 200
    else:
        return jsonify(message='Error filling amount of strip pixels with color.'), 500

# Animation endpoints
@led_api.route('/led/animations/standard/<string:animation_name>', methods=['POST'])
def start_standard_animation(animation_name):
    animation = standard_animations.get(animation_name)
    if animation:
        if getattr(led_controller, animation_name)():
            return jsonify(message=f'{animation["name"]} started.'), 200
        else:
            return jsonify(message='Error starting animation.'), 500
    else:
        return jsonify(message='Invalid animation name.'), 400

@led_api.route('/led/animations/custom/<string:animation_name>', methods=['POST'])
def start_custom_animation(animation_name):
    animation = custom_animations.get(animation_name)
    if animation:
        args = animation['args']
        missing_args = [arg for arg in args if arg not in request.json]
        if missing_args:
            return jsonify(message=f'Missing arguments: {", ".join(missing_args)}'), 400
        if getattr(led_controller, animation_name)(**request.json):
            return jsonify(message=f'{animation["name"]} started.'), 200
        else:
            return jsonify(message='Error starting custom animation.'), 500
    else:
        return jsonify(message='Invalid animation name.'), 400

@led_api.route('/led/animations/special/<string:animation_name>', methods=['POST'])
def start_special_animation(animation_name):
    animation = special_animations.get(animation_name)
    if animation:
        args = animation['args']
        missing_args = [arg for arg in args if arg not in request.json]
        if missing_args:
            return jsonify(message=f'Missing arguments: {", ".join(missing_args)}'), 400
        if getattr(led_controller, animation_name)(**request.json):
            return jsonify(message=f'{animation["name"]} started.'), 200
        else:
            return jsonify(message='Error starting special animation.'), 500
    else:
        return jsonify(message='Invalid animation name.'), 400
    
@led_api.route('/led/animations/start', methods=['GET'])
def get_start_animations():
    return jsonify(start_animations)

# Animation information endpoints
@led_api.route('/led/animations/standard', methods=['GET'])
def get_standard_animations():
    return jsonify(standard_animations), 200

@led_api.route('/led/animations/custom', methods=['GET'])
def get_custom_animations():
    return jsonify(custom_animations), 200

@led_api.route('/led/animations/special', methods=['GET'])
def get_special_animations():
    return jsonify(special_animations), 200