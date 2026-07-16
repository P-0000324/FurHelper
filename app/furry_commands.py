import os
import threading
import webbrowser
import random
import time
from tkinter import messagebox
from tkinter import simpledialog

class FurryCommands:
    def debugCommand(self, cmd = 'echo Hello World!', mode = 'shell', ignoreErrs = False, outputWithGUI = False, adminID = -1):
        def output(data = 'DEBUG', forceShell = False, toLog = False):
            if outputWithGUI == True and forceShell == False :
                self.shellOutput(data, withGUI = True)
            else :
                self.shellOutput(data)
            if toLog == True :
                logEntry = '[{dateTime}]{data}'.format(dateTime = time.strftime('%y.%m.%d %H%M%S'), data = data)
                with open((self.appPath + self.appSettings['application']['logDir'] + '/appLog_{date}.log'.format(dateTime = time.strftime('%y%m%d'))), 'a', encoding = 'utf-8') as fe :
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
            allow = self.appUAC_askForPermission(cmdAssets = cmdAssets)
            if allow == True :
                threading.Thread(target = runCmd).start()
                output(data = '[i]Command Prompt Loaded: {cmd}'.format(cmd = cmdAssets), forceShell = True)
        elif cmdMain in ['syswebapi'] :
            def runCmd(arg1 = None):
                webbrowser.open(cmdAssets)
            allow = self.appUAC_askForPermission(cmdAssets = cmdAssets)
            if allow == True :
                threading.Thread(target = runCmd).start()
                output(data = '[i]Opened page: {cmd}'.format(cmd = cmdAssets), forceShell = True)
        elif cmdMain in ['pass'] :
            output(data = '[i]Pass!')
        elif cmdMain in ['doNothing', 'doNothing'] :
            pass
        elif cmdMain in ['test'] :
            messagebox.showinfo('TEST', 'TEST!')
        elif cmdMain in ['load', 'loadfe', 'run'] :
            try :
                with open(' '.join(cmdAssets), 'r', encoding = 'utf-8') as fe :
                    data = fe.read().split('\n')
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
        messagebox.askyesno('', 'A furry is knocking at your door.\nOpen the door?')

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
                        raise ValueError('Too few lines')
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
        searchTag = simpledialog.askstring(self.loadCurrentLang(key = 'menuOnlineSearchTitle'), self.loadCurrentLang(key = 'menuOnlineSearch'), parent = self.tmpWindow)
        if searchTag == None or searchTag == '' :
            return 0
        if searchTag[0] in ['/', '\\'] :
            self.debugCommand(cmd = searchTag[1:], mode = 'shell', outputWithGUI = True)
        else :
            self.onlineSearch(searchTag = searchTag)

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

        searchAdd1 = self.onlineSearchAddress.format(s = work(text = searchTag))
        try :
            if self.userCfgData['onlineServiceData']['searchAssetsAppendix'] == True :
                searchAdd1 = ' '.join([searchAdd1, self.userCfgData['onlineServiceData']['searchAppendixData']])
        except :
            pass
        permission = self.appUAC_askForPermission(maximumPassLevel = 5, minimumNotificationLevel = 5, cmdAssets = searchAdd1)
        if permission == True :
            webbrowser.open(searchAdd1)
        self.saveData()
