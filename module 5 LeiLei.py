from tkinter import *
from module2 import items
from module3 import Order

# Base
win=Tk()

# Title setting for the program window
win.title("Get those frames to fit!")

# Mainframe
mf=Frame(win)
mf.grid(row=0, column=0)

order = Order(items)
quantities = {}
cart_quantities = {}
cart_total = {}
final_total = StringVar()
final_total.set("$0")
for item in items:
    for dic in [quantities, cart_quantities, cart_total]:
        if dic != cart_total:
            tmp = IntVar()
        else:
            tmp = DoubleVar()
        tmp.set(0)
        dic[item] = tmp

# button functions
def add(item, quantity):
    order.add(item, quantity)
    cart_quantities[item].set(int(order.order[item]))
    cart_total[item].set(order.order[item] * items[item]['price'])

def modify(item, quantity):
    order.modify(item, quantity)
    cart_quantities[item].set(int(order.order[item]))
    cart_total[item].set(order.order[item] * items[item]['price'])

def start_over():
    order.start_over()
    for dic in [quantities, cart_quantities, cart_total]:
        for item in dic:
            dic[item].set(0)

def checkout():
    global final_total
    final_total.set("${}".format(order.checkout()))

# First row frame
wf1=Frame(mf, bg='red')
wf1.grid(row=0, column=0)
# Sub frames inside each frame
sf1 = Frame(wf1, height=300, width=600, bg='green')
sf1.grid(row=0, column=0, columnspan=4, rowspan=len(items)+2)
# Widgets in wf1
l0 = Label(wf1, text='Menu')
l0.grid(row=0, column=0, columnspan=4, sticky="EW")
l1 = Label(wf1, text='Food')
l1.grid(row=1, column=0, sticky="EW")
l2 = Label(wf1, text="Price")
l2.grid(row=1, column=1, sticky="EW")
l3 = Label(wf1, text='Quantity')
l3.grid(row=1, column=2, sticky="EW")

l4 = Label(wf1, text="")
l4.grid(row=1, column=3, sticky="EW")
count = 2
for item in items:
    l1 = Label(wf1, text=item)
    l1.grid(row=count, column=0, sticky=(N,S,E,W))
    l2 = Label(wf1, text="${}".format(items[item]['price']))
    l2.grid(row=count, column=1, sticky=(N,S,E,W))
    e3 = Entry(wf1, textvariable=quantities[item])
    e3.grid(row=count, column=2, sticky="EWNS")
    print(item)
    b4 = Button(wf1, text="Add to cart", bg="yellow", command=lambda item=item: add(item, quantities[item].get()))
    b4.grid(row=count, column=3, sticky=(N,S,E,W))
    count += 1

wf2=Frame(mf, bg='blue')
wf2.grid(row=1, column=0)
sf2 = Frame(wf2, height=100, width=600, bg='green')
sf2.grid(row=0, column=0, columnspan=5, rowspan=2)
# Widgets in wf2
l1 = Label(wf2, text="Order summary", font=('Helvetica', 10, 'bold'))
l1.grid(row=0, column=0, columnspan=5, sticky='EW')

l1 = Label(wf2, text='Food')
l1.grid(row=1, column=0, sticky="EW")
l2 = Label(wf2, text="Quantity")
l2.grid(row=1, column=1, sticky="EW")
l3 = Label(wf2, text='Total cost')
l3.grid(row=1, column=2, sticky="EW")
l4 = Label(wf2, text="")
l4.grid(row=1, column=3, sticky="EW")
l5 = Label(wf2, text="")
l5.grid(row=1, column=4, sticky="EW")

count = 2
for item in items:
    l1 = Label(wf2, text=item)
    l1.grid(row=count, column=0, sticky=(N,S,E,W))
    l2 = Label(wf2, textvariable=cart_quantities[item])
    l2.grid(row=count, column=1, sticky=(N,S,E,W))
    l3 = Label(wf2, textvariable=cart_total[item])
    l3.grid(row=count, column=2, sticky=(N,S,E,W))
    b4 = Button(wf2, text="Change quantity", bg="yellow", command=lambda item=item: modify(item, cart_quantities[item].get()))
    b4.grid(row=count, column=3, sticky=(N,S,E,W))
    e5 = Entry(wf2, textvariable=cart_quantities[item])
    e5.grid(row=count, column=4, sticky="EWNS")
    count += 1

wf3 = Frame(mf, bg='blue')
wf3.grid(row=2, column=0)
sf3 = Frame(wf3, height=50, width=600, bg='green')
sf3.grid(row=0, column=0, columnspan=2, rowspan=2)
b1 = Button(wf3, text="Start over", bg="red", command=start_over)
b1.grid(row=0, column=0, sticky='EW')
b2 = Button(wf3, text="Checkout -- see total", bg="pink", command=checkout)
b2.grid(row=0, column=1, sticky='EW')

wf4 = Frame(mf, bg='blue')
wf4.grid(row=3, column=0)
sf4 = Frame(wf4, height=20, width=600, bg='green')
sf4.grid(row=0, column=0, columnspan=2)
l1 = Label(wf4, text="Total (tax included): ")
l1.grid(row=0, column=0, sticky="WE")
l1 = Label(wf4, textvariable=final_total)
l1.grid(row=0, column=1, sticky="WE")



win.mainloop()