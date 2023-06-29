import snap7
from ctypes import cdll
plc = snap7.client.Client()

plc.connect('192.168.0.1', 0,1)

data = plc.plc_stop