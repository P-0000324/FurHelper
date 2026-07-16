import time
import threading
import os
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class FurryGUI:
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
        if txt1[-1] == '\n' :
            txt1.pop(-1)
        txt1 = ''.join(txt1)
        self.userCfgData['featureData']['noteBoard']['text'] = txt1
        self.saveUserData()
        self.noteBoardWindow.withdraw()

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

        resetPos = False
        if self.mainWindow.winfo_x() + self.windowWidth > self.mainWindow.winfo_screenwidth():
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

    def showWindow(self):
        self.active = True
        self.update()

    def hideWindow(self):
        self.active = False
        self.furryStray.notify(self.loadCurrentLang(key = 'messageHide'), self.loadCurrentLang(key = 'messageTitleHide'))
        self.update()

    def showOrHide(self, arg1 = None):
        if self.active == True :
            self.hideWindow()
        elif self.active == False :
            self.showWindow()
        else :
            self.active = False
            self.hideWindow()

    def onMainWindowMove(self, arg1 = None):
        if (self.userCfgData['featureData']['savedMainWindowPos']['x'] != self.mainWindow.winfo_x() or self.userCfgData['featureData']['savedMainWindowPos']['y'] != self.mainWindow.winfo_y()) and (self.menuPopup == True) :
            self.showOrHideMenu()
        self.userCfgData['featureData']['savedMainWindowPos']['x'] = self.mainWindow.winfo_x()
        self.userCfgData['featureData']['savedMainWindowPos']['y'] = self.mainWindow.winfo_y()
        self.update()

    def mainWindowPosReset(self, x_move = 40, y_move = 95):
        self.windowPosX = self.mainWindow.winfo_screenwidth() - x_move - self.windowWidth
        self.windowPosY = self.mainWindow.winfo_screenheight() - y_move - self.windowHeight
        self.mainWindow.geometry('+{x}+{y}'.format(x = self.windowPosX, y = self.windowPosY))
        self.userCfgData['featureData']['savedMainWindowPos']['x'] = self.mainWindow.winfo_x()
        self.userCfgData['featureData']['savedMainWindowPos']['y'] = self.mainWindow.winfo_y()
        self.saveUserData()

    def showRightMenu(self, arg1 = None):
        self.rightMenu.post(self.mainWindow.winfo_pointerx(), self.mainWindow.winfo_pointery())

    def menu_appendCmd(self, arg1 = None, windowWidth = 400, windowHeight = 230, sideMove = 8, objectMove = 4, singleObjectHeight = 30):
        if self.menuCmdEditWindowActive == True :
            return 0

        self.appendCmdWindow = Toplevel()

        modeList = ('Builtin', 'OS')
        modeNormal = 0

        def appendCmdWindow_update(arg1 = None):
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

        modeList = ('Builtin', 'OS')
        modeNormal = 0

        def removeCmdWindow_update(arg1 = None):
            self.removeCmd_cmdList.delete(0, END)
            self.removeCmd_cmdTable = {}
            for x in range(len(self.userCfgData['menuListData'])):
                self.removeCmd_cmdTable[self.userCfgData['menuListData'][x]['title']] = x
            for y in self.removeCmd_cmdTable.keys():
                self.removeCmd_cmdList.insert(END, y)
        def removeCmdWindow_exit(arg1 = None):
            ans = True
            if ans == True :
                self.menuCmdEditWindowActive = False
                self.removeCmdWindow.destroy()
        def removeCmdWindow_apply(arg1 = None):
            selection = list(self.removeCmd_cmdList.curselection())
            cmdToRemove = []
            cmdRemoveList = []
            for x in selection :
                toRemove = self.removeCmd_cmdList.get(x)
                print(toRemove)
                cmdToRemove.append(self.removeCmd_cmdTable[toRemove])
                cmdRemoveList.append(str('=>' + toRemove))
            if len(cmdToRemove) > 0 :
                ans = messagebox.askyesno(self.loadCurrentLang(key = 'messageTitleTips'), self.loadCurrentLang(key = 'menuRemoveCommandMessageRecheck').format(s = '\n'.join(cmdRemoveList)))
                if ans == True :
                    cmdToRemove.sort(reverse = True)
                    self.shellOutput(('Will remove: ' + str(cmdToRemove)))
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

        self.appSettings_titleApp = Label(self.appSettingsWindow, text = self.loadCurrentLang(key = 'appSettingsTitleApplication'), bg = 'yellow')
        self.appSettings_btnChangeLogSettings = Button(self.appSettingsWindow)

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

        self.appSettings_titleApp.place(x = int(1/2 * (windowWidth + objectMove)), y = int(sideMove + singleObjectHeight + objectMove), width = int(1/2 * (windowWidth - objectMove) - sideMove), height = int(singleObjectHeight))

        self.appSettings_btnClose.place(x = int(windowWidth - sideMove), y = int(windowHeight - sideMove - singleObjectHeight), width = int(4 * singleObjectHeight), height = singleObjectHeight, anchor = 'ne')

        self.appSettingsWindow.protocol('WM_DELETE_WINDOW', appSettingsWindow_exit)

        self.appSettingsWindowActive = True

        appSettingsWindow_update()

    def appSettings_enableSuperSecretSettings(self):
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

    def appSettings_disableSuperSecretSettings(self):
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
        self.menu_searchBtn = Button(self.popupMenuWindow, text = self.addSign(text = self.loadCurrentLang(key = 'menuOnlineSearchBtn'), sign = 'enter'), command = self.onlineSearchWindow)
        self.menu_versionTag = Label(self.popupMenuWindow, text = self.getLang(text = '{appName} {appVer}', mode = 'text'))
        self.menu_separator = ttk.Separator(self.popupMenuWindow)
        self.menu_separator1 = ttk.Separator(self.popupMenuWindow)

        if time.strftime('%m%d') == '0723' :
            txt = self.getLang(text = random.choice(["{userName}:\nIt's been {s} years.", "{userName}:\nCRH2-139E!", "{userName}:\nR.I.P. Pan Yiheng", "{userName}:\nMr.Pan is a hero."]), mode = 'text').format(s = int(time.strftime('%Y')) - 2011)
            self.menu_titleLabel.config(text = txt)
        if time.strftime('%m%d') == '0528' :
            txt = self.getLang(text = random.choice(["P0000324:\nYou're {s} now!", "P0000324:\nHappy Birthday!"]), mode = 'text').format(s = int(time.strftime('%Y')) - 2010)
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
                self.menuList.append([tmp1, int(1 * singleObjectHeight)])
        if len(self.menuList) <= 0 :
            self.menuList.append([Button(self.popupMenuWindow, text = self.loadCurrentLang(key = 'menuAddCommandBtnEmptyList'), command = self.menu_appendCmd), int(singleObjectHeight)])

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
