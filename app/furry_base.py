import time
import json
import os
import threading
import atexit
import socket
import traceback
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image
import pystray
from app.config import dataDir, appSettings as globalAppSettings

class FurryBase:
    def applicationClock(self, arg1 = None, tickDelay = 500):
        self.mainWindow.after(tickDelay, self.applicationClock)

    def reinit(self):
        self.configEncodings = ['utf-8', 'gbk', 'gb2312', 'ANSI']
        with open((dataDir + "/fileList.json"), 'r', encoding = 'utf-8', errors = 'ignore') as flistfe:
            flistdata = json.loads(flistfe.read())
            self.appPath = dataDir + '/' + flistdata['application']['dir']
            print(self.appPath)
        self.cfgPath = self.appPath + '/' + flistdata['application']['mainCfgFile']
        with open(self.cfgPath, 'r', encoding = 'utf-8', errors = 'ignore') as cfgfe:
            self.appSettings = json.loads(cfgfe.read())
            self.windowTransparentColor = self.appSettings['advanced']['transparentColor']
        self.shellOutput('Loaded application settings: {s}'.format(s = self.cfgPath))
        self.appLangPath = self.appPath + '/' + self.appSettings['application']['langDir']
        self.langLoadSuccess = False
        for x in self.configEncodings :
            try :
                with open((self.appLangPath + '/' + self.appSettings['application']['langCfgFile']), 'r', encoding = x) as langfe :
                    self.appLangData = json.loads(langfe.read())
                    self.currentLangData = self.appLangData['Lang']
                    self.langLoadSuccess = True
            except :
                continue
        if self.langLoadSuccess == False :
            with open((self.appLangPath + '/' + self.appSettings['application']['langCfgFile']), 'r', encoding = 'utf-8', errors = 'ignore') as langfe :
                self.appLangData = json.loads(langfe.read())
                self.currentLangData = self.appLangData['lang']
        self.shellOutput('Loaded lang data: {s}({t}, Version {u})'.format(s = self.appLangData['name'], t = self.appLangData['type'], u = self.appLangData['ver']))

        self.userDir = self.appPath + '/' + self.appSettings['user']['userCfgDir']
        self.normalUser = self.appSettings['user']['normalUser']
        self.normalUserDir = self.userDir + '/' + self.appSettings['user']['userList'][self.normalUser]['dir']
        try :
            self.userMainCfgFile = self.normalUserDir + '/' + self.appSettings['user']['userList'][self.normalUser]['mainCfgFile']
            with open(self.userMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore'):
                pass
            self.shellOutput('Loaded user config file: {s}'.format(s = self.userMainCfgFile))
        except :
            self.shellOutput('[X]Set user config file load failed.')
            self.userMainCfgFile = self.normalUserDir + '/userConfigs.json'
            self.shellOutput('Loaded user config file: {s}'.format(s = ('')))
        userCfgReadSuccess = False
        userConfigData = None
        for x in self.configEncodings :
            try :
                with open(self.userMainCfgFile, 'r', encoding = x) as f:
                    userConfigData = f.read()
                userCfgReadSuccess = True
                break
            except :
                continue
        if userCfgReadSuccess == False :
            with open(self.userMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore') as f:
                userConfigData = f.read()
        self.userCfgData = json.loads(userConfigData)
        self.onlineSearchAddress = self.userCfgData['onlineServiceData']['searchAddress']
        self.automaticData = self.userCfgData['automaticData']
        self.menuList = []
        self.menuClick1 = 0
        self.shellOutput('Loaded user: {s}(UserID Length: {t})'.format(s = self.userCfgData['standardData']['userName'], t = len(self.userCfgData['standardData']['userID'])))

        self.furryDir = dataDir + '/' + flistdata['application']['dir'] + '/' + self.appSettings['furry']['furryCfgDir']
        self.normalFurry = self.userCfgData['standardData']['loadedFurry']
        self.normalFurryDir = self.furryDir + '/' + self.appSettings['furry']['furryList'][self.normalFurry]['dir']
        try :
            self.furryMainCfgFile = self.normalFurryDir + '/' + self.appSettings['furry']['furryList'][self.normalFurry]['mainCfgFile']
            with open(self.furryMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore'):
                pass
        except :
            self.furryMainCfgFile = self.normalFurryDir + '/furryConfigs.json'
            print(self.furryMainCfgFile)
        furryCfgReadSuccess = False
        furryConfigData = None
        for x in self.configEncodings :
            try :
                with open(self.furryMainCfgFile, 'r', encoding = x) as f:
                    furryConfigData = f.read()
                furryCfgReadSuccess = True
                break
            except :
                continue
        if furryCfgReadSuccess == False :
            with open(self.furryMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore') as f:
                furryConfigData = f.read()
        self.furryCfgData = json.loads(furryConfigData)
        self.furryImagePath = self.normalFurryDir + '/' + self.furryCfgData['standardData']['imagePath']
        self.furryImages = self.furryCfgData['standardData']['images']
        self.furryAction = self.furryCfgData['standardData']['normalImage']
        self.bgImage = None
        self.furryImage = None
        self.furryTag = self.furryCfgData['standardData']['tag']
        self.shellOutput('Loaded furry: {s}(Builtin Tag: {t})'.format(s = self.furryCfgData['standardData']['name'], t = self.furryCfgData['standardData']['tag']))

        self.furryLangPath = self.normalFurryDir + '/' + self.furryCfgData['standardData']['customizedLangPath'] + '/'
        self.furryLangLoadSuccess = False
        for x in self.configEncodings :
            try :
                with open((self.furryLangPath + '/' + self.furryCfgData['standardData']['customizedLangs'][self.appLangData['type']]), 'r', encoding = x) as furrylangfe :
                    self.furryLangData = json.loads(furrylangfe.read())
                    self.currentFurryLangData = self.furryLangData['lang']
                    self.furryLangLoadSuccess = True
            except :
                continue
        if self.furryLangLoadSuccess == False :
            with open((self.appLangPath + '/' + self.appSettings['application']['langCfgFile']), 'r', encoding = 'utf-8', errors = 'ignore') as furrylangfe :
                self.furryLangData = json.loads(furrylangfe.read())
                self.currentFurryLangData = self.furryLangData['lang']
        self.shellOutput('Loaded customized furry lang data: {s}({t}, Version {u})'.format(s = self.appLangData['name'], t = self.appLangData['type'], u = self.appLangData['ver']))

        self.tmpWindow = Toplevel()
        self.tmpWindow.withdraw()
        self.tmpWindow.geometry('+{x}+{y}'.format(x = int(1/16 * self.mainWindow.winfo_screenwidth()), y = int(1/16 * self.mainWindow.winfo_screenheight())))

        self.noteBoardWindow = Toplevel()
        self.noteBoardWindow_entry = Text(self.noteBoardWindow)
        self.noteBoardWindow_entry.place(x = 0, y = 0)
        self.noteBoardWindow_entry.insert(0.0, self.loadCurrentLang(key = 'noteBoardNormalText'))
        self.noteBoardWindow.iconbitmap((self.appPath + '/' + self.appSettings['application']['iconDir'] + '/' + self.appSettings['application']['windowIcon']))
        self.noteBoardWindow.title(self.loadCurrentLang(key = 'noteBoardTitle'))
        self.noteBoardWindow.protocol('WM_DELETE_WINDOW', self.hideNoteBoard)
        self.noteBoardWindow.bind('<Configure>', self.noteBoardWindowUpdate)
        self.noteBoardWindow.withdraw()
        self.noteBoardWindowSides = {'x' : 2, 'y' : 2}

        self.strayMenu = [pystray.MenuItem(self.getLang(key = 'furryInfo', fromDic = self.currentLangData), self.aboutApp),
                          pystray.Menu.SEPARATOR,
                          pystray.Menu.SEPARATOR,
                          pystray.MenuItem(self.getLang(key = 'showOrHide', fromDic = self.currentLangData), self.showOrHide),
                          pystray.MenuItem(self.getLang(key = 'toolMenu', fromDic = self.currentLangData), self.showOrHideMenu),
                          pystray.Menu.SEPARATOR,
                          ]
        self.strayMenu_Hidden = [pystray.MenuItem(self.getLang(key = 'appHelp', fromDic = self.currentLangData), self.underConstruction),
                                 pystray.MenuItem(self.getLang(key = 'appSettings', fromDic = self.currentLangData), self.appSettings_menuLauncher)
                                 ]
        self.strayMenu_insertPos = 6
        if (self.appSettings['advanced']['enableSuperSecret'] == True) or (self.appSettings['advanced']['debugMode'] == True) :
            for x in self.strayMenu_Hidden :
                self.strayMenu.insert(self.strayMenu_insertPos, x)
                self.strayMenu_insertPos += 1
        self.furryStrayIconImage = Image.open((self.appPath + '/' + self.appSettings['application']['iconDir'] + '/' + self.appSettings['application']['strayIcon']))
        self.furryStray = pystray.Icon(globalAppSettings['appName'], self.furryStrayIconImage, self.getLang(key = 'strayInfo', fromDic = self.currentLangData), self.strayMenu)

        if (self.userCfgData['standardData']['OOBELoaded'] == False) or (self.userCfgData['advancedData']['rootUser'] == True and self.appSettings['advanced']['rootAllowed'] == False) :
            self.shellOutput('[i]OOBE is not loaded.Starting OOBE...')
            self.appOOBE()

        self.shellOutput('Application settings loaded.')

    def __init__(self, windowWidth = 128, windowHeight = 128):
        try :
            self.windowWidth = windowWidth
            self.windowHeight = windowHeight

            self.mainWindow = Toplevel()
            self.mainWindow.config(width = self.windowWidth, height = self.windowHeight)

            self.mainWindow.withdraw()
            self.reinit()

            self.mainWindow.iconbitmap((self.appPath + '/' + self.appSettings['application']['iconDir'] + '/' + self.appSettings['application']['windowIcon']))

            try :
                self.mainWindow.title(self.appSettings['application']['normalTitle'])
            except :
                pass
            try :
                self.mainWindow.title(self.furryCfgData['standardData']['windowTitle'])
            except :
                pass

            self.mainWindow.attributes('-topmost', 'true')
            try :
                self.mainWindow.attributes('-toolwindow', 'true')
            except :
                self.shellOutput('[!]self.mainWindow:Host operating system does not support "toolwindow".')
            self.mainWindow.resizable(0, 0)
            self.scr = Canvas(self.mainWindow, width = self.windowWidth, height = self.windowHeight, highlightthickness = 0)
            self.scr.place(x = 0, y = 0, width = self.windowWidth, height = windowHeight, anchor = 'nw')

            self.rightMenu = Menu(self.mainWindow, tearoff = False)
            self.rightMenu.add_command(label = self.getLang(key = 'furryInfo', fromDic = self.currentLangData), command = self.aboutApp)
            self.rightMenu.add_command(label = self.addSign(text = self.loadCurrentLang(key = 'showOrHide'), sign = 'enter'), command = self.showOrHide)
            self.rightMenu.add_command(label = self.addSign(text = self.getLang(key = 'toolMenu', fromDic = self.currentLangData), sign = 'enter'), command = self.showOrHideMenu)
            if (self.appSettings['advanced']['enableSuperSecret'] == True) or (self.appSettings['advanced']['debugMode'] == True) :
                self.rightMenu.add_command(label = self.addSign(text = self.getLang(key = 'appSettings', fromDic = self.currentLangData), sign = 'enter'), command = self.appSettings_menuLauncher)
                self.rightMenu.add_command(label = self.addSign(text = self.getLang(key = 'appHelp', fromDic = self.currentLangData), sign = 'help'), command = self.underConstruction)
            self.rightMenu.add_command(label = self.addSign(text = self.getLang(key = 'quit', fromDic = self.currentLangData), sign = 'enter'), command = self.quitApp)

            posValid = False
            try :
                if (type(self.userCfgData['featureData']['savedMainWindowPos']['x']) != int) or (type(self.userCfgData['featureData']['savedMainWindowPos']['y']) != int):
                    posValid = False
                else :
                    posValid = True
                    self.mainWindow.geometry('+{x}+{y}'.format(x = self.userCfgData['featureData']['savedMainWindowPos']['x'], y = self.userCfgData['featureData']['savedMainWindowPos']['y']))
            except :
                posValid = False
            if posValid == False :
                try :
                    self.mainWindowPosReset(x_move = self.appSettings['advanced']['windowPosMove'][0], y_move = self.appSettings['advanced']['windowPosMove'][1])
                except :
                    self.mainWindowPosReset()
            self.mainWindow.protocol('WM_DELETE_WINDOW', self.hideWindow)
            self.draw()
            self.windowPopup = False
            self.active = False
            self.mainWindow.withdraw()

            self.popupMenuWindow = Toplevel()
            self.popupMenuWindow.attributes('-topmost', 'true')
            self.popupMenuWindow.iconbitmap((self.appPath + '/' + self.appSettings['application']['iconDir'] + '/' + self.appSettings['application']['windowIcon']))
            self.popupMenuWindow.resizable(0, 0)
            try :
                self.popupMenuWindow.attributes('-toolwindow', 'true')
            except :
                self.shellOutput('[X]self.popupMenuWindow:Host operating system does not support ToolWindow.')
            self.popupMenuWindow.protocol('WM_DELETE_WINDOW', self.showOrHideMenu)
            self.popupMenuWindow.withdraw()
            self.menuPopup = False

            self.scr.tag_bind(self.furryCfgData['standardData']['tag'], "<Button-1>", self.showOrHideMenu)
            self.scr.tag_bind(self.furryCfgData['standardData']['tag'], "<Button-3>", self.showRightMenu)
            self.mainWindow.bind('<Configure>', self.onMainWindowMove)

            self._1_ = False
            self.menuCmdEditWindowActive = False
            self.appSettingsWindowActive = False
            self.appLaunchPermission = True
            if self.appSettings['advanced']['enableApplicationLock'] == True :
                try :
                    try :
                        testPort = int(self.appSettings['advanced']['applicationLockPort'])
                    except :
                        self.appSettings['advanced']['applicationLockPort'] = 5033
                    self.furryToPreventMultiple = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.furryToPreventMultiple.bind(('localhost', self.appSettings['advanced']['applicationLockPort']))
                    atexit.register(self.furryToPreventMultiple.close)
                except :
                    self.appLaunchPermission = False
        except Exception as errData :
            messagebox.showerror('ERROR', 'Failed to load data. The application will be closed.\nMake sure the asset files are available and the assets are valid, then launch the application again.\nException Data:\n{data}'.format(data = '\n'.join([str(errData.__traceback__), str(traceback.extract_tb(errData.__traceback__)), str(type(errData))])))
            quit()
        self.shellOutput('Application Launched.')

    def startFurry(self):
        if self.appLaunchPermission == False :
            messagebox.showerror(self.loadCurrentLang(key = 'messageTitleError'), self.loadCurrentLang(key = 'messageErrorAlreadyRunning').format(s = self.appSettings['advanced']['applicationLockPort']))
            self.quitFurry(resetPerm = False)
        self.showWindow()
        threading.Thread(target = self.furryStray.run, daemon = True).start()
        self.applicationClock()
        if self.userCfgData["advancedData"]["hideFurryWhenStartup"] == True :
            self.showOrHide()
            self.furryStray.notify(self.loadCurrentLang(key = 'messageHideWhenStartup'), self.loadCurrentLang(key = 'messageTitleHide'))
        self.mainWindow.mainloop()

    def quitFurry(self, saveData = True, resetPerm = True):
        if saveData == True :
            self.saveData()
        self.shellOutput('Quitting furry...\n')
        try :
            self.popupMenuWindow.destroy()
        except :
            pass
        try :
            self.mainWindow.destroy()
        except :
            pass
        try :
            self.furryStray.stop()
        except :
            pass
        try :
            self.furryToPreventMultiple.close()
        except :
            pass
        self.mainWindow.quit()
        quit()

    def quitApp(self, arg1 = None):
        ans = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleRecheck'), self.loadCurrentLang(key = 'messageQuit'))
        if ans == True :
            self.quitFurry()
