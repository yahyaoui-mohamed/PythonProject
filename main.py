from tkinter import *
root = Tk()
root.geometry("1366x768")

b = Button(root, text="Enegistrer")
b.pack()

menuButton = Menubutton(root, text="Choisissez la monnaie", relief=FLAT)
menuButton.pack()
menuButton.menu = Menu(menuButton)
menuButton["menu"] = menuButton.menu

menuButton.menu.add_checkbutton(label="Bitcoin", variable=IntVar())
menuButton.menu.add_checkbutton(label="Litecoin", variable=IntVar())
menuButton.menu.add_checkbutton(label="Dogecoin", variable=IntVar())
menuButton.menu.add_checkbutton(label="BitcoinCash", variable=IntVar())
menuButton.menu.add_checkbutton(label="Ethereum", variable=IntVar())


root.mainloop()
