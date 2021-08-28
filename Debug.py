__meta={"type":"internal_script","name":"Debug","version":[0,0,0,0]}
import json
import Resources as r
def load(confLocation,dbgmd):
  u=open(confLocation,"r")
  c=json.loads(u.read())
  u.close()
  global ll
  ll=c["dirs"]["homeDir"]+c["logFile"]
  global debugmode
  debugmode = dbgmd 
def log(src,msg,lvl):
  """Creates a log entry and sends data to stdout. src defines the source, msg defines the message, and lvl defines the log level. Valid inputs for lvl are: 0 (Info), 1 (Log), 2 (Warning), 3 (Error), and 4 (Debug)."""
  l=open(ll,"a")
  if lvl==0:
    print(r.CBLUEBG+"[INF]["+r.CBOLD+src+r.CEND+r.CBLUEBG+"]: "+msg+r.CEND)
    l.write(src+",Info,"+msg+"\n")
  elif lvl==1:
    print(r.CGREEN+"[LOG]["+r.CBOLD+src+r.CEND+r.CGREEN+"]: "+msg+r.CEND)
    l.write(src+",Log,"+msg+"\n")
  elif lvl==2:
    print(r.CYELLOWBG+"[WRN]["+r.CBOLD+src+r.CEND+r.CYELLOWBG+"]: "+msg+r.CEND)
    l.write(src+",Warning,"+msg+"\n")
  elif lvl==3:
    print(r.CREDBG+"[ERR]["+r.CBOLD+src+r.CEND+r.CREDBG+"]: "+msg+r.CEND)
    l.write(src+",Error,"+msg+"\n")
  elif lvl==4:
    if debugmode == True:
      print(r.CVIOLETBG+"[DBG]["+r.CBOLD+src+r.CEND+r.CVIOLETBG+"]: "+msg+r.CEND)
    l.write(src+",Debug,"+msg+"\n")
  l.close()
def clearLog():
  print("Clearing Log File...")
  l=open(ll,"w")
  l.write("")
  l.close()
  print("Done!")