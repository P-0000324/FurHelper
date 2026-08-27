import random
import time
from tkinter import messagebox

class FurryI18N:
    def getLang(self, key = 'DEBUG', fromDic = {'DEBUG' : "DEBUG"}, mode = 'key', text = 'DEBUG', split = True, splitTag = '$$', forceListOutput = False, popEmptyLines = False, outputError = False):
        def work(text = 'DEBUG'):
            txtOutput = text.format(appName = self.appSettings['appName'],
                                    verName = self.appSettings['verName'],
                                    appVer = self.appSettings['ver'],
                                    appVerTag = self.appSettings['versionTag'],
                                    relTips = self.appSettings['releaseTips'],
                                    relDate = self.appSettings['relDate'],
                                    appDevelopers = ', '.join(self.appSettings['developers']),
                                    appLicense = self.appSettings['license'],
                                    appLang = self.appLangData['name'],
                                    superSecretState = superSecretState,

                                    userName = self.userCfgData['standardData']['userName'],
                                    userID = self.userCfgData['standardData']['userID'],
                                    userIDLength = len(self.userCfgData['standardData']['userID']),

                                    furryName = self.furryCfgData['standardData']['name'],
                                    furryRelDate = self.furryCfgData['standardData']['relDate'],
                                    furryDevelopers = ', '.join(self.furryCfgData['standardData']['developers']),
                                    furryLicense = self.furryCfgData['standardData']['license'],

                                    OOBEUsrName = '{OOBEUsrName}',
                                    OOBESearchAdd = '{OOBESearchAdd}',
                                    OOBEHideWhenStartup = '{OOBEHideWhenStartup}',
                                    OOBEUserControlLevel = '{OOBEUserControlLevel}',

                                    splitLine = '--==*==--',

                                    s = '{s}'
                                    )
            return txtOutput
        temp = None
        mode = mode.lower()
        superSecretState = ''
        if self.appSettings['advanced']['enableSuperSecret'] == True :
            superSecretState = '[SUPER SECRET ENABLED]'
        if mode == 'key' :
            try :
                temp = fromDic[key]
            except :
                if outputError == True :
                    raise KeyError('Invalid key: {key}'.format(key = key))
                else :
                    self.shellOutput('[X]Invalid key {key}'.format(key = key))
                    temp = 'python.lang.NullPointerException'
        elif mode == 'text' :
            temp = text
        else :
            print('[X]Invalid mode {mode}. Will use mode "text".'.format(mode = mode))
            temp = text
        if type(temp) in [set, list, tuple] :
            temp = str(random.choice(temp))
        else :
            temp = str(temp)
        if split == True :
            temp = temp.split(splitTag)
        if type(temp) == str :
            temp = work(temp)
        else :
            for x in range(len(temp)):
                temp[x] = work(temp[x])
        if type(temp) == list and len(temp) == 1 and forceListOutput == False :
            temp = temp[0]
        if popEmptyLines == True :
            if type(temp) == str :
                temp1 = temp.split('\n')
                temp2 = []
            for x in temp1 :
                if (x != '') and (x.isspace() == False) :
                    temp2.append(x)
            if type(temp) == str :
                temp = '\n'.join(temp2)
            else :
                temp = temp2.copy()
        return temp

    def loadCurrentLang(self, key = 'empty', popEmptyLines = False, forceApplicationLang = False):
        try :
            if (forceApplicationLang == True) or (self.appSettings['advanced']['forceApplicationLangData'] == True) :
                raise ValueError('Forced application language')
            txt = self.getLang(key = key, fromDic = self.currentFurryLangData, popEmptyLines = popEmptyLines, outputError = True)
        except :
            txt = self.getLang(key = key, fromDic = self.currentLangData, popEmptyLines = popEmptyLines)
        return txt

    def shellOutput(self, text = 'SHELL OUTPUT DEBUG', withGUI = False, withTime = True, toLog = True):
        if withGUI == True :
            messagebox.showinfo('Shell Output', text)
        else :
            print(text)
        if withTime == True :
            dttm = '[{date} {time}]'.format(date = time.strftime('%y.%m.%d'), time = time.strftime('%H:%M:%S'),)
        else :
            dttm = ''
        if (self.appSettings['advanced']['writeToLog'] == True) and (toLog == True) :
            with open(str(self.appPath + '/' + self.appSettings['advanced']['logDir'] + '/' + self.appSettings['advanced']['logFileNameTemplate'].format(date = time.strftime('%y%m%d'), time = time.strftime('%H%M%S'), appendix = '.log')), 'a', encoding = 'utf-8') as fe :
                fe.write('{dttm}{s}\n'.format(dttm = dttm, s = text))

    def addSign(self, text = '', sign = 'none'):
        signs = {
            "none" : "",
            "info" : "(i)",
            "enter" : "(=>)",
            "forward" : "(=>)",
            "back" : "(<=)",
            "command" : "(*)",
            "warning" : "(!)",
            "help" : "(?)",
            "error" : "(X)",
            "close" : "(X)",
            "add" : "(+)",
            "remove" : "(-)",
            "cancel" : "(-)"
            }
        txtOutput = text
        signToAdd = sign.lower()
        try :
            signTemp = signs[signToAdd]
        except :
            self.shellOutput("(X)Unable to load sign {s}".format(s = signToAdd))
            signTemp = ''
        txtOutput = str(signTemp) + str(text)
        return txtOutput

    def aboutAppGUI(self, arg1 = None, windowWidth = 640, windowHeight = 440, sideMove = 8, objectMove = 4, singleObjectHeight = 30):
        def aboutAppWindow_close(arg1 = None):
            self.aboutAppWindow.destroy()
        self.aboutAppWindow = Toplevel()
        self.aboutAppWindow.config(width = windowWidth, height = windowHeight)
        self.aboutAppWindow.resizable(0, 0)
        self.aboutAppWindow.title(self.loadCurrentLang(key = 'messageTitleAbout'))
        self.aboutAppWindow.iconbitmap((self.appPath + '/' + self.appSettings['application']['iconDir'] + '/' + self.appSettings['application']['windowIcon']))
        self.aboutAppWindow.geometry('+{x}+{y}'.format(x = (self.mainWindow.winfo_screenwidth() // 2 - windowWidth // 2), y = (self.mainWindow.winfo_screenheight() // 2 - windowHeight // 2)))

        self.aboutAppWindowTitle = Label(self.aboutAppWindow, text = self.loadCurrentLang(key = 'messageTitleAbout'), font = ('', 36), fg = 'red', anchor = 'w')
        self.aboutAppWindow_appIcon = Canvas(self.aboutAppWindow, highlightthickness = 0)
        self.aboutAppWindow_text = Label(self.aboutAppWindow, text = 'DEBUG', anchor = 'nw', justify = 'left')
        self.aboutAppWindow_btnClose = Button(self.aboutAppWindow, text = self.loadCurrentLang(key = 'btnClose'), command = aboutAppWindow_close)

        txt = self.loadCurrentLang(key = 'messageAbout', popEmptyLines = True)
        superSecret1 = False #...?
        superSecret2 = False
        if time.strftime('%m%d') == '0401' and random.randint(301, 400) == 324 :
            superSecret1 = True
        if time.strftime('%m%d') == '0528' :
            superSecret2 = True
        if superSecret1 == True :
            txt = txt.split('\n')
            for x in range(len(txt)):
                txt[x] = '\u202e' + txt[x]
            txt.append('\n[!]Aha! April fool!:)')
            txt = '\n'.join(txt)
        if superSecret2 == True :
            txt = txt.split('\n')
            txt.append('\n[\\n-n/ Happy birthday, P0000324!]')
            txt = '\n'.join(txt)

        self.aboutAppWindow_text.config(text = txt)

        appIconImage = Image.open((self.appPath + '/' + self.appSettings['application']['iconDir'] + '/' + self.appSettings['application']['strayIcon']))
        appIconImage = appIconImage.resize((128, 128))
        self.aboutAppWindow_iconImage = ImageTk.PhotoImage(appIconImage)
        self.aboutAppWindow_appIcon.create_image(0, 0, image = self.aboutAppWindow_iconImage, anchor = 'nw')

        self.aboutAppWindowTitle.place(x = int(sideMove + objectMove + 128), y = sideMove, width = int(windowWidth - int(sideMove + objectMove + 128) - sideMove), height = int(2 * singleObjectHeight), anchor = 'nw')
        self.aboutAppWindow_appIcon.place(x = sideMove, y = (sideMove + 2 * singleObjectHeight + objectMove), width = 128, height = 128, anchor = 'nw')
        self.aboutAppWindow_text.place(x = int(sideMove + objectMove + 128), y = (sideMove + 2 * singleObjectHeight + objectMove), width = int(windowWidth - int(sideMove + objectMove + 128) - sideMove), height = int(windowHeight - 2 * sideMove - 2 * objectMove - 3 * singleObjectHeight), anchor = 'nw')
        self.aboutAppWindow_btnClose.place(x = int(windowWidth - sideMove), y = int(windowHeight - sideMove), height = singleObjectHeight, anchor = 'se')

        self.aboutAppWindow_text.config(wraplength = int(windowWidth - int(sideMove + objectMove + 128) - sideMove))

    def aboutApp(self, arg1 = None) :
        self.aboutAppGUI()
        #txt = self.loadCurrentLang(key = 'messageAbout', popEmptyLines = True)
        #superSecret1 = False #...?
        #superSecret2 = False
        #if time.strftime('%m%d') == '0401' and random.randint(301, 400) == 324 :
        #    superSecret1 = True
        #if time.strftime('%m%d') == '0528' :
        #    superSecret2 = True
        #if superSecret1 == True :
        #    txt = txt.split('\n')
        #    for x in range(len(txt)):
        #        txt[x] = '\u202e' + txt[x]
        #    txt.append('\n[!]Aha! April fool!:)')
        #    txt = '\n'.join(txt)
        #if superSecret2 == True :
        #    txt = txt.split('\n')
        #    txt.append('\n[\\n-n/ Happy birthday, P0000324!]')
        #    txt = '\n'.join(txt)
        #messagebox.showinfo(self.loadCurrentLang(key = 'messageTitleAbout'), txt)

    def doNothing(self):
        self.shellOutput('I did nothing!:D', toLog = False)

    def underConstruction(self, arg1 = None):
        messagebox.showinfo(self.loadCurrentLang(key = 'messageTitleUnderConstruction'), self.loadCurrentLang(key = 'messageUnderConstruction'))
