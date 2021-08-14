__meta={"type":"internal_script","name":"User","version":[0,0,0,0]}
from tkinter import *
from tkinter import ttk
import SQL
userWin=Tk()
userWin.title("User Manager")
newUserWin=Tk()
newUserWin.title("New User")
uList = Listbox(userWin, height=10).grid(column=0,row=0)
def openUserWindow():
  userWin.mainloop()