from tkinter import*
from random import*
from PIL import Image
from PIL import ImageTk

def so_sanh(player):
    global a
    global x
    a = randint(0,2)
    
    if a==0: x="Keo"
    if a==1: x="Bua"
    if a==2: x="Bao"
    text.set(x)
    if str(player) == x : 
        lbl.configure(text="ban Hoa ")

    else:
        if str(player) == str("Bao"):
            if x == str("Bua"):
                lbl.configure(text="ban thang")
            if x == str("Keo"):
                lbl.configure(text="ban thua")
            if x == str(player): 
                lbl.configure(text="ban Hoa ")
        elif str(player) == "Bua":
            if x == "Keo":
                lbl.configure(text="ban thang")
            else:
                lbl.configure(text="ban thua")
        elif str(player) == "Keo":
            if x == "Bao":
                lbl.configure(text="ban thang")
            else:
                lbl.configure(text="ban thua")
    

game=Tk()
text=StringVar()
game.geometry('350x200')
game.title("Welcome to game keo-bua-bao")

lbl = Label(game, text="Kết quả",bg='green')
lbl.grid(column=2, row=0) 
lbl1 = Label(game, text="máy chọn :")
lbl1.grid(column=0, row=1)
lbl2 = Label(game, text="bạn chọn :")
lbl2.grid(column=0, row=2)


img = ImageTk.PhotoImage(Image.open('bua.png' ))
img1 = ImageTk.PhotoImage(Image.open('keo.png' ))
img2 = ImageTk.PhotoImage(Image.open('bao.png' ))

robot_chon = Entry(game,width = 10,textvariable=text).grid(column =1,row =1)
bua = Button(game,image=img,command=lambda:so_sanh("Bua")).grid(column =3,row =3)
keo = Button(game,image=img1,command=lambda:so_sanh("Keo")).grid(column =2,row =2)
bao = Button(game,image=img2,command=lambda:so_sanh("Bao")).grid(column =4,row =2)

game.mainloop()
