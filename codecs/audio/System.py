__meta={
  "type":"codec",
  "codecType":"audio-codec",
  "name":"System Decoder",
  "author":"Brendan Berger",
  "version":[0,0,0,0],
  "acceptsMIME":["audio/mpeg"]
}
from Tkinter import *
class MediaDecoder:
  def __init__(sf,decoder):
    if sf.decoder=="tkSnack":
      root = Tk()
      import tkSnack
      tkSnack.initializeSnack(root)
      sf.sndbffr = tkSnack.Sound()
  def loadFile(sf,file):
    if sf.decoder=="tkSnack":
      sf.sndbffr.read(sf.file)
  def getStatus(sf):
    return {"isPlaying":sf.playing,"file":sf.file,"decoder":sf.decoder}
  def play(sf):
    if sf.decoder=="tkSnack":
      sf.playing=True
      sf.sndbffr.play()
      sf.playing=False
  def pause(sf):
    if sf.decoder=="tkSnack":
      sf.sndbffr.pause()
      sf.playing=False
  def stop(sf):
    if sf.decoder=="tkSnack":
      sf.sndbffr.stop()
      sf.playing=False