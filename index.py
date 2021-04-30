import time
from os import system
from cv2 import VideoCapture, resize
from playsound import playsound
from threading import Thread

FRAMERATE = 24

def playMP3():
    playsound("badapple.mp3")

def playVideo():
    fps = 0
    excesTime = 0
    cap = VideoCapture('./badapple.mp4')
    res, frame = cap.read()
    
    while res:
        startTime = time.time()
        frame = resize(frame,(90,45))
        height, width, channels = frame.shape
        
        output = ""

        for x in range (0,45):
            for y in range(0,90):
                color = frame[x,y]
                if color[0] > 240 and color[1] > 240 and color[2] > 240:
                    output += u"\u2588"
                else:
                    output += " "
            if x != 62:
                output += "\n"
        system('cls')
        print(output)
        res, frame = cap.read()
        if 1/FRAMERATE - (time.time() - startTime) - excesTime > 0:
            time.sleep(1/FRAMERATE - (time.time() - startTime) - excesTime)
            excesTime -= 1/FRAMERATE - (time.time() - startTime)
        else:
            time.sleep(0)
            excesTime -= 1/FRAMERATE - (time.time() - startTime)

videoThread = Thread(target=playVideo)
audioThread = Thread(target=playMP3)
videoThread.start()
audioThread.start()
audioThread.join()
videoThread.join()
