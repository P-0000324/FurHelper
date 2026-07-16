import json

class FurryPersistence:
    def saveConfigToFile(self, config = {"DEBUG" : "DEBUG"}, file_path = 'debug.json', mode = 'w', encoding = 'utf-8', dump = True):
        try :
            if dump == True :
                cfgData = json.dumps(config)
            else :
                cfgData = str(config)
            with open(file_path, mode, encoding = encoding) as cfgFile:
                cfgFile.write(cfgData)
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
