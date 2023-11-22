# main.py -- run forever

import machine # Contains all functions related to the Pi Pico hardware
from machine import Pin, ADC, PWM # Easier way of using pin, ADC and PWM
import utime # Handles waiting and time
import urequests # Handles HTTP requests
import uping

from microdot import Microdot, send_file, redirect
from microdot_cors import CORS

# Define the pins
LED_PIN = 18
BUTTON_PIN = 19
POTENTIOMETER_PIN = 28
TEMPERATURE_PIN = 4

# Pin setup
led = Pin(LED_PIN, mode=Pin.OUT)
button = Pin(BUTTON_PIN, mode=Pin.IN)

# Setup ADC (Analogue to Digital Converter)
cpu_temperature_adc = ADC(TEMPERATURE_PIN)

# Function for reading the internal CPU temperature sensor
def ReadCpuTemperature():
    adc_value = cpu_temperature_adc.read_u16()
    volt = (3.3/65535) * adc_value
    temperature = 27 - (volt - 0.706)/0.001721
    return round(temperature, 1)

# Setup Microdot webserver
app = Microdot()
cors = CORS(app, allowed_origins='*', allow_credentials=True)

# This will simply redirect the user to the default static folder 
@app.route('/')
def index(request):
    return redirect('/static/index.html')

# This function will serve any files found within the "static" folder on the Raspberry Pi Pico
@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path, max_age=86400)

@app.post('/api/pin/<int:pin_id>/<int:pin_state>')
def set_pin_state(request, pin_id, pin_state):
    ... # Replace these dots with your code

@app.get('/api/pin/<int:pin_id>')
def get_pin_state(request, pin_id):
    ... # Replace these dots with your code
    # Easiest way to return a response is using the below format
    # return f'{variable}'

@app.get('/api/adc/<int:pin_id>')
def read_adc(request, pin_id):
    ... # Replace these dots with your code

@app.get('/api/adc/cpu')
def read_temperature(request):
    ... # Replace these dots with your code

# Print something that we are all setup and just started the main loop
print("Raspberry Pi Pico is now all booted and running!")

app.run(debug=True)