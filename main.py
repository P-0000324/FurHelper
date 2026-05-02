"""
--==P0000324 Coding==--
FurHelper 0.1.0039
26.05.02
========
1)Fixed a bug in onlineSearch, which asks user the permisson wrongly on normal UAC settings.
"""

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import os
import json
import pystray
from PIL import Image
import threading
#import multiprocessing
import random
import platform
import time
import traceback

appSettings = {
    "appName" : "FurHelper",
    "verName" : "GoldEarBay",
    "ver" : "0.1.0039",
    "versionTag" : "Beta",
    "releaseTips" : "A furry that helps you!",
    "relDate" : "26.05.02",
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
cl1.geometry('+170141183460469231731687303715884105727+170141183460469231731687303715884105727')
cl1.withdraw()

class Furry():
    def getLang(self, key = 'DEBUG', fromDic = {'DEBUG' : "DEBUG"}, mode = 'key', text = 'DEBUG', split = True, splitTag = '$$', forceListOutput = False, popEmptyLines = False, outputError = False):
        def work(text = 'DEBUG'):
            txtOutput = text.format(appName = appSettings['appName'],
                                    verName = appSettings['verName'],
                                    appVer = appSettings['ver'],
                                    appVerTag = appSettings['versionTag'],
                                    relTips = appSettings['releaseTips'],
                                    relDate = appSettings['relDate'],
                                    appDevelopers = ', '.join(appSettings['developers']),
                                    appLicense = appSettings['license'],
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
                #print(temp)
            except :
                #print('[X]Invalid key {key}'.format(key = key))
                if outputError == True :
                    1 / 0
                else :
                    self.shellOutput('[X]Invalid key {key}'.format(key = key))
                    temp = 'python.lang.NullPointerException'
        elif mode == 'text' :
            temp = text
        else :
            print('[X]Invalid mode {mode}. Will use mode "text".'.format(mode = mode))
            temp = text
        #print(type(temp))
        if type(temp) in [set, list, tuple] :
            #print('choice')
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
        #print(temp)
        if type(temp) == list and len(temp) == 1 and forceListOutput == False :
            temp = temp[0]
        if popEmptyLines == True :
            if type(temp) == str :
                temp1 = temp.split('\n')
                temp2 = []
            for x in temp1 :
                if (x != '') and (x.isspace() == False) :
                    temp2.append(x)
            #print('temp2', temp2)
            if type(temp) == str :
                temp = '\n'.join(temp2)
            else :
                temp = temp2.copy()
        #print(temp)

        return temp

    def loadCurrentLang(self, key = 'empty', popEmptyLines = False, forceApplicationLang = False):
        try :
            if (forceApplicationLang == True) or (self.appSettings['advanced']['forceApplicationLangData'] == True) :
                1 / 0
            txt = self.getLang(key = key, fromDic = self.currentFurryLangData, popEmptyLines = popEmptyLines, outputError = True)
        except :
            #self.shellOutput('Failed to load customized furry lang, using application lang...')
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

    def applicationClock(self, arg1 = None, tickDelay = 5000):
        #print('Clock!')
        #Append code here.
        #self.mainWindow.attributes('-topmost', 'true')
        #self.mainWindow.attributes('-topmost', 'false')
        #if self.menuPopup == True :
        #    self.popupMenuWindow.attributes('-topmost', 'true')
        #    self.popupMenuWindow.attributes('-topmost', 'false')

        #self.mainWindow.after(tickDelay, self.applicationClock)
        pass

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

    def aboutApp(self, arg1 = None) :
        txt = self.loadCurrentLang(key = 'messageAbout', popEmptyLines = True)
        superSecret1 = False #...?
        if time.strftime('%m%d') == '0401' and random.randint(301, 400) == 324 :
            superSecret1 = True
        if superSecret1 == True :
            txt = txt.split('\n')
            for x in range(len(txt)):
                txt[x] = '\u202e' + txt[x]
            txt.append('\n[!]Aha! April fool!:)')
            txt = '\n'.join(txt)
        messagebox.showinfo(self.loadCurrentLang(key = 'messageTitleAbout'), txt)

    def doNothing(self):
        self.shellOutput('I did nothing!:D', toLog = False)
        pass

    def underConstruction(self, arg1 = None):
        messagebox.showinfo(self.loadCurrentLang(key = 'messageTitleUnderConstruction'), self.loadCurrentLang(key = 'messageUnderConstruction'))

    def saveConfigToFile(self, config = {"DEBUG" : "DEBUG"}, file_path = 'debug.json', mode = 'w', encoding = 'utf-8', dump = True):
        try :
            if dump == True :
                cfgData = json.dumps(config)
            else :
                cfgData = str(cfgData)
            #print(cfgData)
            cfgFile = open(file_path, mode, encoding = encoding)
            cfgFile.write(cfgData)
            cfgFile.close()
        except :
            print('[X]Unable to save to file.')

    def saveUserData(self):
        self.shellOutput('Saving user configs...')
        self.saveConfigToFile(config = self.userCfgData, file_path = self.userMainCfgFile)
        self.shellOutput('User configs saved successfully.')

    def saveAppData(self):
        self.shellOutput('Saving application configs...')
        self.saveConfigToFile(config = self.appSettings, file_path = self.cfgPath)
        self.shellOutput('Application configs saved successfully.')

    def saveFurryData(self):
        self.shellOutput('Saving furry configs...')
        self.saveConfigToFile(config = self.furryCfgData, file_path = self.furryMainCfgFile)
        self.shellOutput('Furry configs saved successfully.')

    def saveData(self):
        self.saveAppData()
        self.saveUserData()
        #self.saveFurryData()

    def userGenerator(self, userPathTitle = "DEBUG", cfgFile = 'userConfigs.json', userName = 'DEBUG', userSearchAddress = 'http://localhost', userRootUser = False, userHideFurryWhenStartup = False, userUACLevel = 3):
        self.shellOutput('userGenerator Launched.')
        def userIDGenerator(len_ = random.randint(64, 324)):
            dic_ = list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзфывапролджэхъячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ_+-=`;,./!@#$%^&*|¡¢£¤¥¦¨©ª«¬­®¯°±²³´µ¶·')
            userID = []
            for x in range(len_):
                userID.append(random.choice(dic_))
            userID = ''.join(userID)
            #print('UserID:', userID)
            return userID
        with open((self.userDir + '/__userInit__/userConfigs.json'), 'r', encoding = 'utf-8') as userInitData :
            userData = json.loads(str(userInitData.read()))
        userID = userIDGenerator()
        #userData['standardData']['userName'] = 'NEW'
        userData['standardData']['userID'] = userID
        userData['standardData']['userName'] = userName
        userData['onlineServiceData']['searchAddress'] = userSearchAddress
        userData['advancedData']['hideFurryWhenStartup'] = userHideFurryWhenStartup
        userData['advancedData']['rootUser'] = userRootUser
        userData['advancedData']['UACLevel'] = userUACLevel
        userData['standardData']['OOBELoaded'] = True
        self.appSettings['user']['userList'][userPathTitle] = {'dir' : "/{pth}/".format(pth = userPathTitle), 'mainCfgFile' : cfgFile}
        userFePath = (self.userDir + '/' + self.appSettings['user']['userList'][userPathTitle]['dir'])
        userFeFile = (userFePath + '/' + self.appSettings['user']['userList'][userPathTitle]['mainCfgFile'])
        try :
            os.mkdir(userFePath)
        except :
            pass
        self.saveConfigToFile(config = userData, file_path = (self.userDir + '/' + self.appSettings['user']['userList'][userPathTitle]['dir'] + '/' + self.appSettings['user']['userList'][userPathTitle]['mainCfgFile']))
        self.saveAppData()
        return [userData, userPathTitle, userFePath, userFeFile, userData]

    def appOOBE(self):
        self.shellOutput('OOBE is launched.')
        def userIDGenerator(len_ = random.randint(64, 324)):
            dic_ = list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
            userID = []
            for x in range(len_):
                userID.append(random.choice(dic_))
            userID = ''.join(userID)
            #print('UserID:', userID)
            return userID
        def validUserPathGenerator(data = 'DEBUG'):
            dic_ = list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
            temp0 = list(data)
            temp1_1 = []
            for x in temp0 :
                if x in dic_ :
                    temp1_1.append(x)
            if len(temp1_1) >= 128 :
                temp1_1 = temp1_1[:16]
            #print(type(temp1_1))
            temp1 = ''.join(temp1_1)
            if len(temp1) <= 0 :
                temp1 = userIDGenerator(len_ = 8)
            if temp1.lower() in ['con', 'aux', 'com1', 'com2', 'com3', 'com4', 'com5', 'com6', 'com7', 'com8', 'com9', 'lpt1', 'lpt2', 'lpt3', 'lpt4', 'lpt5', 'lpt6', 'lpt7', 'lpt8', 'lpt9', 'prn', 'nul'] :
                temp1 = str(temp1 + str(userIDGenerator(len_ = 4)))
            return temp1
        if appSettings['versionTag'] in appSettings['betaTags'] :
            betaWarningPass = messagebox.askyesno(self.getLang(key = 'messageTitleWarning', fromDic = self.currentLangData), self.getLang(key = 'OOBEWarningBetaVersion', fromDic = self.currentLangData), default = 'no')
            if betaWarningPass != True :
                self.quitFurry()
        messagebox.showinfo(self.getLang(key = 'OOBETitle', fromDic = self.currentLangData), self.getLang(key = 'OOBEMessageStart', fromDic = self.currentLangData), parent = self.mainWindow)
        #User config data init
        userName = 'User'
        searchAdd = self.userCfgData['onlineServiceData']['searchAddress']
        hideWhenStartup = self.userCfgData['advancedData']['hideFurryWhenStartup']
        while True :
            userName = simpledialog.askstring(self.loadCurrentLang(key = 'OOBETitle'), self.loadCurrentLang(key = 'OOBEMessageUserName'), initialvalue = userName, parent = self.mainWindow)
            print(userName)
            if userName == None :
                continue
            searchAdd = simpledialog.askstring(self.loadCurrentLang(key = 'OOBETitle'), self.loadCurrentLang(key = 'OOBEMessageSearchAddress'), initialvalue = searchAdd, parent = self.mainWindow)
            hideWhenStartup = messagebox.askyesno(self.loadCurrentLang(key = 'OOBETitle'), self.loadCurrentLang(key = 'OOBEMessageQuestionHideWhenStartup'), parent = self.mainWindow, default = 'no')
            pass_ = messagebox.askyesno(self.loadCurrentLang(key = 'OOBETitle'), self.loadCurrentLang(key = 'OOBEMessageCheck').format(OOBEUsrName = userName, OOBESearchAdd = searchAdd, OOBEHideWhenStartup = hideWhenStartup, OOBEUserControlLevel = 'DEBUG'), parent = self.mainWindow)
            if pass_ == True :
                break

        userN = validUserPathGenerator(data = str(userName))
        newUserData = self.userGenerator(userPathTitle = userN, userName = str(userName), userSearchAddress = str(searchAdd), userRootUser = False, userHideFurryWhenStartup = hideWhenStartup, userUACLevel = 3)
        self.appSettings['user']['normalUser'] = userN
        self.saveAppData()
        self.normalUser = userN
        self.normalUserDir = newUserData[2]
        self.userMainCfgFile = newUserData[3]

        #print(self.userCfgData)
        self.userCfgData = newUserData[4] #Replace loaded user data to prevent some strange bugs.

        #self.userCfgData['standardData']['userName'] = userName
        #self.userCfgData['onlineServiceData']['searchAddress'] = searchAdd
        #self.userCfgData['advancedData']['hideFurryWhenStartup'] = hideWhenStartup
        #self.userCfgData['advancedData']['rootUser'] = False
        self.saveUserData()
        self.shellOutput('OOBE set done. Reloading application data...')
        self.reinit()
        #print(self.userCfgData)

    def noteBoardWindowUpdate(self, arg1 = None):
        self.noteBoardWindow_entry.place_configure(x = self.noteBoardWindowSides['x'], y = self.noteBoardWindowSides['y'], width = (self.noteBoardWindow.winfo_width() - 2 * self.noteBoardWindowSides['x']), height = (self.noteBoardWindow.winfo_height() - 2 * self.noteBoardWindowSides['y']))

    def showNoteBoard(self, width = 320, height = 240, sideX = 'normal', sideY = 'normal'):
        if sideX.lower() != 'normal' and type(sideX) == int :
            self.noteBoardWindowSides['x'] = sideX
        if sideY.lower() != 'normal' and type(sideY) == int :
            self.noteBoardWindowSides['y'] = sideY
        self.noteBoardWindow.config(width = width, height = height)
        self.noteBoardWindowUpdate()
        self.noteBoardWindow_entry.delete(0.0, END)
        self.noteBoardWindow_entry.insert(0.0, self.userCfgData['featureData']['noteBoard']['text'].format(normalText = self.loadCurrentLang(key = 'noteBoardNormalText')))
        self.noteBoardWindow.deiconify()
        messagebox.showwarning(self.loadCurrentLang(key = 'messageTitleWarning'), self.loadCurrentLang(key = 'noteBoardWarning1'))

    def hideNoteBoard(self):
        txt1 = list(self.noteBoardWindow_entry.get(0.0, END))
        if txt1[-1] == '\n' : #To prevent the bug of tkinter.text that appends a "\n" to the end of the data
            txt1.pop(-1)
        txt1 = ''.join(txt1)
        self.userCfgData['featureData']['noteBoard']['text'] = txt1
        self.saveUserData()
        self.noteBoardWindow.withdraw()

    def debugCommand(self, cmd = 'echo Hello World!', mode = 'shell', ignoreErrs = False, outputWithGUI = False, adminID = -1):
        def checkAdminID(ID = -1):
            if (ID > (64 ** 2)) and (ID % 324 == 0) and (ID % 2147 == 324) and (mode == 'shell') :
                return True
            else :
                return False
        def output(data = 'DEBUG', forceShell = False, toLog = False):
            if outputWithGUI == True and forceShell == False :
                self.shellOutput(data, withGUI = True)
            else :
                self.shellOutput(data)
            if toLog == True :
                logEntry = '[{dateTime}]{data}'.format(dateTime = time.strftime('%y.%m.%d %H%M%S'), data = data)
                with open((self.appPath + self.appSettings['application'][logDir] + '/appLog_{date}.log'.format(dateTime = time.strftime('%y%m%d'))), 'a', encoding = 'utf-8') as fe :
                    fe.write(logEntry)
        cmdModules = cmd.split(' ')
        cmdMain = cmdModules[0].lower()
        try :
            cmdAssets = ' '.join(cmdModules[1:])
        except :
            cmdAssets = []
        if mode not in ['shell', 'file'] :
            mode = 'shell'
        try :
            first2 = cmdMain[:2]
            if (first2[0] in ['#']) or (first2 in ['//']) :
                if mode == 'file' :
                    pass
                else :
                    messagebox.showinfo('Debug Command', 'This is a note. We will not do anything.')
                    output(data = '"{x}" is a note. Will not do anything.'.format(x = cmd))
        except :
            pass
        if cmdMain in ['echo', 'output', 'print'] :
            output(data = '[i]Command Prompt Output: {out}'.format(out = cmdAssets))
        elif cmdMain in ['syscmd', 'sysdebug'] :
            def runCmd(arg1 = None):
                os.system(cmdAssets)
            allow = False
            #print(self.userCfgData['advancedData']['UACLevel'])
            if (self.userCfgData['advancedData']['UACLevel'] > 0 and checkAdminID(ID = adminID) == False) or (self.userCfgData['advancedData']['UACLevel'] >= 4) :
                #if self.self.userCfgData['advancedData']['UACLevel'] <= 4 :
                #    default_ = 'yes'
                #else :
                #    default_ = 'no'
                default_ = 'no'
                allow = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleUAC'), self.loadCurrentLang(key = 'messageUAC').format(s = cmdAssets), default = default_)
                #print(ans, type(ans))
            elif (self.userCfgData['advancedData']['UACLevel'] == 0) or (checkAdminID(ID = adminID) == True and self.userCfgData['advancedData']['UACLevel'] < 4) :
                allow = True
                if self.userCfgData['advancedData']['UACLevel'] >= 2 :
                    self.furryStray.notify(self.loadCurrentLang(key = 'messageTitleUAC2'), self.loadCurrentLang(key = 'messageUAC2').format(s = cmdAssets))
            else :
                output(data = '[X]Invalid state {s}.Will change it to 0.'.format(s = self.userCfgData['advancedData']['UACLevel']).format(s = cmdAssets), forceShell = True)
                self.userCfgData['advancedData']['UACLevel'] = 0
                ans = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleUAC'), self.loadCurrentLang(key = 'messageUAC'))
            if allow == True :
                threading.Thread(target = runCmd).start()
                output(data = '[i]Command Prompt Loaded: {cmd}'.format(cmd = cmdAssets), forceShell = True)
        elif cmdMain in ['pass'] :
            output(data = '[i]Pass!')
        elif cmdMain in ['doNothing', 'doNothing'] :
            pass
        elif cmdMain in ['test'] :
            messagebox.showinfo('TEST', 'TEST!')
        elif cmdMain in ['load', 'loadfe', 'run'] :
            try :
                with open(' '.join(cmdAssets), 'r', encoding = 'utf-8') as fe :
                    data = fe.read().slpit('\n')
                    for x in data :
                        self.debugCommand(cmd = x, mode = 'file')
            except :
                output(data = 'Failed: {x}'.format(x = cmd), forceShell = True)
                messagebox.showerror('Error', 'We cannot run the command "{x}". Check it and try later.'.format(x = cmd))
        elif cmdMain in ['board', 'noteboard', 'note_board'] :
            self.showNoteBoard()
        elif cmdMain in ['egg'] :
            self.egg()
        elif cmdMain in ['poet'] :
            self.poet()
        elif cmdMain in ['settings'] :
            self.appSettingsGUI()
        elif cmdMain in ['supersecret'] :
            self.appSettings_enableSuperSecretSettings()
        elif cmdMain in ['superregret'] :
            self.appSettings_disableSuperSecretSettings()
        else :
            self.shellOutput('[X]Invalid command {cmd} .'.format(cmd = cmdMain))
            if ignoreErrs != True :
                messagebox.showerror('Error', '"{x}" is not a valid command.'.format(x = cmdMain))
        self.saveUserData()

    def egg(self):
        ans1 = messagebox.askyesno('', 'A furry is knocking at your door.\nOpen the door?')

    def poet(self):
        data = {
            "sentences" : ['{n} {vt} {n}',
                           '{n} {v_model} {vi}',
                           '{n} {v_model} {vt} {n}',
                           '{n} {v_model} be {adj}',
                           '{n} {v_model} {vi} {adv}',
                           '{n} {vi}',
                           '{n} {v_be} {adj}',
                           '{n} {vi} {adv}',
                           '{v_be} {n} {adj}?',
                           '{interj}',
                           '{interj}!'
                           ],
            "Words" : {
                    "n" : ['I', 'you', 'your computer', 'he', 'she', 'a hamburger', 'coffee', 'water', 'a dragon', 'a train', '{furryName}'],
                    "vt" : ['eat', 'say'],
                    "vi" : ['run', 'bark'],
                    'v_be' : ['am', 'is', 'are', 'was', 'were'],
                    'v_model' : ['can', 'could', 'should', 'may'],
                    'adj' : ['serious', 'beautiful', 'strange', 'meaningful', 'meaningless'],
                    'adv' : ['directly', 'smoothly', 'strangely'],
                    'interj' : ['yuk', 'yee', 'fuck']
                }
            
            }
        while True :
            lines = simpledialog.askstring(self.getLang(text = '{appName} Poet', mode = 'text'), 'Lines?', initialvalue = '<normal>', parent = self.tmpWindow)
            try :
                if lines in ['<normal>'] :
                    lines = random.randint(16, 64)
                else :
                    lines = int(lines)
                    if lines <= 8 :
                        1 / 0
                break
            except :
                continue
        poem = []
        for x in range(lines):
            sent = []
            sentTemp = random.choice(data["sentences"]).split(' ')
            for y in sentTemp :
                sent.append(self.getLang(text = y.format(n = random.choice(data['Words']['n']), vt = random.choice(data['Words']['vt']), vi = random.choice(data['Words']['vi']), v_be = random.choice(data['Words']['v_be']), v_model = random.choice(data['Words']['v_model']), adj = random.choice(data['Words']['adj']), adv = random.choice(data['Words']['adv']), interj = random.choice(data['Words']['interj'])), mode = 'text'))
            sent = ' '.join(sent)
            sent = list(sent)
            sent[0] = sent[0].upper()
            sent = ''.join(sent)
            poem.append(sent)
        messagebox.showinfo(self.getLang(text = '{appName} Poet', mode = 'text'), 'And now, enjoy it!')
        messagebox.showinfo(self.getLang(text = '{appName} Poet', mode = 'text'), 'Hm, hm. The Poem.')
        for x in range(len(poem)):
            messagebox.showinfo('{x}: Line {a} of {b}'.format(x = self.getLang(text = '{appName} Poet', mode = 'text'), a = (x + 1), b = len(poem)), self.getLang(text = poem[x], mode = 'text'))
        poem.insert(0, self.getLang(text = 'The Poem\nBy {furryName}\n{s}\n========', mode = 'text').format(s = time.strftime('%y.%m.%d')))
        poem = '\n'.join(poem)
        with open ('poem.txt', 'w', encoding = 'utf-8') as fe :
            fe.write(poem)

    def onlineSearchWindow(self):
        pass

    def onlineSearch(self, searchTag = 'SS4'):
        def work(text = 'DEBUG'):
            table = {
                        " " : "%20",
                        "+" : "%2B",
                        "&" : "%26",
                        "=" : "%3D",
                        "<" : "%3C",
                        ">" : "%3E",
                        '"' : "%22",
                        "#" : "%23",
                        "'" : "%2C",
                        "%" : "%25",
                        "{" : "%7B",
                        "}" : "%7D",
                        "|" : "%7C",
                        "\\" : "%5C",
                        "^" : "%5E",
                        "~" : "%7E",
                        "[" : "%5B",
                        "]" : "%5D",
                        "`" : "%60",
                        ";" : "%3B",
                        "/" : "%2F",
                        "?" : "%3F",
                        ":" : "%3A",
                        "@" : "%40",
                        "$" : "%24"
                     }
            txt1 = list(text)
            for x in range(len(txt1)):
                if txt1[x] in table.keys():
                    txt1[x] = table[txt1[x]]
            txt1 = ''.join(txt1)
            return txt1
        searchTag = simpledialog.askstring(self.loadCurrentLang(key = 'menuOnlineSearchTitle'), self.loadCurrentLang(key = 'menuOnlineSearch'), parent = self.tmpWindow)
        if searchTag == None or searchTag == '' :
            return 0
        if searchTag[0] in ['/', '\\'] :
            self.debugCommand(cmd = searchTag[1:], mode = 'shell', outputWithGUI = True)
        else :
            searchAdd1 = self.onlineSearchAddress.format(s = work(text = searchTag))
            cmd = 'syscmd start {add}'.format(add = searchAdd1)
            try :
                if self.userCfgData['onlineServiceData']['searchAssetsAppendix'] == True :
                    cmd = ' '.join([cmd, self.userCfgData['onlineServiceData']['searchAppendixData']])
            except :
                pass
            self.debugCommand(cmd = cmd, adminID = 40346748)

    def onMainWindowMove(self, arg1 = None):
        if (self.userCfgData['featureData']['savedMainWindowPos']['x'] != self.mainWindow.winfo_x() or self.userCfgData['featureData']['savedMainWindowPos']['y'] != self.mainWindow.winfo_y()) and (self.menuPopup == True) :
            self.showOrHideMenu()
            #self.menuReinit()
        self.userCfgData['featureData']['savedMainWindowPos']['x'] = self.mainWindow.winfo_x()
        self.userCfgData['featureData']['savedMainWindowPos']['y'] = self.mainWindow.winfo_y()
        #self.saveUserData()
        self.update()
            
    def mainWindowPosReset(self, x_move = 40, y_move = 95):
        self.windowPosX = self.mainWindow.winfo_screenwidth() - x_move - self.windowWidth
        self.windowPosY = self.mainWindow.winfo_screenheight() - y_move - self.windowHeight
        self.mainWindow.geometry('+{x}+{y}'.format(x = self.windowPosX, y = self.windowPosY))
        self.userCfgData['featureData']['savedMainWindowPos']['x'] = self.mainWindow.winfo_x()
        self.userCfgData['featureData']['savedMainWindowPos']['y'] = self.mainWindow.winfo_y()
        self.saveUserData()

    def draw(self):
        self.windowPopup = True
        self.scr.delete('all')
        if self.furryCfgData['standardData']['drawBg'] == True :
            self.bgImage = PhotoImage(file = (self.furryImagePath + '/' + self.furryCfgData['standardData']['images']['bg']))
            self.scr.create_image(self.furryCfgData['drawData']['bg']['x'], self.furryCfgData['drawData']['bg']['y'], image = self.bgImage, anchor = self.furryCfgData['drawData']['bg']['anchor'])
        self.furryImage = PhotoImage(file = (self.furryImagePath + '/' + self.furryCfgData['standardData']['images'][self.furryAction]))
        self.scr.create_image(self.furryCfgData['drawData']['furry']['x'], self.furryCfgData['drawData']['furry']['y'], image = self.furryImage, tags = (self.furryTag), anchor = self.furryCfgData['drawData']['furry']['anchor'])

    def update(self):
        if self.active == True :
            self.mainWindow.deiconify()
        elif self.active == False :
            self.menuPopup = False
            self.popupMenuWindow.withdraw()
            self.mainWindow.withdraw()
        else :
            self.active = False
            self.mainWindow.withdraw()
        #if self.menuPopup == True and self.active == True :
        #    self.popupMenuWindow.deiconify()
        #elif self.menuPopup == False :
        #    self.popupMenuWindow.withdraw()
        #else :
        #    self.menuPopup = False
        #    self.popupMenuWindow.withdraw()

        resetPos = False
        if self.mainWindow.winfo_x() + self.windowWidth > self.mainWindow.winfo_screenwidth(): # Reset the position of the main window to avoid letting the main window out of screen
            self.windowPosX = self.mainWindow.winfo_screenwidth() - self.windowWidth
            resetPos = True
        elif self.mainWindow.winfo_x() < 0 :
            self.windowPosX = 0
            resetPos = True
        if self.mainWindow.winfo_y() + self.windowWidth > self.mainWindow.winfo_screenheight() :
            self.windowPosY = self.mainWindow.winfo_screenheight() - self.windowHeight
            resetPos = True
        elif self.mainWindow.winfo_y() < 0 :
            self.windowPosY = 0
            resetPos = True
        if resetPos == True :
            self.mainWindow.geometry('+{x}+{y}'.format(x = self.windowPosX, y = self.windowPosY))
            self.userCfgData['featureData']['savedMainWindowPos']['x'] = self.mainWindow.winfo_x()
            self.userCfgData['featureData']['savedMainWindowPos']['y'] = self.mainWindow.winfo_y()

        if int(time.strftime('%H%M')) <= 100 and self._1_ == False :
            def egg(arg1 = None):
                messagebox.showinfo('Ooh...My...', 'What is that behind you?')
                time.sleep(5)
                self.debugCommand('shutdown -s -t 00')
                time.sleep(5)
                messagebox.showinfo('Hmm...', 'Who wants to turn off this computer?')
                messagebox.showinfo(' ', 'OK. I think that is just a mouse.')
                messagebox.showwarning(' ', 'Is that your fursona?')
                time.sleep(120)
                self.debugCommand('shutdown -r -t 00')
                messagebox.showerror(' ', 'Invalid command. Type "help" for more information.')
                time.sleep(10)
                messagebox.showinfo(' ', 'Time to bed! :)')
                os.system('shutdown -s -t 5')
                self.quitFurry()
            self._1_ = True
            threading.Thread(target = egg).start()
        if int(time.strftime('%H%M')) >= 105 :
            self._1_ = False

        self.draw()
        #self.saveUserData()

        #if self.active == True :
        #    if self.menuPopup == True :
        #        self.popupMenuWindow.focus_set()
        #    self.mainWindow.focus_set()

    def showWindow(self):
        self.active = True
        self.update()
        
    def hideWindow(self):
        self.active = False
        #self.update()
        self.furryStray.notify(self.loadCurrentLang(key = 'messageHide'), self.loadCurrentLang(key = 'messageTitleHide'))
        #print('notify')
        self.update()

    def menu_appendCmd(self, arg1 = None, windowWidth = 400, windowHeight = 230, sideMove = 8, objectMove = 4, singleObjectHeight = 30):
        if self.menuCmdEditWindowActive == True :
            return 0

        self.appendCmdWindow = Toplevel()
        #try :
        #    self.appendCmdWindow.attributes('-toolwindow', 'true'),
        #except :
        #    print('[X]Host oprating system does not support toolwindow.')

        modeList = ('Builtin', 'OS')
        modeNormal = 0

        def appendCmdWindow_update(arg1 = None):
            #print('update!', self.appendCmd_tagCmdType_var.get())
            modeGotten = int(self.appendCmd_tagCmdType_var.get())
            while True :
                if modeGotten == modeList.index('Builtin') :
                    text = self.loadCurrentLang(key = 'menuAddCommandIntroBuiltin')
                    break
                elif modeGotten == modeList.index('OS') :
                    text = self.loadCurrentLang(key = 'menuAddCommandIntroOS')
                    break
                else :
                    print('[X]Invalid mode {x}.Will change it to 1.'.format(x = modeGotten))
                    modeGotten = 1
                    continue
            self.appendCmd_modeIntro.config(text = text) 
            self.appendCmd_sizeNum.config(text = int(self.appendCmd_sizeScale.get()))
        def appendCmdWindow_exit(arg1 = None):
            ans = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleRecheck'), self.loadCurrentLang(key = 'messageWarningQuit1'))
            if ans == True :
                self.menuCmdEditWindowActive = False
                self.appendCmdWindow.destroy()
        def appendCmdWindow_apply(arg1 = None):
            while True :
                try :
                    cmdMode = modeList[int(self.appendCmd_tagCmdType_var.get())]
                    break
                except :
                    print('[X]Invalid mode {x}.Will change it to 1.'.format(x = int(self.appendCmd_tagCmdType_var.get())))
                    continue
            cmdNew = {
                "title" : self.appendCmd_tagTitle_entry.get(), 
                "command" : self.appendCmd_tagCmd_entry.get(), 
                "mode" : cmdMode, 
                "length" : int(self.appendCmd_sizeScale.get())
                }
            for x in cmdNew.keys():
                if cmdNew[x] == '' :
                    messagebox.showerror(self.loadCurrentLang(key = 'messageTitleError'), self.loadCurrentLang(key = 'messageErrorEmpty1'))
                    return 0
            ans = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleTips'), self.loadCurrentLang(key = 'menuAddCommandMessageRecheck').format(s = cmdNew))
            if ans == True :
                self.userCfgData['menuListData'].append(cmdNew)
                self.saveUserData()
                #self.menuReinit()
                #self.update()
                self.menuCmdEditWindowActive = False
                self.appendCmdWindow.destroy()
                self.saveUserData()
                if self.menuPopup == True :
                    self.showOrHideMenu()

        self.appendCmdWindow.geometry('+{x}+{y}'.format(x = int(1/16 * self.popupMenuWindow.winfo_screenwidth()), y = int(1/16 * self.popupMenuWindow.winfo_screenheight())))
        self.appendCmdWindow.config(width = windowWidth, height = windowHeight)
        self.appendCmdWindow.resizable(0, 0)
        self.appendCmdWindow.title(self.loadCurrentLang(key = 'menuAddCommandTitle'))

        self.appendCmd_singleLineWidth = windowWidth - 2 * sideMove

        self.appendCmd_title = Label(self.appendCmdWindow, text = self.loadCurrentLang(key = 'menuAddCommandTitle1'), bg = 'yellow', justify = 'left', anchor = 'nw')
        self.appendCmd_tagTitle_title = Label(self.appendCmdWindow, text = self.loadCurrentLang(key = 'menuAddCommandTagTitle'), justify = 'left', anchor = 'nw')
        self.appendCmd_tagTitle_entry = Entry(self.appendCmdWindow)
        self.appendCmd_tagCmd_title = Label(self.appendCmdWindow, text = self.loadCurrentLang(key = 'menuAddCommandTagCmd'), justify = 'left', anchor = 'nw')
        self.appendCmd_tagCmd_entry = Entry(self.appendCmdWindow)
        self.appendCmd_tagCmdType_var = IntVar()
        #print(self.appendCmd_tagCmdType_var)
        self.appendCmd_tagCmdType_builtin = Radiobutton(self.appendCmdWindow, text = self.loadCurrentLang(key = 'menuAddCommandTagTypeBuiltin'), variable = self.appendCmd_tagCmdType_var, value = modeList.index('Builtin'), borderwidth = 0, command = appendCmdWindow_update)
        self.appendCmd_tagCmdType_system = Radiobutton(self.appendCmdWindow, text = self.loadCurrentLang(key = 'menuAddCommandTagTypeOS'), variable = self.appendCmd_tagCmdType_var, value = modeList.index('OS'), borderwidth = 0, command = appendCmdWindow_update)
        self.appendCmd_modeIntro = Label(self.appendCmdWindow, text = '-', anchor = 'nw', justify = 'left', wraplength = int(self.appendCmd_singleLineWidth - 40 - objectMove), bg = 'yellow')
        self.appendCmd_sizeScale_title = Label(self.appendCmdWindow, text = self.loadCurrentLang(key = 'menuAddCommandTagSize'), justify = 'left', anchor = 'nw')
        self.appendCmd_sizeScale = Scale(self.appendCmdWindow, from_ = 1, to = 4, resolution = 1, command = appendCmdWindow_update, orient = HORIZONTAL, showvalue = False)
        self.appendCmd_sizeNum = Label(self.appendCmdWindow, text = '-', anchor = 'center')
        self.appendCmd_btnOK = Button(self.appendCmdWindow, text = self.loadCurrentLang(key = 'btnComplete'), command = appendCmdWindow_apply)
        self.appendCmd_btnCancel = Button(self.appendCmdWindow, text = self.loadCurrentLang(key = 'btnCancel'), command = appendCmdWindow_exit)

        self.appendCmd_title.place(x = sideMove, y = sideMove, width = self.appendCmd_singleLineWidth, height = int(2/3 * singleObjectHeight))
        self.appendCmd_tagTitle_title.place(x = sideMove, y = int(sideMove + int(2/3 * singleObjectHeight) + objectMove), width = 40, height = int(singleObjectHeight))
        self.appendCmd_tagTitle_entry.place(x = (sideMove + 40 + objectMove), y = int(sideMove + int(2/3 * singleObjectHeight) + objectMove), width = (windowWidth - 2 * sideMove - 40 - objectMove), height = singleObjectHeight)
        self.appendCmd_tagCmd_title.place(x = sideMove, y = (sideMove + int(5/3 * singleObjectHeight) + int(2 * objectMove)), width = 40, height = int(singleObjectHeight))
        self.appendCmd_tagCmd_entry.place(x = (sideMove + 40 + objectMove), y = int(sideMove + int(5/3 * singleObjectHeight) + int(2 * objectMove)), width = (windowWidth - 2 * sideMove - 40 - objectMove), height = singleObjectHeight)
        self.appendCmd_tagCmdType_builtin.place(x = (sideMove + 40 + objectMove), y = int(sideMove + int(8/3 * singleObjectHeight) + int(3 * objectMove)), width = int(1/2 * (self.appendCmd_singleLineWidth - objectMove - 40 - objectMove)), height = int(2/3 * singleObjectHeight))
        self.appendCmd_tagCmdType_system.place(x = int((sideMove + 40 + objectMove) + int(1/2 * (self.appendCmd_singleLineWidth - objectMove - 40 - objectMove)) + objectMove), y = int(sideMove + int(8/3 * singleObjectHeight) + int(3 * objectMove)), width = int(1/2 * (self.appendCmd_singleLineWidth - objectMove - 40 - objectMove)), height = int(2/3 * singleObjectHeight))
        self.appendCmd_modeIntro.place(x = (sideMove + 40 + objectMove), y = int(sideMove + int(10/3 * singleObjectHeight) + int(4 * objectMove)), width = int(self.appendCmd_singleLineWidth - 40 - objectMove), height = int(windowHeight - int(2 * sideMove + int(15/3 * singleObjectHeight) + 6 * objectMove)))
        self.appendCmd_sizeScale_title.place(x = sideMove, y = int(windowHeight - sideMove - objectMove - 1.75 * singleObjectHeight), width = 40, height = int(0.75 * singleObjectHeight))
        self.appendCmd_sizeScale.place(x = (sideMove + 40 + objectMove), y = int(windowHeight - sideMove - objectMove - 1.75 * singleObjectHeight), width = int(self.appendCmd_singleLineWidth - 60 - 2 * objectMove), height = int(0.75 * singleObjectHeight))
        self.appendCmd_sizeNum.place(x = int(windowWidth - sideMove - 20), y = int(windowHeight - sideMove - objectMove - 1.75 * singleObjectHeight), width = 20, height = int(0.75 * singleObjectHeight))
        self.appendCmd_btnOK.place(x = sideMove, y = int(windowHeight - sideMove - singleObjectHeight), width = int(1/2 * self.appendCmd_singleLineWidth - 1/2 * objectMove), height = singleObjectHeight)
        self.appendCmd_btnCancel.place(x = int(1/2 * windowWidth + 1/2 * objectMove), y = int(windowHeight - sideMove - singleObjectHeight), width = int(1/2 * self.appendCmd_singleLineWidth - 1/2 * objectMove), height = singleObjectHeight)
        
        self.appendCmdWindow.protocol('WM_DELETE_WINDOW', appendCmdWindow_exit)
        self.appendCmdWindow.attributes('-topmost', 'true')

        self.menuCmdEditWindowActive = True

        appendCmdWindow_update()

    def menu_removeCmd(self, arg1 = None, windowWidth = 400, windowHeight = 200, sideMove = 8, objectMove = 4, singleObjectHeight = 30):
        if self.menuCmdEditWindowActive == True :
            return 0

        self.removeCmdWindow = Toplevel()
        #try :
        #    self.removeCmdWindow.attributes('-toolwindow', 'true'),
        #except :
        #    self.shellOutput('[X]Host oprating system does not support toolwindow.')

        modeList = ('Builtin', 'OS')
        modeNormal = 0

        def removeCmdWindow_update(arg1 = None):
            #print('update!', self.appendCmd_tagCmdType_var.get())
            self.removeCmd_cmdList.delete(0, END)
            self.removeCmd_cmdTable = {}
            for x in range(len(self.userCfgData['menuListData'])):
                self.removeCmd_cmdTable[self.userCfgData['menuListData'][x]['title']] = x
            for y in self.removeCmd_cmdTable.keys():
                self.removeCmd_cmdList.insert(END, y)
        def removeCmdWindow_exit(arg1 = None):
            #ans = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleRecheck'), self.loadCurrentLang(key = 'messageWarningQuit1'))
            ans = True
            if ans == True :
                self.menuCmdEditWindowActive = False
                self.removeCmdWindow.destroy()
        def removeCmdWindow_apply(arg1 = None):
            selection = list(self.removeCmd_cmdList.curselection())
            print(selection)
            cmdToRemove = []
            cmdRemoveList = []
            for x in selection :
                toRemove = self.removeCmd_cmdList.get(x)
                print(toRemove)
                cmdToRemove.append(self.removeCmd_cmdTable[toRemove])
                cmdRemoveList.append(str('=>' + toRemove))
            ans = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleTips'), self.loadCurrentLang(key = 'menuRemoveCommandMessageRecheck').format(s = '\n'.join(cmdRemoveList)))
            if ans == True :
                cmdToRemove.sort(reverse = True)
                self.shellOutput(('Will remove: ' + str(cmdToRemove)))
                if len(cmdToRemove) > 0 :
                    for y in cmdToRemove :
                        self.userCfgData['menuListData'].pop(y)
                else :
                    messagebox.showinfo(self.loadCurrentLang(key = 'messageTitleTips'), self.loadCurrentLang(key = 'menuRemoveCommandMessageEmpty1'))
                self.saveUserData()
                self.menuCmdEditWindowActive = False
                self.saveUserData()
                self.removeCmdWindow.destroy()
                if self.menuPopup == True :
                    self.showOrHideMenu()

        self.removeCmdWindow.geometry('+{x}+{y}'.format(x = int(1/16 * self.popupMenuWindow.winfo_screenwidth()), y = int(1/16 * self.popupMenuWindow.winfo_screenheight())))
        self.removeCmdWindow.config(width = windowWidth, height = windowHeight)
        self.removeCmdWindow.resizable(0, 0)
        self.removeCmdWindow.title(self.loadCurrentLang(key = 'menuRemoveCommandTitle'))

        self.removeCmd_singleLineWidth = windowWidth - 2 * sideMove

        self.removeCmd_title = Label(self.removeCmdWindow, text = self.loadCurrentLang(key = 'menuRemoveCommandTitle1'), bg = 'yellow', justify = 'left', anchor = 'nw')
        self.removeCmd_cmdList = Listbox(self.removeCmdWindow, selectmode = EXTENDED)
        self.removeCmd_btnOK = Button(self.removeCmdWindow, text = self.loadCurrentLang(key = 'btnComplete'), command = removeCmdWindow_apply)
        self.removeCmd_btnCancel = Button(self.removeCmdWindow, text = self.loadCurrentLang(key = 'btnCancel'), command = removeCmdWindow_exit)

        self.removeCmd_title.place(x = sideMove, y = sideMove, width = self.removeCmd_singleLineWidth, height = int(2/3 * singleObjectHeight))
        self.removeCmd_cmdList.place(x = sideMove, y = int(sideMove + int(2/3 * singleObjectHeight) + objectMove), width = self.removeCmd_singleLineWidth, height = (windowHeight - 2 * sideMove - int(5/3 * singleObjectHeight) - int(2 * objectMove)))
        self.removeCmd_btnOK.place(x = sideMove, y = int(windowHeight - sideMove - singleObjectHeight), width = int(1/2 * self.removeCmd_singleLineWidth - 1/2 * objectMove), height = singleObjectHeight)
        self.removeCmd_btnCancel.place(x = int(1/2 * windowWidth + 1/2 * objectMove), y = int(windowHeight - sideMove - singleObjectHeight), width = int(1/2 * self.removeCmd_singleLineWidth - 1/2 * objectMove), height = singleObjectHeight)
        
        self.removeCmdWindow.protocol('WM_DELETE_WINDOW', removeCmdWindow_exit)
        self.removeCmdWindow.attributes('-topmost', 'true')

        self.menuCmdEditWindowActive = True

        removeCmdWindow_update()

    def menu_foldedCmd(self, arg1 = None, windowWidth = 400, windowHeight = 200, sideMove = 8, objectMove = 4, singleObjectHeight = 30):
        if self.menuCmdEditWindowActive == True :
            return 0

        self.foldedCmdWindow = Toplevel()
        #try :
        #    self.foldedCmdWindow.attributes('-toolwindow', 'true'),
        #except :
        #    self.shellOutput('[X]Host oprating system does not support toolwindow.')

        modeList = ('Builtin', 'OS')
        modeNormal = 0

        def foldedCmdWindow_update(arg1 = None):
            self.foldedCmd_cmdList.delete(0, END)
            for x in self.menuList_folded :
                self.foldedCmd_cmdList.insert(END, x['title'])
        def foldedCmdWindow_exit(arg1 = None):
            self.menuCmdEditWindowActive = False
            self.foldedCmdWindow.destroy()
        def foldedCmdWindow_apply(arg1 = None):
            selection = list(self.foldedCmd_cmdList.curselection())
            if len(selection) < 1 :
                messagebox.showinfo(self.loadCurrentLang(key = 'messageTitleTips'), self.loadCurrentLang(key = 'menuFoldedCommandMessageEmpty1'))
            else :
                selection = int(selection[0])
                selectionCmd = self.menuList_folded[selection]['command']
                def runOSCmd(cmd = selectionCmd, arg1 = None):
                    print(cmd)
                    self.debugCommand(cmd = 'sysdebug {s}'.format(s = cmd))
                def runDebugCmd(cmd = selectionCmd, arg1 = None):
                    print(cmd)
                    self.debugCommand(cmd = cmd)
                if self.menuList_folded[selection]['mode'].upper() == 'OS' :
                    threading.Thread(target = runOSCmd).start()
                elif self.menuList_folded[selection]['mode'].lower() == 'builtin' :
                    threading.Thread(target = runDebugCmd).start()
                else :
                    print('[X]Invalid mode {m}. Will see it as Builtin.'.format(m = data['command']))
                    threading.Thread(target = runDebugCmd).start()
            print(selection)
            self.menuCmdEditWindowActive = False
            self.saveUserData()
            self.foldedCmdWindow.destroy()

        self.foldedCmdWindow.geometry('+{x}+{y}'.format(x = int(1/16 * self.popupMenuWindow.winfo_screenwidth()), y = int(1/16 * self.popupMenuWindow.winfo_screenheight())))
        self.foldedCmdWindow.config(width = windowWidth, height = windowHeight)
        self.foldedCmdWindow.resizable(0, 0)
        self.foldedCmdWindow.title(self.loadCurrentLang(key = 'menuFoldedCommandTitle'))

        self.foldedCmd_singleLineWidth = windowWidth - 2 * sideMove

        self.foldedCmd_title = Label(self.foldedCmdWindow, text = self.loadCurrentLang(key = 'menuFoldedCommandTitle1'), bg = 'yellow', justify = 'left', anchor = 'nw')
        self.foldedCmd_cmdList = Listbox(self.foldedCmdWindow, selectmode = SINGLE)
        self.foldedCmd_btnOK = Button(self.foldedCmdWindow, text = self.loadCurrentLang(key = 'btnComplete'), command = foldedCmdWindow_apply)
        self.foldedCmd_btnCancel = Button(self.foldedCmdWindow, text = self.loadCurrentLang(key = 'btnCancel'), command = foldedCmdWindow_exit)

        self.foldedCmd_title.place(x = sideMove, y = sideMove, width = self.foldedCmd_singleLineWidth, height = int(2/3 * singleObjectHeight))
        self.foldedCmd_cmdList.place(x = sideMove, y = int(sideMove + int(2/3 * singleObjectHeight) + objectMove), width = self.foldedCmd_singleLineWidth, height = (windowHeight - 2 * sideMove - int(5/3 * singleObjectHeight) - int(2 * objectMove)))
        self.foldedCmd_btnOK.place(x = sideMove, y = int(windowHeight - sideMove - singleObjectHeight), width = int(1/2 * self.foldedCmd_singleLineWidth - 1/2 * objectMove), height = singleObjectHeight)
        self.foldedCmd_btnCancel.place(x = int(1/2 * windowWidth + 1/2 * objectMove), y = int(windowHeight - sideMove - singleObjectHeight), width = int(1/2 * self.foldedCmd_singleLineWidth - 1/2 * objectMove), height = singleObjectHeight)
        
        self.foldedCmdWindow.protocol('WM_DELETE_WINDOW', foldedCmdWindow_exit)
        self.foldedCmdWindow.attributes('-topmost', 'true')

        self.menuCmdEditWindowActive = True

        foldedCmdWindow_update()

    def appSettingsGUI(self, arg1 = None, windowWidth = 640, windowHeight = 480, sideMove = 8, objectMove = 4, singleObjectHeight = 30):
        if self.appSettingsWindowActive == True :
            return 0

        self.appSettingsWindow = Toplevel()

        def appSettingsWindow_update(arg1 = None):
            self.appSettings_labelLocalUser.config(text = self.loadCurrentLang(key = 'appSettingsLocalUser'))
            self.appSettings_labelUserLang.config(text = self.loadCurrentLang(key = 'appSettingsUserLang'))
            if self.menuPopup == True :
                self.showOrHideMenu()
        def appSettingsWindow_exit(arg1 = None):
            self.appSettingsWindowActive = False
            self.appSettingsWindow.destroy()
        def appSettingsWindow_apply(arg1 = None):
            pass
        def appSettings_changeUserName(arg1 = None):
            newName = simpledialog.askstring(self.loadCurrentLang(key = 'appSettingsUserNameChangeTitle'), self.loadCurrentLang(key = 'appSettingsUserNameChangeText'), initialvalue = self.userCfgData['standardData']['userName'], parent = self.tmpWindow)
            if newName == None :
                return 0
            ans = messagebox.askyesno(self.loadCurrentLang(key = 'appSettingsUserNameChangeTitle'), self.loadCurrentLang(key = 'appSettingsUserNameChangeRecheck').format(s = newName))
            print(ans)
            if ans == True :
                self.userCfgData['standardData']['userName'] = newName
                self.saveUserData()
                messagebox.showinfo(self.loadCurrentLang(key = 'appSettingsUserNameChangeTitle'), self.loadCurrentLang(key = 'appSettingsUserNameChangeDone'))
            appSettingsWindow_update()
        def appSettings_changeSearchAddress(arg1 = None):
            newAddress = simpledialog.askstring(self.loadCurrentLang(key = 'appSettingsLocalSearchChangeTitle'), self.loadCurrentLang(key = 'appSettingsUserNameChangeText'), initialvalue = self.userCfgData['onlineServiceData']['searchAddress'], parent = self.tmpWindow)
            if newAddress == None :
                return 0
            ans = messagebox.askyesno(self.loadCurrentLang(key = 'appSettingsLocalSearchChangeTitle'), self.loadCurrentLang(key = 'appSettingsLocalSearchChangeRecheck').format(s = newAddress))
            print(ans)
            if ans == True :
                self.userCfgData['onlineServiceData']['searchAddress'] = newAddress
                self.saveUserData()
                messagebox.showinfo(self.loadCurrentLang(key = 'appSettingsLocalSearchChangeTitle'), self.loadCurrentLang(key = 'appSettingsLocalSearchChangeDone'))
            appSettingsWindow_update()
        def appSettings_setSearchArgs(arg1 = None):
            #newArgs = simpledialog.askstring(self.loadCurrentLang(key = 'appSettingsLocalSearchAssetsSetTitle'), self.loadCurrentLang(key = 'appSettingsLocalSearchAssetsSetText'), initialvalue = self.userCfgData['onlineServiceData']['searchAppendixData'], parent = self.tmpWindow)
            #if newArgs == None :
            #    return 0
            #ans = messagebox.askyesno(self.loadCurrentLang(key = 'appSettingsLocalSearchAssetsSetTitle'), self.loadCurrentLang(key = 'appSettingsLocalSearchAssetsSetRecheck').format(s = newArgs))
            #print(ans)
            #if ans == True :
            #    self.userCfgData['onlineServiceData']['searchAppendixData'] = newArgs
            #    self.saveUserData()
            #    messagebox.showinfo(self.loadCurrentLang(key = 'appSettingsLocalSearchAssetsSetTitle'), self.loadCurrentLang(key = 'appSettingsLocalSearchAssetsSetDone'))

            self.underConstruction()

            appSettingsWindow_update()

        self.appSettingsWindow.geometry('+{x}+{y}'.format(x = int(1/16 * self.popupMenuWindow.winfo_screenwidth()), y = int(1/16 * self.popupMenuWindow.winfo_screenheight())))
        self.appSettingsWindow.config(width = windowWidth, height = windowHeight)
        self.appSettingsWindow.resizable(0, 0)
        self.appSettingsWindow.title(self.loadCurrentLang(key = 'appSettingsWindowTitle'))
        self.appSettingsWindow.iconbitmap((self.appPath + '/' + self.appSettings['application']['iconDir'] + '/' + self.appSettings['application']['windowIcon']))

        self.appSettingsWindow_singleLineWidth = windowWidth - 2 * sideMove

        self.appSettings_title = Label(self.appSettingsWindow, text = self.loadCurrentLang(key = 'appSettingsWindowTitle1'), bg = 'yellow')

        self.appSettings_titleUser = Label(self.appSettingsWindow, text = self.loadCurrentLang(key = 'appSettingsTitleUser'), bg = 'yellow')
        self.appSettings_labelLocalUser = Label(self.appSettingsWindow, text = self.loadCurrentLang(key = 'appSettingsLocalUser'), justify = 'left', anchor = 'w', bg = 'yellow')
        self.appSettings_btnChangeUser = Button(self.appSettingsWindow, text = self.addSign(text = self.loadCurrentLang(key = 'appSettingsChangeUser'), sign = 'enter'), command = self.underConstruction)
        self.appSettings_btnChangeUserName = Button(self.appSettingsWindow, text = self.addSign(text = self.loadCurrentLang(key = 'appSettingsUserNameChange'), sign = 'command'), command = appSettings_changeUserName)
        self.appSettings_btnResetUser = Button(self.appSettingsWindow, text = self.addSign(text = self.loadCurrentLang(key = 'appSettingsUserReset'), sign = 'command'), fg = 'red', command = self.underConstruction)
        self.appSettings_labelUserLang = Label(self.appSettingsWindow, text = self.loadCurrentLang(key = 'appSettingsUserLang'), justify = 'left', anchor = 'w', bg = 'yellow')
        self.appSettings_btnChangeUserLang = Button(self.appSettingsWindow, text = self.addSign(text = self.loadCurrentLang(key = 'appSettingsUserLangChange'), sign = 'enter'), command = self.underConstruction)
        self.appSettings_labelLocalHelper = Label(self.appSettingsWindow, text = self.loadCurrentLang(key = 'appSettingsLocalHelper'), justify = 'left', anchor = 'w', bg = 'yellow')
        self.appSettings_btnChangeHelper = Button(self.appSettingsWindow, text = self.addSign(text = self.loadCurrentLang(key = 'appSettingsChangeHelper'), sign = 'enter'), command = self.underConstruction)
        self.appSettings_btnAboutThisHelper = Button(self.appSettingsWindow, text = self.addSign(text = self.loadCurrentLang(key = 'appSettingsAboutThisHelper'), sign = 'info'), command = self.underConstruction)
        self.appSettings_labelLocalSearch = Label(self.appSettingsWindow, text = self.loadCurrentLang(key = 'appSettingsLocalSearch').format(s = self.userCfgData['onlineServiceData']['searchAddress']), justify = 'left', anchor = 'w', bg = 'yellow')
        self.appSettings_btnChangeSearchAddress = Button(self.appSettingsWindow, text = self.addSign(text = self.loadCurrentLang(key = 'appSettingsLocalSearchChange'), sign = 'enter'), command = appSettings_changeSearchAddress)
        #self.appSettings_btnSetSearchAssets = Button(self.appSettingsWindow, text = self.addSign(text = self.loadCurrentLang(key = 'appSettingsLocalSearchAssetsSet'), sign = 'enter'), command = appSettings_setSearchArgs)
        
        self.appSettings_titleApp = Label(self.appSettingsWindow, text = self.loadCurrentLang(key = 'appSettingsTitleApplication'), bg = 'yellow')
        self.appSettings_btnChangeLogSettings = Button(self.appSettingsWindow) #UNCOMPLETED!!!

        #self.appSettings_btnApply = Button(self.appSettingsWindow, text = self.loadCurrentLang(key = 'btnApply'), command = appSettingsWindow_apply)
        self.appSettings_btnClose = Button(self.appSettingsWindow, text = self.loadCurrentLang(key = 'btnClose'), command = appSettingsWindow_exit)

        self.appSettings_title.place(x = sideMove, y = sideMove, width = self.appSettingsWindow_singleLineWidth, height = int(singleObjectHeight))

        self.appSettings_titleUser.place(x = int(sideMove), y = int(sideMove + singleObjectHeight + objectMove), width = int(1/2 * (windowWidth - objectMove) - sideMove), height = int(singleObjectHeight))
        self.appSettings_labelLocalUser.place(x = int(sideMove), y = int(sideMove + 2 * singleObjectHeight + 2 * objectMove), width = int(1/2 * (windowWidth - objectMove) - sideMove - objectMove - 4 * singleObjectHeight), height = int(singleObjectHeight))
        self.appSettings_btnChangeUser.place(x = int(1/2 * (windowWidth - objectMove)), y = int(sideMove + 2 * singleObjectHeight + 2 * objectMove), width = int(4 * singleObjectHeight), height = singleObjectHeight, anchor = 'ne')
        self.appSettings_btnChangeUserName.place(x = sideMove, y = int(sideMove + 3 * singleObjectHeight + 3 * objectMove), width = int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)), height = int(singleObjectHeight))
        self.appSettings_btnResetUser.place(x = int(sideMove + int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)) + objectMove), y = int(sideMove + 3 * singleObjectHeight + 3 * objectMove), width = int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)), height = int(singleObjectHeight))
        self.appSettings_labelUserLang.place(x = int(sideMove), y = int(sideMove + 4 * singleObjectHeight + 4 * objectMove), width = int(1/2 * (windowWidth - objectMove) - sideMove - objectMove - 4 * singleObjectHeight), height = int(singleObjectHeight))
        self.appSettings_btnChangeUserLang.place(x = int(1/2 * (windowWidth - objectMove)), y = int(sideMove + 4 * singleObjectHeight + 4 * objectMove), width = int(4 * singleObjectHeight), height = singleObjectHeight, anchor = 'ne')
        self.appSettings_labelLocalHelper.place(x = int(sideMove), y = int(sideMove + 5 * singleObjectHeight + 5 * objectMove), width = int(1/2 * (windowWidth - objectMove) - sideMove), height = int(singleObjectHeight))
        self.appSettings_btnChangeHelper.place(x = sideMove, y = int(sideMove + 6 * singleObjectHeight + 6 * objectMove), width = int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)), height = int(singleObjectHeight))
        self.appSettings_btnAboutThisHelper.place(x = int(sideMove + int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)) + objectMove), y = int(sideMove + 6 * singleObjectHeight + 6 * objectMove), width = int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)), height = int(singleObjectHeight))
        self.appSettings_labelLocalSearch.place(x = int(sideMove), y = int(sideMove + 7 * singleObjectHeight + 7 * objectMove), width = int(1/2 * (windowWidth - objectMove) - sideMove), height = int(singleObjectHeight))
        self.appSettings_btnChangeSearchAddress.place(x = sideMove, y = int(sideMove + 8 * singleObjectHeight + 8 * objectMove), width = int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)), height = int(singleObjectHeight))
        #self.appSettings_btnSetSearchAssets.place(x = int(sideMove + int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)) + objectMove), y = int(sideMove + 8 * singleObjectHeight + 8 * objectMove), width = int(1/2 * (1/2 * (windowWidth - objectMove) - sideMove - objectMove)), height = int(singleObjectHeight))
        
        self.appSettings_titleApp.place(x = int(1/2 * (windowWidth + objectMove)), y = int(sideMove + singleObjectHeight + objectMove), width = int(1/2 * (windowWidth - objectMove) - sideMove), height = int(singleObjectHeight))

        #self.appSettings_btnApply.place(x = int(windowWidth - sideMove - 4 * singleObjectHeight - objectMove), y = int(windowHeight - sideMove - singleObjectHeight), width = int(4 * singleObjectHeight), height = singleObjectHeight, anchor = 'ne')
        self.appSettings_btnClose.place(x = int(windowWidth - sideMove), y = int(windowHeight - sideMove - singleObjectHeight), width = int(4 * singleObjectHeight), height = singleObjectHeight, anchor = 'ne')
        
        self.appSettingsWindow.protocol('WM_DELETE_WINDOW', appSettingsWindow_exit)

        self.appSettingsWindowActive = True

        #self.saveUserData()

        appSettingsWindow_update()

    def appSettings_enableSuperSecretSettings(self): #Enable super secret settings so that some hidden developing features can be shown for testing
        if self.appSettings['advanced']['enableSuperSecret'] == True :
            return 0
        ans = []
        for x in range(1, 4):
            ans_ = messagebox.askyesno(self.loadCurrentLang(key = 'appSettingsWindowTitle'), self.loadCurrentLang(key = ('appSettingsSuperSecretEnableCheck' + str(x))), default = 'no')
            if ans_ != True :
                return 0
            ans.append(ans_)
        if ans == [True, True, True] :
            self.shellOutput('Changing settings...')
            self.appSettings['advanced']['enableSuperSecret'] = True
            self.shellOutput('Saving settings...')
            self.saveAppData()
            self.shellOutput('SuperSecretSettings enabled. You have to restart the application to apply the changes.')
            messagebox.showinfo(self.loadCurrentLang(key = 'appSettingsWindowTitle'), self.loadCurrentLang(key = 'appSettingsSuperSecretEnableNote'))

    def appSettings_disableSuperSecretSettings(self): #Disable super secret settings so that some shown developing features can be hidden for daily uses.
        if self.appSettings['advanced']['enableSuperSecret'] == False :
            return 0
        ans = messagebox.askyesno(self.loadCurrentLang(key = 'appSettingsWindowTitle'), self.loadCurrentLang(key = 'appSettingsSuperSecretDisableCheck'))
        if ans == True :
            self.shellOutput('Changing settings...')
            self.appSettings['advanced']['enableSuperSecret'] = False
            self.shellOutput('Saving settings...')
            self.saveAppData()
            self.shellOutput('SuperSecretSettings disabled. You have to restart the application to apply the changes.')
            messagebox.showinfo(self.loadCurrentLang(key = 'appSettingsWindowTitle'), self.loadCurrentLang(key = 'appSettingsSuperSecretDisableNote'))

    def appSettings_menuLauncher(self, arg1 = None):
        self.appSettingsGUI()

    def menuReinit(self, x_move = 40, y_move = 36, title = 'DEBUG', sideMove = 8, objectMove = 4, singleObjectHeight = 30):
        for x in self.popupMenuWindow.winfo_children():
            x.destroy()

        try :
            self.menuWidth = self.userCfgData['featureData']['mainMenu']['mainMenuWidth']
        except :
            self.shellOutput('[X]Unable to load the custom menu width data. Will use the normal setting 160.')
            self.menuWidth = 160
        self.menuHeight = self.mainWindow.winfo_y() - y_move - 32
        self.menuPosX = self.mainWindow.winfo_x() - (self.menuWidth - self.mainWindow.winfo_width())
        if self.menuPosX < int(1/10 * self.mainWindow.winfo_screenwidth()):
            self.menuPosX = self.mainWindow.winfo_x()
        if self.menuHeight <= int(1/5 * self.mainWindow.winfo_screenheight()) :
            self.menuHeight = self.mainWindow.winfo_screenheight() - self.mainWindow.winfo_y() - self.mainWindow.winfo_height() - 3 * y_move - 16
            self.menuPosY = self.mainWindow.winfo_y() + self.mainWindow.winfo_height() + y_move
        else :
            self.menuPosY = self.mainWindow.winfo_y() - y_move - self.menuHeight
        self.menuTitle = self.loadCurrentLang(key = 'menuTitle')
        self.menu_singleLineWidth = self.menuWidth - 2 * sideMove
        self.popupMenuWindow.config(width = self.menuWidth, height = self.menuHeight)
        self.popupMenuWindow.geometry('+{x}+{y}'.format(x = self.menuPosX, y = self.menuPosY))
        self.popupMenuWindow.title(self.menuTitle)

        self.menu_titleLabel = Label(self.popupMenuWindow, text = self.loadCurrentLang(key = 'menuTitle1'), bg = 'yellow', wraplength = int((self.menuWidth - 2 * sideMove)))
        self.menu_searchBtn = Button(self.popupMenuWindow, text = self.addSign(text = self.loadCurrentLang(key = 'menuOnlineSearchBtn'), sign = 'enter'), command = self.onlineSearch)
        self.menu_versionTag = Label(self.popupMenuWindow, text = self.getLang(text = '{appName} {appVer}', mode = 'text'))
        self.menu_separator = ttk.Separator(self.popupMenuWindow)
        self.menu_separator1 = ttk.Separator(self.popupMenuWindow)

        if time.strftime('%m%d') == '0723' : #Mr.Pan, we miss you! 2011.7.23-2025.7.23
            txt = self.getLang(text = random.choice(["{userName}:\nIt's been {s} years.", "{userName}:\nCRH2-139E!", "{userName}:\nR.I.P. Pan Yiheng", "{userName}:\nMr.Pan is a hero."]), mode = 'text').format(s = int(time.strftime('%Y')) - 2011)
            self.menu_titleLabel.config(text = txt)


        self.listMaxHeight = self.menuHeight - int(8/3 * singleObjectHeight) - 4 * objectMove - 2 * sideMove  - objectMove - 2
        self.listTopY = sideMove + int(4/3 * singleObjectHeight) + 2 * objectMove

        self.menuList = []
        self.menuList_folded = []
        self.menuFolded = False
        for x in range(len(self.userCfgData['menuListData'])):
            def runCmd(data = self.userCfgData['menuListData'][x], arg1 = None):
                print(data)
                def runOSCmd(cmd = data['command'], arg1 = None):
                    self.debugCommand(cmd = 'sysdebug {s}'.format(s = cmd))
                def runDebugCmd(cmd = data['command'], arg1 = None):
                    self.debugCommand(cmd = data['command'])
                if data['mode'].upper() == 'OS' :
                    threading.Thread(target = runOSCmd).start()
                elif data['mode'].lower() == 'builtin' :
                    threading.Thread(target = runDebugCmd).start()
                else :
                    self.shellOutput('[X]self.menuReinit:Invalid mode {m}. Will see it as Builtin.'.format(m = data['command']))
                    threading.Thread(target = runDebugCmd).start()
            try :
                btnHeight = self.userCfgData['menuListData'][x]['length'] * singleObjectHeight
            except :
                self.shellOutput('[X]self.menuReinit:Invalid length {l}. Will change it to 1.'.format(l = self.userCfgData['menuListData'][x]['length']))
                btnHeight = 1 * singleObjectHeight
            tmp1 = Button(self.popupMenuWindow, text = self.getLang(text = self.userCfgData['menuListData'][x]['title'], mode = 'text'), command = lambda a=self.userCfgData['menuListData'][x]:runCmd(a))

            heightNow = 0
            for y in self.menuList :
                heightNow += y[1]
                heightNow += objectMove
            if (heightNow + btnHeight + objectMove + 1 * singleObjectHeight > self.listMaxHeight) or (self.menuFolded == True) :
                try :
                    if self.menuFolded == False :
                        self.menuList.pop(-1)
                        self.menuList_folded.append({'title' : self.userCfgData['menuListData'][x - 1]['title'], 'command' : self.userCfgData['menuListData'][x - 1]['command'], 'mode' : self.userCfgData['menuListData'][x - 1]['mode']})
                        self.menuFolded = True
                    self.menuList_folded.append({'title' : self.userCfgData['menuListData'][x]['title'], 'command' : self.userCfgData['menuListData'][x]['command'], 'mode' : self.userCfgData['menuListData'][x]['mode']})
                except :
                    pass
            else :
                self.menuList.append([tmp1, int(btnHeight)])
            #del tmp1
            #del btnHeight
        self.menu_appendCommandBtn = Button(self.popupMenuWindow, text = self.addSign(text = self.loadCurrentLang(key = 'menuAddCommandBtn'), sign = 'add'), command = self.menu_appendCmd)
        self.menu_removeCommandBtn = Button(self.popupMenuWindow, text = self.addSign(text = self.loadCurrentLang(key = 'menuRemoveCommandBtn'), sign = 'remove'), command = self.menu_removeCmd)

        self.menu_titleLabel.place(x = sideMove, y = sideMove, width = (self.menuWidth - 2 * sideMove), height = int(4/3 * singleObjectHeight))
        self.menu_searchBtn.place(x = sideMove, y = (self.menuHeight - sideMove - singleObjectHeight - objectMove - int(1/3 * singleObjectHeight)), width = (self.menuWidth - 2 * sideMove), height = singleObjectHeight)
        self.menu_versionTag.place(x = sideMove, y = (self.menuHeight - sideMove - int(1/3 * singleObjectHeight)), width = self.menu_singleLineWidth, height = int(1/3 * singleObjectHeight))
        self.menu_separator.place(x = sideMove, y = (sideMove + int(4/3 * singleObjectHeight) + objectMove - 1), width = self.menu_singleLineWidth, height = 2)

        menuMove = 0
        for x in self.menuList :
            x[0].place(x = sideMove, y = (self.listTopY + menuMove), width = self.menu_singleLineWidth, height = x[1], anchor = 'nw')
            menuMove += x[1]
            menuMove += objectMove
        if self.menuFolded == True :
            self.menu_btnFolded = Button(self.popupMenuWindow, text = self.loadCurrentLang(key = 'menuFoldedCommandsBtn').format(s = len(self.menuList_folded)), command = self.menu_foldedCmd)
            self.menu_btnFolded.place(x = sideMove, y = (self.listTopY + menuMove), width = self.menu_singleLineWidth, height = x[1], anchor = 'nw')
        self.menu_separator1.place(x = sideMove, y = (self.listTopY + self.listMaxHeight - singleObjectHeight), width = self.menu_singleLineWidth, height = 2)
        self.menu_appendCommandBtn.place(x = sideMove, y = (self.listTopY + self.listMaxHeight - singleObjectHeight + objectMove + 2), width = int(self.menu_singleLineWidth / 2 - 1/2 * objectMove), height = singleObjectHeight)
        self.menu_removeCommandBtn.place(x = int(sideMove + 1/2 * self.menu_singleLineWidth + 1/2 * objectMove), y = (self.listTopY + self.listMaxHeight - singleObjectHeight + objectMove + 2), width = int(self.menu_singleLineWidth / 2 - 1/2 * objectMove), height = singleObjectHeight)

        #self.saveUserData()
        self.update()

    def showMenu(self):
        if self.active == True :
            self.menuReinit()
            self.popupMenuWindow.deiconify()
            self.menuPopup = True
        else :
            self.shellOutput('Failed to show menu: main window is not active')
        self.update()

    def hideMenu(self, saveData = True):
        self.popupMenuWindow.withdraw()
        self.menuPopup = False
        if saveData == True :
            self.saveUserData()
        self.update()

    def showOrHideMenu(self, arg1 = None):
        if self.menuPopup == False :
            if self.active == True :
                self.showMenu()
        elif self.menuPopup == True :
            self.hideMenu()
        else :
            self.shellOutput('[X]self.showOrHideMenu:Invalid value of self.menuPopup: {v} .'.format(v = self.menuPopup))
            self.hideMenu(saveData = False)
        #self.saveUserData()
        #self.mainWindow.after(10, self.update)
        #self.update()

    def showOrHide(self, arg1 = None):
        if self.active == True :
            self.hideWindow()
        elif self.active == False :
            self.showWindow()
        else :
            self.active = False
            self.hideWindow()

    def quitFurry(self, saveData = True):
        if saveData == True :
            self.saveData()
        self.shellOutput('Quitting furry...\n') #Leave a empty line so that the log can be more readable
        try :
            self.popupMenuWindow.destroy() #Close the popup menu window first
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
        self.mainWindow.quit()
        quit()

    def quitApp(self, arg1 = None):
        ans = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleRecheck'), self.loadCurrentLang(key = 'messageQuit'))
        #print(ans, type(ans))
        if ans == True :
            self.quitFurry()

    def showRightMenu(self, arg1 = None):
        self.rightMenu.post(self.mainWindow.winfo_pointerx(), self.mainWindow.winfo_pointery())

    def reinit(self):
        self.configEncodings = ['utf-8', 'gbk', 'gb2312', 'ANSI']
        #Load file list
        with open((dataDir + "/fileList.json"), 'r', encoding = 'utf-8', errors = 'ignore') as flistfe:
            flistdata = json.loads(flistfe.read())
            self.appPath = dataDir + '/' + flistdata['application']['dir']
            print(self.appPath)
        self.cfgPath = self.appPath + '/' + flistdata['application']['mainCfgFile']
        #Load main application config
        with open(self.cfgPath, 'r', encoding = 'utf-8', errors = 'ignore') as cfgfe:
            self.appSettings = json.loads(cfgfe.read())
            #print(self.appSettings)
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
        #print(self.appLangData)
        self.shellOutput('Loaded lang data: {s}({t}, Version {u})'.format(s = self.appLangData['name'], t = self.appLangData['type'], u = self.appLangData['ver']))

        #Load user config
        self.userDir = self.appPath + '/' + self.appSettings['user']['userCfgDir'] #Load user config file path
        self.normalUser = self.appSettings['user']['normalUser']
        self.normalUserDir = self.userDir + '/' + self.appSettings['user']['userList'][self.normalUser]['dir']
        try : #Open config file and load data
            self.userMainCfgFile = self.normalUserDir + '/' + self.appSettings['user']['userList'][self.normalUser]['mainCfgFile']
            userConfigFileCheck = open(self.userMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore')
            userConfigFileCheck.close()
            self.shellOutput('Loaded user config file: {s}'.format(s = self.userMainCfgFile))
        except :
            self.shellOutput('[X]Set user config file load failed.')
            self.userMainCfgFile = self.normalUserDir + '/userConfigs.json'
            userConfigFile = open(self.userMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore')
            userConfigFileCheck.close()
            self.shellOutput('Loaded user config file: {s}'.format(s = ('')))
        userCfgReadSuccess = False
        for x in self.configEncodings :
            try :
                userConfigFile = open(self.userMainCfgFile, 'r', encoding = x)
                userConfigData = userConfigFile.read()
                userCfgReadSuccess = True
            except :
                continue
        if userCfgReadSuccess == False :
            userConfigFile = open(self.userMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore')
            userConfigData = userConfigFile.read()
        self.userCfgData = json.loads(userConfigData)
        userConfigFile.close()
        #print(self.userCfgData)
        self.onlineSearchAddress = self.userCfgData['onlineServiceData']['searchAddress']
        self.automaticData = self.userCfgData['automaticData']
        self.menuList = []
        self.menuClick1 = 0
        self.shellOutput('Loaded user: {s}(UserID Length: {t})'.format(s = self.userCfgData['standardData']['userName'], t = len(self.userCfgData['standardData']['userID'])))

        #Load furry config
        self.furryDir = dataDir + '/' + flistdata['application']['dir'] + '/' + self.appSettings['furry']['furryCfgDir']
        self.normalFurry = self.userCfgData['standardData']['loadedFurry']
        self.normalFurryDir = self.furryDir + '/' + self.appSettings['furry']['furryList'][self.normalFurry]['dir']
        try :
            self.furryMainCfgFile = self.normalFurryDir + '/' + self.appSettings['furry']['furryList'][self.normalFurry]['mainCfgFile']
            furryConfigFileCheck = open(self.furryMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore')
            furryConfigFileCheck.close()
        except :
            self.furryMainCfgFile = self.normalFurryDir + '/furryConfigs.json'
            print(self.furryMainCfgFile)
            furryConfigFileCheck = open(self.furryMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore')
            furryConfigFileCheck.close()
        furryCfgReadSuccess = False
        for x in self.configEncodings :
            try :
                furryConfigFile = open(self.furryMainCfgFile, 'r', encoding = x)
                furryConfigData = furryConfigFile.read()
                furryCfgReadSuccess = True
            except :
                continue
        if furryCfgReadSuccess == False :
            furryConfigFile = open(self.furryMainCfgFile, 'r', encoding = 'utf-8', errors = 'ignore')
            furryConfigData = furryConfigFile.read()
        self.furryCfgData = json.loads(furryConfigData)
        #print(self.furryCfgData)
        furryConfigFile.close()
        self.furryImagePath = self.normalFurryDir + '/' + self.furryCfgData['standardData']['imagePath']
        self.furryImages = self.furryCfgData['standardData']['images'] #Load image data
        self.furryAction = self.furryCfgData['standardData']['normalImage'] #Load main image
        self.bgImage = None
        self.furryImage = None #Set a empty port
        self.furryTag = self.furryCfgData['standardData']['tag']
        self.shellOutput('Loaded furry: {s}(Builtin Tag: {t})'.format(s = self.furryCfgData['standardData']['name'], t = self.furryCfgData['standardData']['tag']))

        #Load furry customized lang
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

        self.strayMenu = (pystray.MenuItem(self.getLang(key = 'furryInfo', fromDic = self.currentLangData), self.aboutApp),
                          pystray.Menu.SEPARATOR,
                          pystray.Menu.SEPARATOR,
                          pystray.MenuItem(self.getLang(key = 'showOrHide', fromDic = self.currentLangData), self.showOrHide),
                          pystray.MenuItem(self.getLang(key = 'toolMenu', fromDic = self.currentLangData), self.showOrHideMenu),
                          pystray.Menu.SEPARATOR,
                          #pystray.MenuItem(self.getLang(key = 'appSettings', fromDic = self.currentLangData), self.appSettings_menuLauncher),
                          #pystray.MenuItem(self.getLang(key = 'appHelp', fromDic = self.currentLangData), self.underConstruction),
                          pystray.MenuItem(self.getLang(key = 'quit', fromDic = self.currentLangData), self.quitApp)
                          )
        self.furryStrayIconImage = Image.open((self.appPath + '/' + self.appSettings['application']['iconDir'] + '/' + self.appSettings['application']['strayIcon']))
        self.furryStray = pystray.Icon(appSettings['appName'], self.furryStrayIconImage, self.getLang(key = 'strayInfo', fromDic = self.currentLangData), self.strayMenu)

        if (self.userCfgData['standardData']['OOBELoaded'] == False) or (self.userCfgData['advancedData']['rootUser'] == True and self.appSettings['advanced']['rootAllowed'] == False) :
            self.shellOutput('[i]OOBE is not loaded.Starting OOBE...')
            self.appOOBE()
        
        self.shellOutput('Application settings loaded.')
        
    def __init__(self, windowWidth = 128, windowHeight = 128):
        #self.reinit() #For getting error reports in self.reinit only.
        try :
            self.windowWidth = windowWidth
            self.windowHeight = windowHeight

            self.mainWindow = Toplevel()
            self.mainWindow.config(width = self.windowWidth, height = self.windowHeight)

            self.mainWindow.withdraw()
            self.reinit()
            #print(0)

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
                self.shellOutput('[!]self.mainWindow:Host oprating system does not support "toolwindow".')
            self.mainWindow.resizable(0, 0)
            self.scr = Canvas(self.mainWindow, width = self.windowWidth, height = self.windowHeight, highlightthickness = 0)
            #if self.transParent == True :
            #    self.scr.config(bg = self.windowTransParentColor)
            self.scr.place(x = 0, y = 0, width = self.windowWidth, height = windowHeight, anchor = 'nw')

            self.rightMenu = Menu(self.mainWindow, tearoff = False)
            self.rightMenu.add_command(label = self.getLang(key = 'furryInfo', fromDic = self.currentLangData), command = self.aboutApp)
            self.rightMenu.add_command(label = self.addSign(text = self.loadCurrentLang(key = 'showOrHide'), sign = 'enter'), command = self.showOrHide)
            self.rightMenu.add_command(label = self.addSign(text = self.getLang(key = 'toolMenu', fromDic = self.currentLangData), sign = 'enter'), command = self.showOrHideMenu)
            if self.appSettings['advanced']['enableSuperSecret'] == True :
                self.rightMenu.add_command(label = self.addSign(text = self.getLang(key = 'appSettings', fromDic = self.currentLangData), sign = 'enter'), command = self.appSettings_menuLauncher)
                self.rightMenu.add_command(label = self.addSign(text = self.getLang(key = 'appHelp', fromDic = self.currentLangData), sign = 'help'), command = self.underConstruction)
            self.rightMenu.add_command(label = self.addSign(text = self.getLang(key = 'quit', fromDic = self.currentLangData), sign = 'enter'), command = self.quitApp)

            posValid = False
            try :  #Check if the saved pos data is valid or not
                if (type(self.userCfgData['featureData']['savedMainWindowPos']['x']) != int) or (type(self.userCfgData['featureData']['savedMainWindowPos']['y']) != int):
                    posValid = False
                else :
                    posValid = True #If saved pos data is valid, use it
                    self.mainWindow.geometry('+{x}+{y}'.format(x = self.userCfgData['featureData']['savedMainWindowPos']['x'], y = self.userCfgData['featureData']['savedMainWindowPos']['y']))
            except : #Read failed, reset it
                posValid = False
            if posValid == False : #If saved pos data is not valid, reset it
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
                self.shellOutput('[X]self.popupMenuWindow:Host oprating system does not support ToolWindow.')
            self.popupMenuWindow.protocol('WM_DELETE_WINDOW', self.showOrHideMenu)
            self.popupMenuWindow.withdraw()
            self.menuPopup = False

            self.scr.tag_bind(self.furryCfgData['standardData']['tag'], "<Button-1>", self.showOrHideMenu)
            self.scr.tag_bind(self.furryCfgData['standardData']['tag'], "<Button-3>", self.showRightMenu)
            self.mainWindow.bind('<Configure>', self.onMainWindowMove)

            #print(self.userCfgData['standardData']['userID'])

            self._1_ = False
            self.menuCmdEditWindowActive = False
            self.appSettingsWindowActive = False
            #self.tick1 = 0
        except Exception as errData :
            messagebox.showerror('ERROR', 'Failed to load data. The application will be closed.\nMake sure the asset files are available and the assets are valid, then launch the application again.\nException Data:\n{data}'.format(data = '\n'.join([str(errData.__traceback__), str(traceback.extract_tb(errData.__traceback__)), str(type(errData))])))
            quit()
        #self.shellOutput('', withTime = False)
        #self.shellOutput('DEBUG')
        self.shellOutput('Application Launched.')

    def startFurry(self):
        self.showWindow()
        threading.Thread(target = self.furryStray.run, daemon = True).start()
        self.applicationClock()
        if self.userCfgData["advancedData"]["hideFurryWhenStartup"] == True :
            self.showOrHide()
            self.furryStray.notify(self.loadCurrentLang(key = 'messageHideWhenStartup'), self.loadCurrentLang(key = 'messageTitleHide'))
        self.mainWindow.mainloop()

main = Furry()
main.startFurry()
#quit()
