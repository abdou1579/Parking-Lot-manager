from cv2 import (VideoCapture, namedWindow, imshow, waitKey, destroyWindow, imwrite)
import time
cam_port = 0
cam = VideoCapture(cam_port)
 
result, image = cam.read()
  

if result:
    imshow("frame", image)
   
    imwrite("plate.jpg", image)
  
   
    waitKey(0)
    destroyWindow("frame")
  
else:
    print("No image detected. Please! try again")


