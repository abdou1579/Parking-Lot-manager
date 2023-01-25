import cv2
import numpy as np
import pytesseract
from skimage.morphology import disk
from skimage.morphology import erosion, dilation
from PIL import Image


path= r'C:\Users\Romeila\Desktop\stage(4)\mat.jpg' #130
path1 = r'C:\Users\Romeila\Downloads\stage(4)\LP_images 12h\r1.jpg' #30 40 (50 et 60 kherejli un caractére zyada) 70 faux
path2 = r'C:\Users\Romeila\Downloads\stage(4)\LP_images 12h\r2.jpg' 
path3 = r'C:\Users\Romeila\Downloads\stage(4)\LP_images 12h\r3.jpg' #20
path4 = r'C:\Users\Romeila\Downloads\stage(4)\LP_images 12h\r4.jpg' #15
path5 =r'C:\Users\Romeila\Desktop\Stage\yolov5-master\runs\detect\exp5\crops\licence\20210728_122054.jpg'
path6 =r'C:\Users\Romeila\Desktop\Stage\yolov5-master\runs\detect\exp5\crops\licence\20210728_122344.jpg'
path7 =r'C:\Users\Romeila\Desktop\Stage\yolov5-master\runs\detect\exp5\crops\licence\20210728_122122.jpg' #khalal
path8 =r'C:\Users\Romeila\Desktop\Stage\yolov5-master\runs\detect\exp5\crops\licence\20210728_122211.jpg'
path9 =r'F:\stage\yolov5\runs\detect\exp3\crops\license\plate.jpg'#15
img = cv2.imread(path9)
window_name = 'Image'
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\\Tesseract-OCR\\tesseract.exe'
##### hada pretraitemet li massla7ch khelito brk besh nel9ah ila s7a9ito kesh nhar###
# get grayscale image
def get_grayscale(image):
    im = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    im= cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    im =  cv2.bilateralFilter(im, 13, 15, 15)
    return im
# # noise removal
def remove_noise(image):
    return cv2.GaussianBlur(image,(3,3),0)

def edge (image):
 return  cv2.Canny(image, 150, 300) 

# #thresholding
def thresholding(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 45, 15)
def median(image):
    return cv2.medianBlur(image,3)
# #dilation
def dilate(image):
   kernel = np.ones((5,5),np.uint8)
   return cv2.dilate(image, kernel, iterations = 1)
# #erosion
def erode(image):
    selem=disk(1)
    eroded = erosion(image, selem) 
    return eroded 

# #opening - erosion followed by dilation
def opening(image):
   kernel = np.ones((5,5),np.uint8)
   return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# #canny edge detection
def canny(image):
   return cv2.Canny(image, 100, 200)

# #skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
      angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated
######## yekhlass hna##############

#********** had la partie win je modifiait la taille des images********
scale_percent = 25 # percent of original size ****coeff ta3 tassghir or takbir kima thebo xD**** 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imshow(window_name ,resized )
text= pytesseract.image_to_string(resized ) 
print("text:" ,text)

cv2.waitKey(0)









# #template matching
# def match_template(image, template):
#     return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

