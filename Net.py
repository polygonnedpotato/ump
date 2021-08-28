__meta={"type":"internal_script","name":"Net","version":[0,0,0,0]}
import SQL
import Debug
import requests
import datetime as dt
class HTTPRequestObject:
  def __init__(sf,src):
    sf.src=src
  def get(sf,url):
    sf.url=url
    Debug.log("Net","Making a 'GET' request to "+sf.url,4)
    sf.r=requests.get(sf.url)
    print(sf.src,sf.r.url,sf.r.status_code,)
    SQL.storeHTTPRequest(sf.src,sf.r.url,"GET",dt.datetime.now(),sf.r.status_code)
    return sf.r.text
