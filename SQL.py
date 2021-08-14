__meta={"type":"internal_script","name":"SQL","version":[0,0,0,0]}
import Debug
import Config
import sqlite3
import Resources as r
def init():
  dbl=Config.conf["dirs"]["homeDir"]+"/.ump/db/"
  try:
    userdb=sqlite3.connect(dbl+"user.db")
  except sqlite3.OperationalError:
    Debug.log("SQL","Cannot Load User Database from "+dbl+"user.db . It may be in use or nonexistant alltogether!",3)
  else:
    global udbcur
    udbcur=userdb.cursor()
    udbcur.execute('''CREATE TABLE IF NOT EXISTS users(uname TEXT, pfp TEXT, fullname TEXT, isDefaultUser BOOL, lang TEXT)''')
    Debug.log("SQL","Loaded User Database from "+dbl+"user.db",1)
  
  try:
    medialib=sqlite3.connect(dbl+"medialib.db")
  except sqlite3.OperationalError:
    Debug.log("SQL","Cannot Load Media Library from "+dbl+"medialib.db . It may be in use or nonexistant alltogether!",3)
  else:
    global mlcur
    mlcur=medialib.cursor()
    Debug.log("SQL","Loaded Media Library from "+dbl+"medialib.db",1)
  
  try:
    internaldb=sqlite3.connect(dbl+"internaldb.db")
  except sqlite3.OperationalError:
    Debug.log("SQL","Cannot Load Internal Database from "+dbl+"internaldb.db . It may be in use or nonexistant alltogether!",3)
  else:
    global idbcur
    idbcur=internaldb.cursor()
    idbcur.execute('''CREATE TABLE IF NOT EXISTS app(variable TEXT, value TEXT)''')
    Debug.log("SQL","Loaded Internal Database from "+dbl+"internaldb.db",1)
def storeValue(db,table,variable,value):
  if db=="idb":
    idbcur.execute(r.DSQL["MINSERT0"].format(table,variable,value))
    Debug.log("SQL","Stored the value of "+variable+" as "+str(value)+" inside of the "+table+" table of the Internal Database.",4)
  elif db=="udb":
    udb