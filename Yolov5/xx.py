import tkinter as tk
import torch
import os
from IPython.display import Image, clear_output
import pytesseract
import cv2
from PIL import Image
import numpy
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog
import detect


import os
root = Tk()
root.title('Verification')
root.geometry('800x800')
path = '.\yolov5'
os.chdir(path)
print(os.getcwd())
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    shutil.copy2(os.path.join(filename,filename), r'C:\Users\asus zephyrus\Desktop\localisation et reconnaissance des  matricules\yolov5')
    #shutil.move(filename, r'C:\Users\asus zephyrus\Desktop\localisation et reconnaissance des  matricules\yolov5')
def detectt():
    python detect.py --weights best.pt  --source plate.jpg  --save-crop



def takepic():
    os.startfile(r"C:\Users\asus zephyrus\Desktop\localisation et reconnaissance des  matricules\yolov5\takepic.py", operation="open")
def import_pic():
    pass
def showres():
    path1= r'C:\Users\asus zephyrus\Desktop\localisation et reconnaissance des  matricules\yolov5\runs\detect\exp2\crops\license\plate.jpg'
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(path1)
    data = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
    print(data)
    x = "Registration Number is " + data
    Result.insert(tk.END, x)
    return data
def clear():
    Result.delete('1.0', END)
    shutil.rmtree(r'C:\Users\asus zephyrus\Desktop\localisation et reconnaissance des  matricules\yolov5\runs\detect\exp2')
    os.remove("plate.jpg")

Label(root,text="",font="System").place(x=200,y=600) 
Button(root,text='Detect The board',activebackground="black",command=detectt,activeforeground="white").place(x=550,y=280)
Button(root,text='Take Picture',command=takepic,activebackground="black",activeforeground="white").place(x=350,y=130)
Button(root,text='Import Picture',command=UploadAction,activebackground="black",activeforeground="white").place(x=350,y=400)
Button(root,text='Show results',activebackground="black",command=showres,activeforeground="white").place(x=550,y=220)
Button(root,text='Clear Results',activebackground="black",command=clear,activeforeground="white").place(x=550,y=350)
Result = Text(root, height=2, width=70)
Result.place(x=10,y=500)
Result.pack()
root.mainloop()