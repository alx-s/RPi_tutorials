# Analog inputs for the Raspberry Pi : playing with MaxBotix ultrasonic sensors

alx-s

23-03-2013

## Context

Some time ago I got to work on an installation which aimed at controlling the sound coming from loudspeakers according to the distance between them and the listener. The prototype only involved two sound sources and ended up as follow : a Raspberry Pi, two speakers and two MaxBotix ultrasonic sensors (one per speaker). 
To give you the general idea : ultrasonics evaluated the distance between a speaker and the listener. Their analog output was then read through the Raspberry Pi's GPIO using a MCP3008. A python scrpit gathered the data and sent it using OSC to Pure Data which generated the sound.

If you want to know how to set up the OSC between python and pure data take a look at my other tutorial : https://github.com/alx-s/RPi_tutorials/tree/master/OSC_python-pd .

When it comes to using the RPi, lots of information can be found on learn.adafruit.com . As a matter of fact, this tutorial is based on one from adafruit : http://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/ . 

## Getting started

### What we need

* Raspberry Pi
* Breadboard
* Wires (pay attention to connectors)
* Maxbotix sensor (like a MB1000 LV-MaxSonar-EZ0 for exemple)
* MCP3008 (or MCP3004)

### MaxBotix ultrasonic sensors

Our aim is to use MaxBotix ultrasonic sensors. I've been using the MB1000 LV-MaxSonar-EZ0 but they all work in a similar way. Though those sensor can provide a PWM as well as a serial output, we will concentrate on their analog output.
Go take a look at http://www.maxbotix.com/ , choose your weapon and let's hook it up to the Pi!
We won't discuss the sensors here since the website provides tutorials and datasheets that contain all you need to know.

### MCP3008

When attempting to read an analog signal with the RPi we need to keep in mind that the RPi is a digital-only computer, it does not have any analog input.
That's the reason why we need to use a MCP3008 (or MCP3004 which is basically the same but with only 4 inputs instead of 8).
The MCP3008 is ADC (Analog-to-Digital Converter) and will help us make the bridge between the analog sensor and the digital-only Raspberry Pi.
Here's the datasheet : https://www.adafruit.com/datasheets/MCP3008.pdf . 
Take a good look at it and and let's hook it up!

### GPIO

The GPIO are here to let us connect anything we want to the RPi. Though there's no need knowing everything about them to use them, go take a look there : http://elinux.org/RPi_Low-level_peripherals .
The GPIO's layout is something you will need in this tutorial and that will come in handy quite often!

## Wiring the MCP3008 to the RPi

Now that you have the materials and the basic information, grab your breadboard and prepare for the fun!

Here comes the wiring diagram. On your left are the MCP3008 pins, on your right the RPi GPIO. Keep the datasheet with you, you'll want to take a look at them sooner or later.

* VDD -> 3.3V (power)
* VREF -> 5V (we're going to use sensors 5V powered sensors. Since their analog output will vary between 0V and 5V the ADC's VREF must match the sensor's output)
* AGND -> GND (analog ground)
* CLK -> GPIO 18 (clock)
* DOUT -> GPIO 23 (data going out of the MCP3008 to the RPi)
* DIN -> GPIO 24 (data coming in the MCP3008 from the RPi)
* CS -> GPIO 25 (Chip Select)
* DGND -> GND

Now let's connect the sensor. Once again, take a look at the datasheet!
* sensor's GND -S GND
* sensor's 5V -> 5V
* sensor's AN -> MCP3008's ch0 (pin 0)

## Installing stuff

Here is what you need to install first : 
```shell
sudo apt-get install python-dev
```
Then you will need the GPIO library :
```shell
sudo apt-get install python-setuptools
sudo easy_install rpi.gpio
```
And... that's all!
You might need to update your Raspberry Pi depending on your OS release but everything should work as described.

