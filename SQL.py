__meta={"type":"internal_script","name":"SQL","version":[0,0,0,0]}
from psutil import NETBSD
import Debug
import Config
import sqlite3
import Resources as r
from datetime import datetime as dt
def init():
  dbl=Config.conf["dirs"]["homeDir"]+"/.ump/db/"
  try:
    global userdb
    userdb=sqlite3.connect(dbl+"user.db")
  except sqlite3.OperationalError:
    Debug.log("SQL","Cannot Load User Database from "+dbl+"user.db . It may be in use or nonexistant alltogether!",3)
  else:
    global udbcur
    udbcur=userdb.cursor()
    udbcur.execute('''CREATE TABLE IF NOT EXISTS users(uname TEXT, pfp TEXT, fullname TEXT, isDefaultUser BOOL, lang TEXT)''')
    Debug.log("SQL","Loaded User Database from "+dbl+"user.db",1)
  
  try:
    global medialib
    medialib=sqlite3.connect(dbl+"medialib.db")
  except sqlite3.OperationalError:
    Debug.log("SQL","Cannot Load Media Library from "+dbl+"medialib.db . It may be in use or nonexistant alltogether!",3)
  else:
    global mlcur
    mlcur=medialib.cursor()
    Debug.log("SQL","Loaded Media Library from "+dbl+"medialib.db",1)
  
  try:
    global internaldb
    internaldb=sqlite3.connect(dbl+"internaldb.db")
  except sqlite3.OperationalError:
    Debug.log("SQL","Cannot Load Internal Database from "+dbl+"internaldb.db . It may be in use or nonexistant alltogether!",3)
  else:
    global idbcur
    idbcur=internaldb.cursor()
    idbcur.execute('''CREATE TABLE IF NOT EXISTS app(variable TEXT, value TEXT)''')
    Debug.log("SQL","Loaded Internal Database from "+dbl+"internaldb.db",1)
  try:
    global netdb
    netdb=sqlite3.connect(dbl+"netdb.db")
  except sqlite3.OperationalError:
    Debug.log("SQL","Cannot Load Network Database from "+dbl+"netdb.db . It may be in use or nonexistant alltogether!",3)
  else:
    global ndbcur
    ndbcur=netdb.cursor()
    ndbcur.execute('''CREATE TABLE IF NOT EXISTS config(flag TEXT, value TEXT)''')
    ndbcur.execute('''CREATE TABLE IF NOT EXISTS internal_httpreqhistory(url TEXT, method TEXT, datetime TEXT, responceCode INT)''')
    ndbcur.execute('''CREATE TABLE IF NOT EXISTS httpcache(url TEXT, mime TEXT DEFAULT 'text/plain', contents LONGTEXT)''')
    Debug.log("SQL","Loaded Network Database from "+dbl+"netdb.db",1)
def storeInternalValue(table,variable,value):
  """Stores a value into the internal database (.ump/db/internaldb.db). If a value does not exist, it will be created."""
  idbcur.execute(r.DSQL["MINSERT0"].format(table,variable,value))
  internaldb.commit()
  Debug.log("SQL","Stored the value of "+variable+" as "+str(value)+" inside of the "+table+" table of the Internal Database.",4)
def createUser(uname,pfp,fullname,isDefaultUser,lang):
  """Creates new data for a user."""
  udbcur.execute(r.DSQL["MINSERT1"].format(uname,pfp,fullname,isDefaultUser,lang))
  userdb.commit()
  Debug.log("SQL","Created User Data for '"+uname+"'.",4)
def storenetflag(flag,value):
  """Stores a value for the Network service."""
  ndbcur.execute(r.DSQL["MINSERT2"].format(flag,value))
  netdb.commit()
  Debug.log("SQL","Stored data for Net Flag "+flag+".",4)
def storeHTTPRequest(table,url,method,datetime,responceCode):
  """Stores HTTP Request Data."""
  ndbcur.execute(r.DSQL["MINSERT3"].format(table,url,method,datetime,responceCode))
  netdb.commit()
  Debug.log("SQL","Stored HTTP Request data.",4)