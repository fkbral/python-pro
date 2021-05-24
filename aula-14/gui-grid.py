import math
import tkinter as tk
from tkinter.constants import LEFT, RIDGE, RIGHT, TOP, X
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import pandas as pd

def carrega_arquivo(button_text):
  # print('clicou no botão')
  button_text.set("Carregando") 
  file = askopenfile(
    parent=root.option_add('*foreground', 'black'),
    mode="r",
    filetypes=[("arquivo csv", ".csv"), ("arquivo xls", ".xls")]
  )
  if file:
    df = pd.read_csv(file, sep=";")
    print(df)
  button_text.set("Selecionar")

root = tk.Tk()

# container = tk.Frame(root, width=400, height=400)
container = tk.Frame(root, pady=36)
container.grid(columnspan=5)

logo = Image.open('aula-14/logo.png')

logo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(container, image=logo)
logo_label.grid(columnspan=3, column=1, row=0)

texto = tk.Label(
  container,
  text="Selecione um arquivo .csv ou .xls",
  font=("Roboto", 16),
  pady=24,
)
texto.grid(columnspan=5, column=0, row=1)

file_select_button_text = tk.StringVar()
file_select_button_text.set("Selecionar")

file_select_button = tk.Button(
  container,
  command=lambda: carrega_arquivo(file_select_button_text),
  font=("Roboto", 14),
  textvariable=file_select_button_text,
  # text="Selecionar",
  background="#d3af0c",
  borderwidth=0,
  activebackground="#8a7308"
)

file_select_button.grid(column=2, row=2)

root.mainloop()