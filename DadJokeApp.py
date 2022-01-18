import tkinter as tk
from tkinter import ttk
import requests

url = "https://icanhazdadjoke.com/"
headers = {
    'Accept': 'application/json',
    "User-Agent": "hollaattontone"
    
    }


window = tk.Tk()
window.title("Anthony's 'Dadabase' of Random Dad Jokes")

frame = ttk.Frame(window)


canvas1 = tk.Canvas(window, width=700, height=300)
canvas1.pack()

label = tk.Label(window, text="At BBQ? Need a dad joke?")
label.config(font=('helvetica', 14))
canvas1.create_window(350, 25, window=label)    


def get_joke():
    
    joke_data= requests.get(url, headers=headers).json()

    
    joke = joke_data['joke']

    label3 = tk.Label(window, text= f'{joke}.',font=('helvetica', 11))
    canvas1.create_window(350, 230, window=label3)



button = tk.Button(text='Hit me!', command=get_joke)
canvas1.create_window(350, 150, window=button)


window.mainloop()


