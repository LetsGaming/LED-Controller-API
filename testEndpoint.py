import requests
import json

def send_color_wipe_request(red, green, blue):
    url = 'http://127.0.0.1:5000/led/custom/color_wipe'  # Replace with your app's IP address

    # Prepare the JSON payload
    payload = {
        'red': red,
        'green': green,
        'blue': blue
    }

    # Send the POST request to the "color_wipe" endpoint
    response = requests.post(url, json=payload)

    # Print the response
    print(response.text)

# Example usage: sending a color wipe request with RGB values (255, 0, 0)
send_color_wipe_request(255, 0, 0)
