from win32api import GetMonitorInfo
from win32api import MonitorFromPoint
import math

monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
monitor = monitor_info.get('Monitor')
WIDTH_PIX: int = monitor_info.get('Monitor')[2]  
HEIGHT_PIX: int = monitor_info.get('Monitor')[3]

# 字体大小
dW = 9
dH = 9

WIDTH = WIDTH_PIX // dW
HEIGHT = HEIGHT_PIX // dH - 1

PI = math.pi