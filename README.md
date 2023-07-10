# LED Controller
This repository contains the code for the LED Controller, which receives LED control commands from the LED Control API and controls a WS2812B LED strip connected to a Raspberry Pi.
### Note
Check out my implementation of an Webbased-GUI for this API: [LED-Controller-GUI](https://github.com/LetsGaming/LED-Controller-GUI)

## Important
* This implementation is only meant for local deployment! 
* There are basically no security checks added, so there is no rate-limiting or much input validation or anything else!!
    - If you want to add those implementations, feel free to create a fork of this repository.

## Features
The LED Controller provides the following features:
* Control the WS2812B LED strip based on received commands.

## Prerequisites
Before using the LED Controller, ensure you have the following prerequisites:

* Python (version X.X.X)
* Raspberry Pi with the RPi.GPIO library installed
* WS2812B LED strip and library (e.g., rpi_ws281x)
* Depending on the number of LEDs (anything above 30), a separate power supply unit (PSU) for the LED strip is recommended. 
    - The rule of thumb is 20mA average per LED and 60mA for white at full brightness.

## Installation
To install and set up the LED Controller, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/LetsGaming/led-controller-api.git
```

2. Install the dependencies:
```bash
cd PATH/TO/YOUR/CLONE
pip install -r requirements.txt
```

## Starting the LED Controller API
To start the LED Controller API, use the following command:

```bash
cd PATH/TO/YOUR/CLONE
python app.py
```
The API will start and wait for requests to control the LED strip.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
