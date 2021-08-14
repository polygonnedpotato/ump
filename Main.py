__meta={"type":"internal_script","name":"Main","version":[0,0,0,0]}
import Debug
import Config
import SQL
import User
import Resources as r
import sys
import os
import datetime
from pathlib import Path
def init(cfgFile,dbgmd):
  Debug.load(cfgFile,dbgmd)
  Config.loadConfigFile(cfgFile)
  Debug.log("Main","Loaded Config File From "+cfgFile,4)
  st=str(datetime.datetime.now().strftime("%c"))
  Debug.log("Main","UMP Started near "+st,0)
  Debug.log("Debug","Debug Flag is set to "+str(dbgmd),4)
  Debug.log("Debug","Debug Log will be stored at "+Debug.ll,4)
  global vshrt
  vshrt=""
  for x in range(4):
    vshrt+=str(__meta["version"][x])
    if x==3:
      pass
    else:
      vshrt+="."
  SQL.init()
  SQL.storeValue("idb","app","lastStart",st)
  SQL.storeValue("idb","app","version",__meta["version"])
try:
  a0=sys.argv[1]
except:
  a0=Path.home().joinpath(".ump","config.json")
  a0=str(a0)
try:
  a1=sys.argv[2]
  if a1 == "q00":
    print("UMP Startup Interupted with flag "+r.CBOLD+"q00"+r.CEND)
    Debug.load(a0,False)
    Debug.clearLog()
    os._exit(0)
  else:
    a1=bool(a1)
except:
  a1=True
print("argument 0 = "+a0+"\nargument 1 = "+str(a1))
init(a0,a1)
Debug.log("Main","Universal Media Player "+vshrt,0)
User.openUserWindow()