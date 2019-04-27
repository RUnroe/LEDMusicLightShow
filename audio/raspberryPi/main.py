#Ran from raspberry pi
import socket
import board
import neopixel
import time
import sys

numOfPixels = 63
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(board.D18, numOfPixels, brightness=1, auto_write=False, pixel_order=ORDER)
pixels.show()
color = (0,255, 255)
bgColor = (0,0, 255)
host = ''
port = 12345

prevData = 0

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply


def pickColor(color):
        switcher = {
            "red":(255,0,0),
            "green":(0,255,0),
            "blue":(0,0,255),
            "yellow":(255,255,0),
            "white":(255,255,255),
            "purple":(255,0,255),
            "orange":(255,155,0),
            "aqua": (0,255,255),
            "violet":(100,0,255)
        }
        return switcher.get(color)
    

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    if (sys.argv[1] == "line"):
        print("Line")
        global color
        global bgColor
        # Moving color
        color = pickColor(sys.argv[2])
        # Background color
        bgColor = pickColor(sys.argv[3])
        print ("Main: "+ sys.argv[2] + "; Background: " + sys.argv[3])
        
        while True:
            # Receive the data
            data = conn.recv(1024) # receive the data
            data = data.decode('utf-8')
            int_data = int(data)
            
            # Send the reply back to the client
                #conn.sendall(str.encode(reply))
            #print(data)
            global prevData
            if int_data < 6000 and int_data < prevData * 80:
                #function call
                calcLightSpread(int_data)
                pass
        
            prevData = int_data
    elif (sys.argv[1] == "pulse"):
        print("Pulse")
        pixels.fill((0,0,40))
        pixels.show()
        while True:
            # Receive the data
            data = conn.recv(1024) # receive the data
            data = data.decode('utf-8')
            int_data = int(data)
            if int_data < 6000:
                #function call
                calcPulseColor(int_data)
                pass
    
    conn.close()

def calcPulseColor(data):
    if data > 400:
        if data < 500:
            pulseColor = (255,0,0)
        elif data < 600:
            pulseColor = (255,155,0)
        elif data < 700:
            pulseColor = (255,255,0)
        elif data < 800:
            pulseColor = (0,255,0)
        elif data < 900:
            pulseColor = (0,255,255)
        elif data < 1000:
            pulseColor = (255,0,255)
        elif data < 1250:
            pulseColor = (100,0,255)
        else:
            pulseColor = (255,255,255)
    else:
        pulseColor = (0,0,40)
    sendPulse(pulseColor)
        
def sendPulse(color):
    pixels[31] = color
    for i in range(31):
        #right side
        pixels[i+32] = pixels[i+31]
        #left side
        pixels[30-i] = pixels[31-i]
        pixels.show()
        time.sleep(0.004)


    
def calcLightSpread(data):
    spread = 0
    if data < 50:
        spread = 2
    elif data < 100:
        spread = 4
    elif data < 200:
        spread = 6
    elif data < 300:
        spread = 8
    elif data < 350:
        spread = 10
    elif data < 400:
        spread = 12
    elif data < 450:
        spread = 14
    elif data < 500:
        spread = 16
    elif data < 550:
        spread = 22
    elif data < 600:
        spread = 24
    elif data < 700:
        spread = 26
    elif data < 800:
        spread = 28
    elif data > 799:
        spread = 32
    showLights(spread)
    
def showLights(pixel_spread):
    pixels.fill(bgColor) 
    #print("display lights")
    for i in range(pixel_spread):
        pixels[31+i] = color
        pixels[31-i] = color
    pixels.show()
    
s = setupServer()

while True:
    conn = setupConnection()
    dataTransfer(conn)
