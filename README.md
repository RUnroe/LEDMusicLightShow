# LED Music Light Show

## DESCRIPTION ##
A Python script is used to stream your desktop audio to the Raspberry Pi through a TCP port. The Raspberry Pi displays a light show on a NeoPixel ws2812b LED strip. The pattern and color of lights are configurable when the program is started on the Pi. The Python program must be run with sudo in order for the LEDs to work. 

## WHAT I LEARNED ##
I learned how to connect two Python scripts on different devices wirelessly through a port. I also learned how to use the pyAudio library to stream audio from select inputs and the NeoPixel library to program the LEDs.

## main.py ##
This is the main file ran from the Raspberry Pi consisting of two light patterns. The first of which, called 'line', displays a line of the selected color. The line goes out from the center in both directions with varying lengths based on the audio level. 

Run through bash terminal using **sudo python3 line _color backgroundColor_**
The 'color' corresponds to the color of the line while the 'backgroundColor' is the color of the pixels behind the line.
All colors must be chosen from the list below.

The second light pattern sends a pulse of color out from the center. The color of the pulse is based on how great the audio level was. This pattern comes with predetermined colors.

Run through bash terminal using ##### sudo python3 pulse #####

### Color List ###
Red
Green
Blue
Yellow
White
Purple
Orange
Aqua
Violet
