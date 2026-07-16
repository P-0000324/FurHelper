from tkinter import messagebox

class FurryAuth:
    def appUAC_checkAdminID(self, ID = -1, mode = 'shell'):
        if (ID > (64 ** 2)) and (ID % 324 == 0) and (ID % 2147 == 324) and (mode == 'shell') :
            return True
        else :
            return False

    def appUAC_askForPermission(self, maximumPassLevel = 3, minimumNotificationLevel = 2, adminID = -1, cmdAssets = 'debug'):
        self.shellOutput(('[i]UAC: The settings now is ' + str([self.userCfgData['advancedData']['UACLevel'], self.appUAC_checkAdminID(ID = adminID), self.userCfgData['advancedData']['UACLevel']])))
        if (self.userCfgData['advancedData']['UACLevel'] > 0 and self.appUAC_checkAdminID(ID = adminID) == False) and (self.userCfgData['advancedData']['UACLevel'] >= maximumPassLevel) :
            default_ = 'no'
            allow = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleUAC'), self.loadCurrentLang(key = 'messageUAC').format(s = cmdAssets), default = default_)
        elif self.appUAC_checkAdminID(ID = adminID) == True or self.userCfgData['advancedData']['UACLevel'] < maximumPassLevel :
            allow = True
            if self.userCfgData['advancedData']['UACLevel'] >= minimumNotificationLevel :
                self.furryStray.notify(self.loadCurrentLang(key = 'messageTitleUAC2'), self.loadCurrentLang(key = 'messageUAC2').format(s = cmdAssets))
        else :
            self.shellOutput(text = '[X]Invalid state {s}.Will change it to 0.'.format(s = self.userCfgData['advancedData']['UACLevel']).format(s = cmdAssets))
            self.userCfgData['advancedData']['UACLevel'] = 0
            allow = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleUAC'), self.loadCurrentLang(key = 'messageUAC'))
        return allow
