# lauches the laptop cameara

import cv2
import numpy as np
cam = cv2.VideoCapture(0)
while True:
    myret, CapFrame =cam.read()

    mirrored_frame = cv2.flip(CapFrame, 1)

    # Display the mirrored frame
    cv2.imshow('Mirrored Camera Feed', mirrored_frame)

    #cv2.imshow('CapFrame',CapFrame)
    if cv2.waitKey(10) & 0xFF==ord('c'):
        cv2.imwrite('CapFrame.jpg', CapFrame)
        break
    if cv2.waitKey(10) & 0xFF==27:
        break
cam.release()
cv2.destroyAllWindows()
