import requests
from tkinter import *
from tkinter import ttk

def consultar_categoria():
    category = combo.get()
    url = f'https://api.chucknorris.io/jokes/random?category={category}'
    response = requests.get(url)
    dado = response.json()
    resultado.config(text=dado['value'])


root = Tk()
root.title("Chuck Norris Jokes")

frm = ttk.Frame(root, padding=10)
frm.grid()

categorias = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

ttk.Label(frm, text="Escolha uma categoria:").grid(column=0, row=0)
combo = ttk.Combobox(frm, values=categorias)
combo.grid(column=1, row=0)

ttk.Button(frm, text="Consultar", command=consultar_categoria).grid(column=2, row=0)

resultado = ttk.Label(frm, text="")
resultado.grid(column=0, row=1, columnspan=3)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2, columnspan=3)

root.mainloop()
