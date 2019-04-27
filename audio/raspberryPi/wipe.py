#Ran from raspberry pi
import board
import neopixel
import time

numOfPixels = 63
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(board.D18, numOfPixels, brightness=1, auto_write=False, pixel_order=ORDER)
pixels.fill((0,0,0))
pixels.show()

colorIndex = 0
ledDir = 1

colorList = []
colorList.append((255,0,0))
colorList.append((0,0,255))
colorList.append((0,255,0))
colorList.append((255,255,0))
colorList.append((255,0,255))



while True:
    color = colorList[colorIndex]
    if colorIndex == len(colorList) - 1:
        colorIndex = 0
    else:
        colorIndex += 1
    if ledDir == 1:
        for i in range(numOfPixels):
            pixels[i] = color
            pixels.show()
            time.sleep(((1/10)*(i-31)*(i-31) + 8)/800)
    elif ledDir == -1:
        
        for i in range(numOfPixels-1, 0, -1):
            
            pixels[i] = color
            pixels.show()
            time.sleep(((1/10)*(i-31)*(i-31) + 8)/800)
            
    ledDir *= -1
    
