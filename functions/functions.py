from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox, QColorDialog
from qt_material import apply_stylesheet
import configparser
import keyboard
import time
import os

# import example code
from examples.example_code import *

# upper dir
upper_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

# error or info message I dont know why you ask me read the code
def msg(self, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle("information / error")
    msg.setText(str(text))
    msg.exec_()
    return

# color changing wheel
def SelectColor(self, Button):
    color = QColorDialog.getColor()
    if Button == "KeywordColorChnage_btn":
        self.KeywordColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    elif Button == "NummbersColorChnage_btn":
        self.NummbersColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    elif Button == "BraceColorChnage_btn": 
        self.BraceColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    elif Button == "DefClassColorChnage_btn":
        self.DefClassColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    elif Button == "StringColorChnage_btn":
        self.StringColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    elif Button == "String2ColorChnage_btn":
        self.String2ColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    elif Button == "CommentColorChnage_btn":
        self.CommentColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    elif Button == "SelfColorChnage_btn":
        self.SelfColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    elif Button == "OperatorColorChnage_btn":
        self.OperatorColorChnage_btn.setStyleSheet("background-color: rgb(" + str(color.red()) + ", " + str(color.green()) + ", " + str(color.blue()) + ");")
    return

# save file
def Save_file(MainWindow, self):
    try:
        title = MainWindow.windowTitle()
        title = title.replace("CAKE-EDITOR - ", "")
        if title == "":
            if self.CodeLanguage_comboBox.currentText() == "Python":
                fileName, _ = QFileDialog.getSaveFileName(MainWindow, "Save Code File", "", "Python (*.py)")
            elif self.CodeLanguage_comboBox.currentText() == "java":
                fileName, _ = QFileDialog.getSaveFileName(MainWindow, "Save Code File", "", "Java (*.java)")
            elif self.CodeLanguage_comboBox.currentText() == "Lua":
                fileName, _ = QFileDialog.getOpenFileName(MainWindow, "Save Code File", "", "Lua (*.lua)") 

            if fileName:
                path = str(fileName)
            else:
                return
            # get code from CodeEditor_plainTextEdit
            code = self.CodeEditor_plainTextEdit.toPlainText()
            # save code to file
            with open(fileName, "w") as file:
                file.write(code)
            file.close()
            return
        else:
            # get code from CodeEditor_plainTextEdit
            code = self.CodeEditor_plainTextEdit.toPlainText()
            # save code to file
            with open(title, "w") as file:
                file.write(code)
            file.close()
            return
    except Exception as e:
        msg(self, e)

# open file
def Open_file(MainWindow, self):
    try:
        if self.CodeLanguage_comboBox.currentText() == "Python":
            fileName, _ = QFileDialog.getOpenFileName(MainWindow, "Open Code File", "", "Python (*.py)") 
        elif self.CodeLanguage_comboBox.currentText() == "Java":
            fileName, _ = QFileDialog.getOpenFileName(MainWindow, "Open Code File", "", "Java (*.java)")  
        elif self.CodeLanguage_comboBox.currentText() == "Lua":
            fileName, _ = QFileDialog.getOpenFileName(MainWindow, "Open Code File", "", "Lua (*.lua)") 
        if fileName:
            path = str(fileName)
        else:
            return
        # read code from file
        with open(fileName, "r") as file:
            code = file.read()
        file.close()
        # write code to ui
        code = str(code)
        self.CodeEditor_plainTextEdit.clear()
        self.CodeEditor_plainTextEdit.appendPlainText(code)
        MainWindow.setWindowTitle("CAKE-EDITOR - "+fileName)
        return
    except Exception as e:
        msg(self, e)

# auto indent 
def Auto_indent(self):
    try:
        if self.CodeEditor_plainTextEdit.toPlainText().endswith(':\n') and self.AutoIndent_checkBox.isChecked():
            self.CodeEditor_plainTextEdit.insertPlainText('    ')
    except Exception as e:
        msg(self, e)

# get python.exe location
def GetCompilerLocation(MainWindow, self):
    try:
        fileName, _ = QFileDialog.getOpenFileName(MainWindow, "Find Language Compiler", "", "Exec. (*.exe)")  
        if fileName:
            pass
        else:
            return
        # save path
        self.LanguagePathlineEdit.setText(fileName)
        return
    except Exception as e:
        msg(self, e)

# run code
def RunCode(MainWindow, self):
    try:
        title = MainWindow.windowTitle()
        title = title.replace("CAKE-EDITOR - ", "")
        if title == "":
            if self.CodeLanguage_comboBox.currentText() == "Python":
                TempCode = upper_dir+"/temp/code.py"
            elif self.CodeLanguage_comboBox.currentText() == "Java":
                TempCode = upper_dir+"/temp/code.java"
            elif self.CodeLanguage_comboBox.currentText() == "Lua":
                TempCode = upper_dir+"/temp/code.lua"

            timer = upper_dir+"/functions/time.bat"
            LanguageLocation = str(self.LanguagePathlineEdit.text())
            #get code
            code = self.CodeEditor_plainTextEdit.toPlainText()
            # save code in a temp file.
            with open(TempCode, "w") as file:
                file.write(code)
            file.close()
            #run code in cmd
            os.system(f"""\
start cmd.exe /k {timer} {LanguageLocation} {TempCode}
""")
            return 
        else:
            timer = upper_dir+"/functions/time.bat"
            LanguageLocation = str(self.LanguagePathlineEdit.text())
            #run code in cmd
            os.system(f'start cmd.exe /k {timer} {LanguageLocation} {title} pause')
            return
    except Exception as e:
        msg(self, e)

# show hide dockWidget
def ShowHide_dockWidget(MainWindow,self):
    if self.dockWidget.isHidden():
        self.dockWidget.show()
        return
    else:
        self.dockWidget.hide()
        return
    
# reset Syntax color
def ResetSyntaxColor(MainWindow,self):
    try:
        self.KeywordColorChnage_btn.setStyleSheet(f"background-color: rgb(0, 255, 0);")
        self.OperatorColorChnage_btn.setStyleSheet(f"background-color: rgb(150, 150, 150);")
        self.BraceColorChnage_btn.setStyleSheet(f"background-color: rgb(93, 92, 91);")
        self.DefClassColorChnage_btn.setStyleSheet(f"background-color: rgb(255, 255, 204);")
        self.StringColorChnage_btn.setStyleSheet(f"background-color: rgb(51, 255, 255);")
        self.String2ColorChnage_btn.setStyleSheet(f"background-color: rgb(30, 120, 110);")
        self.CommentColorChnage_btn.setStyleSheet(f"background-color: rgb(128, 128, 128);")
        self.SelfColorChnage_btn.setStyleSheet(f"background-color: rgb(255, 0, 255);")
        self.NummbersColorChnage_btn.setStyleSheet(f"background-color: rgb(0, 204, 102);")
        return
    except Exception as e:
        msg(self, e) 




# SETTINGS
# apply settings
def Save_settings(MainWindow, self):
    #try:
        settings = upper_dir+"/settings/config.ini"
        config = configparser.ConfigParser()
        config.read(settings)
        # get auto indent state
        if self.AutoIndent_checkBox.isChecked(): Autoindent = True
        else: Autoindent = False
        # define
        config['-settings-']['theme'] = str(self.Themes_comboBox.currentText().replace("-", "_"))
        config['-settings-']['language'] = str(self.CodeLanguage_comboBox.currentText())
        config['-settings-']['AutoIndent'] = str(Autoindent)
        if self.CodeLanguage_comboBox.currentText() == "Python":
            language = "Python"
            if self.label_4.text() == "Python.exe location":
                config['-settings-']['PythonPath'] = str(self.LanguagePathlineEdit.text())
        elif self.CodeLanguage_comboBox.currentText() == "Java":
            language = "Java"
            if self.label_4.text() == "Java.exe location":
                config['-settings-']['JavaPath'] = str(self.LanguagePathlineEdit.text())
        elif self.CodeLanguage_comboBox.currentText() == "Lua":
            language = "Lua"
            if self.label_4.text() == "Lua.exe location":
                config['-settings-']['LuaPath'] = str(self.LanguagePathlineEdit.text())

        ## color buttons
        config['-color-']['KeywordColorChnage'] = str(self.KeywordColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        config['-color-']['OperatorColorChnage'] = str(self.OperatorColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        config['-color-']['BraceColorChnage'] = str(self.BraceColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        config['-color-']['DefClassColorChnage'] = str(self.DefClassColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        config['-color-']['StringColorChnage'] = str(self.StringColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        config['-color-']['String2ColorChnage'] = str(self.String2ColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        config['-color-']['CommentColorChnage'] = str(self.CommentColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        config['-color-']['SelfColorChnage'] = str(self.SelfColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        config['-color-']['NummbersColorChnage'] = str(self.NummbersColorChnage_btn.palette().button().color().getRgb()).replace(", 255)", "").replace("(","")
        # save settings
        with open(settings, 'w') as file: # save
            config.write(file)
        # get theme
        user_theme = self.Themes_comboBox.currentText().replace("-", "_")
        # get paths
        PythonPath = config.get('-settings-', 'PythonPath')
        JavaPath = config.get('-settings-', 'JavaPath')
        LuaPath = config.get('-settings-', 'LuaPath')
        # apply text, theme, ...
        apply_stylesheet(MainWindow, theme=upper_dir+"/themes/"+user_theme+".xml")
        if language == "Python":
            self.label_4.setText("Python.exe location")
            self.LanguagePathlineEdit.setText(PythonPath)
            self.CodeEditor_plainTextEdit.setPlaceholderText(example_codePY)
        elif language == "Java":
            self.label_4.setText("Java.exe location")
            self.LanguagePathlineEdit.setText(JavaPath)
            self.CodeEditor_plainTextEdit.setPlaceholderText(example_codeJ)
        elif language == "Lua":
            self.label_4.setText("Lua.exe location")
            self.LanguagePathlineEdit.setText(LuaPath)
            self.CodeEditor_plainTextEdit.setPlaceholderText(example_codeLua)
        return
    #except Exception as e:
    #    msg(self, e)


def Load_settings(MainWindow, self):
    try:
        settings = upper_dir+"/settings/config.ini"
        config = configparser.ConfigParser()
        config.read(settings)
        # load settings
        theme = config.get('-settings-', 'theme')
        language = config.get('-settings-', 'language')
        Autoindent = config.get('-settings-', 'AutoIndent')
        PythonPath = config.get('-settings-', 'PythonPath')
        JavaPath = config.get('-settings-', 'JavaPath')
        LuaPath = config.get('-settings-', 'LuaPath')
        if Autoindent == "True":
            Autoindent = True
        else:
            Autoindent = False
        # apply settings
        # theme
        apply_stylesheet(MainWindow, theme=upper_dir+"/themes/"+theme+".xml")
        self.Themes_comboBox.setCurrentText((theme.replace(".xml", "").replace("_", "-")))
        # coding language
        self.CodeLanguage_comboBox.setCurrentText(language)
        # auto Indent
        self.AutoIndent_checkBox.setChecked(Autoindent)
        # set text- background
        self.LanguagePathlineEdit.setText(" ")
        if language == "Python":
            self.label_4.setText("Python.exe location")
            self.LanguagePathlineEdit.setText(PythonPath)
            self.CodeEditor_plainTextEdit.setPlaceholderText(example_codePY)
        elif language == "Java":
            self.label_4.setText("Java.exe location")
            self.LanguagePathlineEdit.setText(JavaPath)
            self.CodeEditor_plainTextEdit.setPlaceholderText(example_codeJ)
        elif language == "Lua":
            self.label_4.setText("Lua.exe location")
            self.LanguagePathlineEdit.setText(LuaPath)
            self.CodeEditor_plainTextEdit.setPlaceholderText(example_codeLua)

        ## get button colors
        KeywordColorChnage = config.get('-color-', 'KeywordColorChnage')
        OperatorColorChnage = config.get('-color-', 'OperatorColorChnage')
        BraceColorChnage = config.get('-color-', 'BraceColorChnage')
        DefClassColorChnage = config.get('-color-', 'DefClassColorChnage')
        StringColorChnage = config.get('-color-', 'StringColorChnage')
        String2ColorChnage = config.get('-color-', 'String2ColorChnage')
        CommentColorChnage = config.get('-color-', 'CommentColorChnage')
        SelfColorChnage = config.get('-color-', 'SelfColorChnage')
        NummbersColorChnage = config.get('-color-', 'NummbersColorChnage')
        ## set button colors
        self.KeywordColorChnage_btn.setStyleSheet(f"background-color: rgb({KeywordColorChnage});")
        self.OperatorColorChnage_btn.setStyleSheet(f"background-color: rgb({OperatorColorChnage});")
        self.BraceColorChnage_btn.setStyleSheet(f"background-color: rgb({BraceColorChnage});")
        self.DefClassColorChnage_btn.setStyleSheet(f"background-color: rgb({DefClassColorChnage});")
        self.StringColorChnage_btn.setStyleSheet(f"background-color: rgb({StringColorChnage});")
        self.String2ColorChnage_btn.setStyleSheet(f"background-color: rgb({String2ColorChnage});")
        self.CommentColorChnage_btn.setStyleSheet(f"background-color: rgb({CommentColorChnage});")
        self.SelfColorChnage_btn.setStyleSheet(f"background-color: rgb({SelfColorChnage});")
        self.NummbersColorChnage_btn.setStyleSheet(f"background-color: rgb({NummbersColorChnage});")
        return
    except Exception as e:
        msg(self, e)

