# Imports
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

# import Highlighting
from highlighting.highlighting import *
# import functions
from functions.functions import *
# import example code
from examples.example_code import example_code


# current dir
current_dir = os.path.dirname(os.path.realpath(__file__))


# Ui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # set size and lock it
        MainWindow.resize(870, 480)
        MainWindow.setMinimumSize(870, 480)
        MainWindow.setMaximumSize(870, 480)
        font = QtGui.QFont()
        # Ui content
        self.SaveFile_btn = QtWidgets.QPushButton(MainWindow)
        self.SaveFile_btn.setGeometry(QtCore.QRect(50, 2, 30, 30))
        self.SaveFile_btn.setText("")
        self.SaveFile_btn.setFlat(True)
        self.SaveFile_btn.setObjectName("SaveFile_btn")
        self.OpenFile_btn = QtWidgets.QPushButton(MainWindow)
        self.OpenFile_btn.setGeometry(QtCore.QRect(10, 2, 30, 30))
        self.OpenFile_btn.setText("")
        self.OpenFile_btn.setFlat(True)
        self.OpenFile_btn.setObjectName("OpenFile_btn")
        self.Settings_btn = QtWidgets.QPushButton(MainWindow)
        self.Settings_btn.setGeometry(QtCore.QRect(90, 2, 30, 30))
        self.Settings_btn.setText("")
        self.Settings_btn.setFlat(True)
        self.Settings_btn.setObjectName("Settings_btn")
        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(5, 40, 850, 430))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Editor_page = QtWidgets.QWidget()
        self.Editor_page.setObjectName("Editor_page")
        self.CodeEditor_plainTextEdit = QtWidgets.QPlainTextEdit(self.Editor_page)
        self.CodeEditor_plainTextEdit.setGeometry(QtCore.QRect(0, 0, 851, 431))
        font = QtGui.QFont("Times",0,QFont.Bold)
        self.CodeEditor_plainTextEdit.setFont(font)
        self.CodeEditor_plainTextEdit.setObjectName("CodeEditor_plainTextEdit")
        self.stackedWidget.addWidget(self.Editor_page)
        self.Settings_page = QtWidgets.QWidget()
        self.Settings_page.setObjectName("Settings_page")
        self.label = QtWidgets.QLabel(self.Settings_page)
        self.label.setGeometry(QtCore.QRect(5, 0, 130, 20))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Themes_comboBox = QtWidgets.QComboBox(self.Settings_page)
        self.Themes_comboBox.setGeometry(QtCore.QRect(5, 20, 130, 20))
        self.Themes_comboBox.setObjectName("Themes_comboBox")
        self.Save_btn = QtWidgets.QPushButton(self.Settings_page)
        self.Save_btn.setGeometry(QtCore.QRect(5, 400, 90, 30))
        self.Save_btn.setObjectName("Save_btn")
        self.Back_btn = QtWidgets.QPushButton(self.Settings_page)
        self.Back_btn.setGeometry(QtCore.QRect(110, 400, 100, 30))
        self.Back_btn.setObjectName("Back_btn")
        self.label_3 = QtWidgets.QLabel(self.Settings_page)
        self.label_3.setGeometry(QtCore.QRect(5, 50, 130, 20))
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.CodeLanguage_comboBox = QtWidgets.QComboBox(self.Settings_page)
        self.CodeLanguage_comboBox.setGeometry(QtCore.QRect(5, 70, 130, 20))
        self.CodeLanguage_comboBox.setObjectName("CodeLanguage_comboBox")
        self.AutoIndent_checkBox = QtWidgets.QCheckBox(self.Settings_page)
        self.AutoIndent_checkBox.setGeometry(QtCore.QRect(5, 105, 130, 20))
        font.setPointSize(10)
        self.AutoIndent_checkBox.setFont(font)
        self.AutoIndent_checkBox.setObjectName("AutoIndent_checkBox")
        self.label_4 = QtWidgets.QLabel(self.Settings_page)
        self.label_4.setGeometry(QtCore.QRect(5, 340, 130, 20))
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.PythonPathlineEdit = QtWidgets.QLineEdit(self.Settings_page)
        self.PythonPathlineEdit.setGeometry(QtCore.QRect(5, 360, 350, 20))
        self.PythonPathlineEdit.setObjectName("PythonPathlineEdit")
        self.GetPythonLocation_btn = QtWidgets.QPushButton(self.Settings_page)
        self.GetPythonLocation_btn.setGeometry(QtCore.QRect(360, 355, 30, 30))
        self.GetPythonLocation_btn.setAutoFillBackground(False)
        self.GetPythonLocation_btn.setText("")
        self.GetPythonLocation_btn.setFlat(True)
        self.GetPythonLocation_btn.setObjectName("GetPythonLocation_btn")
        self.stackedWidget.addWidget(self.Settings_page)
        self.Run_btn = QtWidgets.QPushButton(MainWindow)
        self.Run_btn.setGeometry(QtCore.QRect(825, 2, 30, 30))
        self.Run_btn.setText("")
        self.Run_btn.setFlat(True)
        self.Run_btn.setObjectName("Run_btn")

        # icon paths
        save_file = QIcon(current_dir+"/res/save_file.png")
        open_file = QIcon(current_dir+"/res/open_file.png")
        settings  = QIcon(current_dir+"/res/settings.png")
        find_Python  = QIcon(current_dir+"/res/open_file.png")
        run_code = QIcon(current_dir+"/res/run.png")

        # apply icons to buttons
        self.OpenFile_btn.setIcon(open_file)
        self.SaveFile_btn.setIcon(save_file)
        self.Settings_btn.setIcon(settings)
        self.GetPythonLocation_btn.setIcon(find_Python)
        self.Run_btn.setIcon(run_code)

        # default stuff
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # add themes to combobox
        for file in os.listdir(current_dir+"/themes/"):
            file = file.replace(".xml", "").replace("_", "-")
            self.Themes_comboBox.addItem(file)
        # highlighting
        self.highlight = PythonHighlighter(self.CodeEditor_plainTextEdit.document())
        # code language
        self.CodeLanguage_comboBox.addItem("Python")
        # auto line indent
        self.CodeEditor_plainTextEdit.textChanged.connect(lambda: Auto_indent(self))
        # load settings
        Load_settings(MainWindow, self)



        # button actions
        class BTN_actions():
            # open file button
            self.OpenFile_btn.clicked.connect(lambda: Open_file(MainWindow, self))
            # save file button
            self.SaveFile_btn.clicked.connect(lambda: Save_file(MainWindow,self))
            # settings button
            self.Settings_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
            ##### save button
            self.Save_btn.clicked.connect(lambda: Save_settings(MainWindow, self))
            ##### back button
            self.Back_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
            # get Python.exe buttom
            self.GetPythonLocation_btn.clicked.connect(lambda: GetPythonLocation(MainWindow, self))
            # run code button
            self.Run_btn.clicked.connect(lambda: RunCode(MainWindow, self))


    # Ui text
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.CodeEditor_plainTextEdit.setPlaceholderText(_translate("MainWindow", example_code))
        self.AutoIndent_checkBox.setText(_translate("MainWindow", "Auto indent"))
        self.label_3.setText(_translate("MainWindow", "Editor Code Language:"))
        self.label_4.setText(_translate("MainWindow", "Python.exe location"))
        self.label.setText(_translate("MainWindow", "Editor Theme:"))
        self.Save_btn.setText(_translate("MainWindow", "Save"))
        self.Back_btn.setText(_translate("MainWindow", "Back"))

# Run Ui
if __name__ == "__main__":
    # Handle high resolution displays:
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    # build ui
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # set window title
    MainWindow.setWindowTitle("CAKE-EDITOR - ")
    sys.exit(app.exec_())

