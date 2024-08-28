from tkinter import *
root = Tk()
root.title("Code Dungeon")
root=Canvas(root, width=900, height=675)
def img1():
    image1 = PhotoImage(file='Assets/Titlescreen.png')
    root.create_image(0,0, anchor = NW, image = image1)

def img2():
    image2 = PhotoImage(file='Assets/Titlescreen.png')
    root.create_image(0,0, anchor = NW, image = image2)


 
