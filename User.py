__meta={"type":"internal_script","name":"User","version":[0,0,0,0]}
from tkinter import *
from tkinter import ttk
import SQL
def updateUserList():
  uservar.set(users)
def newUser():
  newUserWin=Tk()
  newUserWin.title("New User")
  username = StringVar()
  fullname = StringVar()
  l0 = ttk.Label(newUserWin,text='Username:').grid(column=0,row=0)
  name = ttk.Entry(newUserWin,textvariable=username).grid(column=1,row=0,sticky=(N,W,E))
  l1 = ttk.Label(newUserWin,text='Full Name:').grid(column=0,row=1)
  fname = ttk.Entry(newUserWin,textvariable=fullname).grid(column=1,row=1,sticky=(N,W,E))
  newUserWin.columnconfigure(1, weight=1)
def openUserWindow():
  userWin.mainloop()
userWin=Tk()
userWin.title("User Manager")
s=ttk.Style()
s.theme_use("clam")
users = ["user0", "user1", "user2"]
uservar = StringVar(value=users)
uList = Listbox(userWin, height=10,listvariable=uservar)
bydefault = BooleanVar(value=True)
bdc = ttk.Checkbutton(userWin, text="Show on Startup", variable=bydefault, onvalue=True)
srt=ttk.Button(userWin,text="Start UMP")
new=ttk.Button(userWin,text="New User",command=newUser)
rem=ttk.Button(userWin,text="Remove User")
cfg=ttk.Button(userWin,text="Edit User")
uList.grid(column=0,row=0,columnspan=3,sticky=(N,E,S,W))
bdc.grid(column=0,row=1,columnspan=3)
srt.grid(column=3,row=0,sticky=(N,E,W))
new.grid(column=0,row=2,sticky=(N,E,W))
rem.grid(column=1,row=2,sticky=(N,E,W))
cfg.grid(column=2,row=2,sticky=(N,E,W))
userWin.columnconfigure(0, weight=1)
userWin.rowconfigure(0, weight=1)
userWin.resizable(FALSE,FALSE)