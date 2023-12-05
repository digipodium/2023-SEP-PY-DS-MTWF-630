import cv2
import numpy as np

video = cv2.VideoCapture(r"C:\Users\ZAID\Videos\mantissa.xyz_loop_064.mp4")
while True:
    status, frame = video.read()
    if not status: break
    cv2.imshow("Video output", frame)
    if cv2.waitKey(1) == 27: # escape key
        break
video.release()
cv2.destroyAllWindows()