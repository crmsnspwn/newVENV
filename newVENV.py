from tkinter import *
from tkinter import filedialog
import os
 
root = Tk()
root.geometry('500x500')
root.title('New Hire Email Clock ID Query')

# Frames

# Text Boxes

venv_title = Text(root, height = 1, font = ('Helvetica', 16))

# Labels

## Functions

def open_folder():
    file_path = filedialog.askdirectory(initialdir = 'C:/Users/')
    file_path_label = Label(root, text = file_path).grid(row = 1, column = 0, columnspan = 3, sticky = 'NESW')
    os.chdir(file_path)

def get_text():
    global venv_name
    venv_name = venv_title.get('1.0', END)

def create_venv():
    get_text()
    cmd_create_venv = f'cmd /c "python -m venv {venv_name}"'
    os.system(cmd_create_venv)

def clear_venv_title():
    venv_title.delete(1.0, END)

# Buttons

venv_open_folder = Button(root, text = 'Open Root Folder', command = open_folder)
venv_create = Button(root, text = 'Create Virtual Environment', command = create_venv)
venv_title_clear = Button(root, text = 'Clear Text', command = clear_venv_title)

## List of Objects

object_list = [venv_title, venv_open_folder, venv_create, venv_title_clear]

## Configuration

row_number = 0
for object in object_list:
    Grid.rowconfigure(root, row_number, weight = 1)
    row_number += 1

column_number = 0
for object in object_list:
    Grid.columnconfigure(root, column_number, weight = 1)
    column_number += 1

## Positions

venv_open_folder.grid(row = 0, column = 0, columnspan = 3, sticky = 'NESW')
venv_title.grid(row = 2, column = 0, columnspan = 3, sticky = 'NESW')
venv_create.grid(row = 3, column = 0, sticky = 'NESW')
venv_title_clear.grid(row = 3, column = 2, sticky = 'NESW')

root.mainloop()