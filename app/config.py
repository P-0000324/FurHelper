"""
--==P0000324 Coding==--
FurHelper 0.1.0042
26.05.30
========
"""

from tkinter import Tk
import os
import json
import pystray
from PIL import Image
import threading
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
    "ver" : "0.1.0042",
    "versionTag" : "Beta",
    "releaseTips" : "A furry that helps you!",
    "relDate" : "26.05.30",
    "firstRelDate" : "25.06.24",
    "firstRelTime" : "11:02",
    "betaTags" : [
        "Beta"
        ],
    "developers" : [
        "P0000324"
        ],
    "license" : "Copyright (C) 2025, 2026 P0000324"
    }

dataDir = "./Data/"

cl1 = Tk(className = ' ')
cl1.withdraw()
