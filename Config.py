from tkinter import *
from tkinter import ttk
cfgui=Tk()
cfgui.geometry('500x325+1+40')
cfgui.resizable(FALSE,FALSE)
cfgui.title("ump-cfgui")
n = ttk.Notebook(cfgui)
f1 = ttk.Frame(n)   
f2 = ttk.Frame(n)   
n.add(f1, text='General')
n.add(f2, text='Behavior')
n.grid(column=0,row=2,sticky=(N,E,S,W),columnspan=3,pady=5, padx=5)
