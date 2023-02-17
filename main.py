import requests
from tkinter import *

root = Tk()
root.geometry("1366x768")

# Import API

url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
headers = {'X-CoinAPI-Key': 'CC78E6F3-7AC5-4BB1-BA80-519948CB977F'}
response = requests.get(url, headers=headers)
result = response.json()

# Import API

label = Label(root, text="1 BTC : "+str(int(result["rate"]))+" USD")
label.pack()


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
