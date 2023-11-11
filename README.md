# MQTT Sensor Data and LED Control

This project utilizes MQTT (Message Queuing Telemetry Transport) to send and receive sensor data between a Raspberry Pi and a client device. The program reads distance data from an ultrasonic sensor and publishes it to an MQTT topic. Additionally, it subscribes to a separate topic to control an LED based on incoming messages.

## Dependencies

- **paho-mqtt**: MQTT client library for Python
- **gpiozero**: Library for interacting with GPIO components (e.g., DistanceSensor, LED)

Ensure you have these dependencies installed before running the program.

`pip install paho-mqtt`
`pip install gpiozero`

## Configuration

Update the following variables in the script to match your MQTT broker's address and port:

`broker_address = "your_broker_address`
`broker_port = your_broker_port`


## Hardware Setup

Connect an ultrasonic sensor with trigger pin connected to GPIO pin 23 and echo pin connected to GPIO pin 25. Additionally, connect an LED to GPIO pin 4.

## Usage

1. Run the script on your Raspberry Pi:

   `python main.py`

2. The program will continuously read distance data from the ultrasonic sensor and publish it to the specified MQTT topic.

3. Subscribe to the "apagar" topic to remotely control the LED. Send "1" to turn the LED on and "0" to turn it off.

4. If the distance measured by the sensor is less than or equal to 0.5, the program will print "Persona cerca," indicating that a person is nearby.

Feel free to customize the script or expand its functionality based on your project requirements.