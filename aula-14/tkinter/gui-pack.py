import math
import tkinter as tk
from tkinter.constants import LEFT, RIDGE, RIGHT, TOP, X
from PIL import Image, ImageTk

root = tk.Tk()

# container = tk.Frame(root, width=400, height=400)
container = tk.Frame(root, pady=36)
container.pack(fill=X)

logo = Image.open('aula-14/logo.png')

img_resize_factor = 0.2
[img_width, img_height] = logo.size
img_new_width = math.floor(img_width * img_resize_factor)
img_new_height = math.floor(img_height * img_resize_factor)

logo.resize((img_new_width, img_new_height), Image.ANTIALIAS)

logo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(container, image=logo)
logo_label.pack()

texto = tk.Label(
  container,
  text="Selecione um arquivo .csv ou .xls",
  font=("Roboto", 16),
  pady=24,
)
texto.pack()

file_select_button = tk.Button(
  container,
  font=("Roboto", 14),
  text="Selecionar",
  background="#d3af0c",
  borderwidth=0,
  activebackground="#8a7308"
)

file_select_button.pack()
# file_select_button.pack(fill=X)
# file_select_button.pack(side=LEFT)
# file_select_button.pack(side=RIGHT)
# file_select_button.pack(side=TOP)

root.mainloop()