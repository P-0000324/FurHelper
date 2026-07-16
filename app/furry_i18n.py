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

    def aboutApp(self, arg1 = None) :
        txt = self.loadCurrentLang(key = 'messageAbout', popEmptyLines = True)
        superSecret1 = False
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
        messagebox.showinfo(self.loadCurrentLang(key = 'messageTitleAbout'), txt)

    def doNothing(self):
        self.shellOutput('I did nothing!:D', toLog = False)

    def underConstruction(self, arg1 = None):
        messagebox.showinfo(self.loadCurrentLang(key = 'messageTitleUnderConstruction'), self.loadCurrentLang(key = 'messageUnderConstruction'))
