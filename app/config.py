"""
--==P0000324 Coding==--
FurHelper 0.1.0046
26.08.27
========
1)
"""

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import os
import json
import pystray
from PIL import Image, ImageTk
import threading
#import multiprocessing
import random
import platform
import time
import traceback
import webbrowser
import tempfile
import socket
import sys
import atexit

appSettings = {
    "appName" : "FurHelper",
    "verName" : "GoldEarBay",
    "ver" : "0.1.0046",
    "versionTag" : "Beta",
    "releaseTips" : "A furry that helps you!",
    "relDate" : "26.08.27",
    "firstRelDate" : "25.06.24",
    "firstRelTime" : "11:02",
    "betaTags" : [
        "Beta"
        ],
    "developers" : [
        "P0000324(Main Programmer)",
        "DianziNoDianZi(Great Technical Support!)"
        ],
    "license" : "Copyright (C) 2025, 2026 P0000324"
    }

dataDir = "./Data/"

cl1 = Tk(className = ' ')
cl1.withdraw()
