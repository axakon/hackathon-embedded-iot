# Hackathon on Embedded and IoT, November 22
The second embedded hackathon, where we narrow our focus on IoT (Internet of Things) development with the Raspberry Pi Pico!

## Recommended setup
1. Download and install the [Thonny IDE](https://thonny.org/)
2. Clone this repo
3. Open the `main.py` file in Thonny
4. Connect the Raspberry Pi Pico to your computer using a USB cable, it should show up automatically after a couple of seconds. 
   If it doesn't show up, click on the current Python version in the bottom right corner and wait for a list to pop-up. 
   From this list, select "MicropPython (Raspberry Pi Pico)" (the name might also contain which physical port it is connected on). 
5. Press F5 or the green arrow button up in the top left part of the window to send your code to the Pi Pico and run it
6. You're off to the races, now complete the challenges below!

The boilerplate `main.py` file contains all imports and libraries (including links to the documentation) that you will need to complete the below challenges!
You will need to update the WiFi credentials in the `boot.py` file, they will be posted in the Hackathon Slack channel.
In addition, we also have `static/index.html` which contains the website we can visit and use to interact with the Raspberry Pi Pico.

Remember, Python requires proper indentation of code to work!

## Transfering files
In this challenge, you might need to preform some file transfers to the Pi Pico, and it is sadly not as trivial as draging and dropping them (but almost!).
This section is specific to the Thonny IDE, and other IDE:s will work differently.

1. Make sure you have the file viewer enable by going into "View" and selecting the "Files" option in the dropdown. There should be a tick on the left hand side to denote it being active.
2. Stop yuor currently running python software by pressing the red "Stop" button (or F12)
3. In the file explorer in Thonny, right click on the file or folder that you wish to transfer. From the context menu, select the option `Upload to <path>`. The path might vary depending on what you have selected in the bottom part of the file explorer.

## Challenge
Your mission is to expand on the boilerplate code found in `main.py` and `static/index.html` by adding the following functions:
- Finish the end-point in `main.py` to toggle the LED light on or off
- Finish the end-point in `main.py` to take a reading of the ADC (Analogue to Digital Converter)
- Add a button on the webpage that turns the LED off and a button that turns the LED on
- Add a simple function that reads the current value of the potentiometer every 5 seconds and display it on the webpage
- Finish the end-point in `main.py` to measure the current temperature in the room using the CPU sensor (code already exists, just finish the implementation)
- Show the current temperature on the webpage, same way as the potentiometer
- Show the current LED state on the webpage, you will need to either add a new end-point for this or alter the toggle end-point to return a value

## Bonus challenge
- Did you notice he extra `uping.py` file? Using the `uping.ping(url)` function, add a new end-point that can ping any URL on the Internet, add a field on the webpage where the user can enter the URL and add a button that will send that URL to the new end-point. Finally, show the resulting averaged ping response time from the functions response tuple (hint, it is on index 3)
- Replace the `fetch` functions on the webpage with Axios (can be found in the static folder already, minified)
- Update the LED toggle end-point to also accept a PWM (Pulse Width Modulation) value (0-65535) and enable the LED to be dimmed from the webpage