from tkinter import *

# Base
win=Tk()

win.title("Get those frames to fit!")

# Mainframe
mf=Frame(win)
mf.grid(row=0, column=0)

# 1st row frame
wf1=Frame(mf, bg='red')
wf1.grid(row=0, column=0)

# 2nd row frame
wf2=Frame(mf, bg='blue')
wf2.grid(row=1, column=0)

# 3rd row frame
wf3=Frame(mf, bg='yellow')
wf3.grid(row=2, column=0, columnspan=4, sticky="NSEW")

# Sub frames inside each frame
sf1 = Frame(wf1, height=350, width=400, bg='green')
sf1.grid(row=0, column=0)
sf2 = Frame(wf2, height=10, width=400, bg='white')
sf2.grid(row=0, column=0, columnspan=2, rowspan=2)
sf3 = Frame(wf3, height=150, width=400, bg='red')
sf3.grid(row=0, column=0, columnspan=4, rowspan=1)

# Widgets in wf1
photo = PhotoImage(file="")
pikachu=Label(wf1, image=photo)
pikachu.photo=photo
pikachu.grid(row=0, column=0, stick=(E,W))

# Widgets in wf2
l1 = Label(wf2, text="Enemy Hp:")
l1.grid(row=0, column=0, sticky=EW)
l2 = Label(wf2, text="Player Hp:")
l2.grid(row=1, column=0, sticky=EW)

ehp = IntVar()
ehp.set(10)

enemy_hp = Label(wf2, textvariable=ehp)
enemy_hp.grid(row=0, column=1, sticky="EW")

Player_hp = Label(wf2, textvariable=ehp)
Player_hp.grid(row=1, column=1, sticky="EW")

# Widgets in wf3
b1=Button(wf3, text="atk1")
b1.grid(row=0, column=0, sticky=(N,S,E,W))

b2=Button(wf3, text="atk2")
b2.grid(row=0, column=1, sticky=(N,S,E,W))

b3=Button(wf3, text="atk3")
b3.grid(row=0, column=2, sticky=(N,S,E,W))

b4=Button(wf3, text="atk4")
b4.grid(row=0, column=3, sticky=(N,S,E,W))

win.mainloop()

