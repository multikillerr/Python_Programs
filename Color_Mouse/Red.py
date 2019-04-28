import cv2
import numpy as np
lower_red = np.array([169,100,100])
upper_red = np.array([189,255,255])
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))
def get_red():
    while True:
        hsv=cv2.cvtColor(frame,(pyautogui.size()))
        mask=cv2.inRange(hsv,lower_red,upper_red)
        maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
        maskFinal=maskClose
        conts=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
