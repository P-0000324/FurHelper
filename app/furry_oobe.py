import random
import json
import os
from tkinter import messagebox
from tkinter import simpledialog
from app.config import appSettings

class FurryOOBE:
    def userGenerator(self, userPathTitle = "DEBUG", cfgFile = 'userConfigs.json', userName = 'DEBUG', userSearchAddress = 'http://localhost', userRootUser = False, userHideFurryWhenStartup = False, userUACLevel = 3):
        self.shellOutput('userGenerator Launched.')
        def userIDGenerator(len_ = random.randint(64, 324)):
            dic_ = list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
            userID = []
            for x in range(len_):
                userID.append(random.choice(dic_))
            userID = ''.join(userID)
            return userID
        with open((self.userDir + '/__userInit__/userConfigs.json'), 'r', encoding = 'utf-8') as userInitData :
            userData = json.loads(str(userInitData.read()))
        userID = userIDGenerator()
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

        self.userCfgData = newUserData[4]

        self.saveUserData()
        self.shellOutput('OOBE set done. Reloading application data...')
        self.reinit()
