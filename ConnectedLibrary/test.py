from tkinter import *
from package.Library import library
from PIL import ImageTk, Image

def printcoucou():
    print("coucou")

#Créer la fenêtre
window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.title("Bibliothèque RPi")
window.maxsize(width, height)
window.minsize(480,360)


l = library.library("test")
s = l.getSerie("D-game")
print(s)
b = s.getBook("9782355927416")
imgPath = b.getPath()[0:len(b.getPath())-7]+".jpg"
print(imgPath)


#Création Image
iWidth = width/4
iHeight = height/3
image = ImageTk.PhotoImage(Image.open(imgPath))  
canvas = Canvas(window, width=iWidth, height=iHeight, bg='ivory')
canvas.grid(column=1, row=1)
canvas.create_image(iWidth/2, iHeight/2, image=image)
canvas.pack(expand=YES)

#Afficher la fenêtre
window.config(background='ivory', width=width, height=height)
window.mainloop()
