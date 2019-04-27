#Ran from the main computer / source of audio
import socket
import pyaudio
import numpy as np
import time
import math

CHUNK = 2**11
RATE = 44100

p = pyaudio.PyAudio()
#open audio stream. In my case, my desktop audio is 'input_device_index' = 3
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input_device_index = 3,input=True,
              frames_per_buffer=CHUNK)

host = '192.168.0.xx' #ip address of raspberry pi
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True: 
	#Loop to gather audio, convert it to a number, and then send it to the pi
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak = np.average(np.abs(data))*2
    time.sleep(0.01)
    out = math.floor(peak)
    str_data = str(out)
    s.send(str.encode(str_data)) # sends data to raspberry pi
    
    print(str_data)
    time.sleep(0.02) #Delay to prevent overloading raspberry pi 
    
s.close()
stream.stop_stream()
stream.close()
p.terminate()
