CEND='\33[0m'
CBOLD='\33[1m'
CITALIC='\33[3m'
CURL='\33[4m'
CBLINK='\33[5m'
CBLINK2='\33[6m'
CSELECTED='\33[7m'
CBLACK='\33[30m'
CRED='\33[31m'
CGREEN='\33[32m'
CYELLOW='\33[33m'
CBLUE='\33[34m'
CVIOLET='\33[35m'
CBEIGE='\33[36m'
CWHITE='\33[37m'
CBLACKBG='\33[40m'
CREDBG='\33[41m'
CGREENBG='\33[42m'
CYELLOWBG='\33[43m'
CBLUEBG='\33[44m'
CVIOLETBG='\33[45m'
CBEIGEBG='\33[46m'
CWHITEBG='\33[47m'
CGREY='\33[90m'
CRED2='\33[91m'
CGREEN2='\33[92m'
CYELLOW2='\33[93m'
CBLUE2='\33[94m'
CVIOLET2='\33[95m'
CBEIGE2='\33[96m'
CWHITE2='\33[97m'
CGREYBG='\33[100m'
CREDBG2='\33[101m'
CGREENBG2='\33[102m'
CYELLOWBG2='\33[103m'
CBLUEBG2='\33[104m'
CVIOLETBG2='\33[105m'
CBEIGEBG2='\33[106m'
CWHITEBG2='\33[107m'
DSETUP={
  "TOUCH":["/config.json","/log","/db/","/db/user.db","/db/medialib.db","/db/internal.db"]
}
DDFLT={
  "HOMEDIR":{
    "Linux":"/home/{}",
    "Windows":"{}\\Users\\{}",
    "Android":"/storage/emulated/0"
  }
}
DALL={
  "OS":{
    "Android":False,
    "Windows":False,
    "Linux":True,
    "MacOS":False
  }
}
DSQL={
  "MINSERT0":'''INSERT INTO {}(variable, value) VALUES ('{}', '{}')''',  # Table, Variable, Value
  "MINSERT1":'''INSERT INTO users(uname, pfp, fullname, isDefaultUser, lang) VALUES ('{}', '{}', '{}', {}, '{}')''',
  "MINSERT2":'''INSERT INTO config(flag, value) VALUES ('{}', '{}')''',
  "MINSERT3":'''INSERT INTO {}_httpreqhistory(url, method, datetime, responceCode) VALUES ('{}', '{}', '{}', {})''',
  "MCREATE0":'''CREATE TABLE IF NOT EXISTS {}(id INTEGER, url TEXT, mime TEXT)'''
}
DMIME={ #TODO: Add all mime types.
  "audio/x-psf":{"name":"Playstation Sound Format","suffixes":[".minipsf"]},
  "audio/mpeg":{"name":"MP3 Audio","suffixes":[".mp3"]}
}
DAS={
  "DMSG":["The Audio Server is starting..."]
}