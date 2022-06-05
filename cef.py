from cefpython3 import cefpython as cef
import sys

sys.excepthook = cef.ExceptHook  
cef.Initialize()
cef.CreateBrowserSync(url="https://www.bing.com")
cef.MessageLoop()
cef.Shutdown()