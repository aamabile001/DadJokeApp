import os
os.getcwd()

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

window.configure(bg='blue')

# style configuration
style = ttk.Style(window)
style.configure('TLabel', background='blue', foreground='white')
style.configure('TFrame', background='blue')

frame = ttk.Frame(window)
# frame.grid(column=0, row=0)

# background_image = tk.PhotoImage(file="./fff.png")
# background_label = tk.Label(window, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas1 = tk.Canvas(window, width=700, height=300)
canvas1.pack()

label = tk.Label(window, text="At BBQ? Need a dad joke?")
label.config(font=('helvetica', 14))
canvas1.create_window(350, 25, window=label)    


def get_joke():
    
    joke_data= requests.get(url, headers=headers).json()
    #clean_data = json.load(weather_data)
    
    joke = joke_data['joke']

    label3 = tk.Label(window, text= f'{joke}.',font=('helvetica', 11))
    canvas1.create_window(350, 230, window=label3)
    #break
# label4 = tk.Label(window, text= weather_data,font=('helvetica', 10, 'bold'))
# canvas1.create_window(200, 230, window=label4)


button = tk.Button(text='Hit me!', command=get_joke)
canvas1.create_window(350, 150, window=button)


window.mainloop()


