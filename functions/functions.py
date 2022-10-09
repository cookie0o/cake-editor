from PyQt5.QtWidgets import QInputDialog, QFileDialog, QCompleter
from qt_material import apply_stylesheet
import configparser
import keyboard
import time
import os

# upper dir
upper_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

# error or info message I dont know why you ask me read the code
def msg(self, text):
    msg.setIcon(QMessageBox.Critical)
    msg.setText("information / error")
    msg.setWindowTitle(text)
    return

# save file
def Save_file(MainWindow, self):
    try:
        title = MainWindow.windowTitle()
        title = title.replace("CAKE-EDITOR - ", "")
        if title == "":
            fileName, _ = QFileDialog.getSaveFileName(MainWindow, "Save Code File", "", "Python (*.py)")
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
        fileName, _ = QFileDialog.getOpenFileName(MainWindow, "Open Code File", "", "Python (*.py)")  
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
        return
    except Exception as e:
        msg(self, e)

# get python.exe location
def GetPythonLocation(MainWindow, self):
    try:
        fileName, _ = QFileDialog.getOpenFileName(MainWindow, "Find Python", "", "Exec. (*.exe)")  
        if fileName:
            path = str(fileName)
        else:
            return
        # save path
        self.PythonPathlineEdit.setText(fileName)
        return
    except Exception as e:
        msg(self, e)

# run code
def RunCode(MainWindow, self):
    try:
        title = MainWindow.windowTitle()
        title = title.replace("CAKE-EDITOR - ", "")
        if title == "":
            TempCode = upper_dir+"/temp/code.py"
            PythonLocation = str(self.PythonPathlineEdit.text())
            #get code
            code = self.CodeEditor_plainTextEdit.toPlainText()
            # save code in a temp file.
            with open(TempCode, "w") as file:
                file.write(code)
            file.close()
            #run code in cmd
            os.system(f'start cmd.exe /k "{PythonLocation} {TempCode} pause"')
            return 
        else:
            PythonLocation = str(self.PythonPathlineEdit.text())
            #run code in cmd
            os.system(f'start cmd.exe /k "{PythonLocation} {title} pause"')
            return
    except Exception as e:
        msg(self, e)
    


# SETTINGS
# apply settings
def Save_settings(MainWindow, self):
    try:
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
        config['-settings-']['PythonPath'] = str(self.PythonPathlineEdit.text())
        # save settings
        with open(settings, 'w') as file: # save
            config.write(file)
        # apply settings
        # get theme
        user_theme = self.Themes_comboBox.currentText().replace("-", "_")
        # apply selected theme
        apply_stylesheet(MainWindow, theme=upper_dir+"/themes/"+user_theme+".xml")
        return
    except Exception as e:
        msg(self, e)


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
        if Autoindent == "True":
            Autoindent = True
        else:
            Autoindent = False
        # apply settings
        # theme
        self.Themes_comboBox.setCurrentText(theme)
        apply_stylesheet(MainWindow, theme=upper_dir+"/themes/"+theme+".xml")
        # coding language
        self.CodeLanguage_comboBox.setCurrentText(language)
        # auto Indent
        self.AutoIndent_checkBox.setChecked(Autoindent)
        # python path
        self.PythonPathlineEdit.setText(PythonPath)
        return
    except Exception as e:
        msg(self, e)

