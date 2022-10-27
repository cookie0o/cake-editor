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
from examples.example_code import *


# current dir
current_dir = os.path.dirname(os.path.realpath(__file__))


# Ui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon(current_dir+"/res/ico.ico"))
        # set size and lock it
        MainWindow.resize(870, 480)
        MainWindow.setMinimumSize(870, 480)
        MainWindow.setMaximumSize(870, 480)
        font = QtGui.QFont()
        # Ui content
        self.SaveFile_btn = QtWidgets.QPushButton(MainWindow)
        self.SaveFile_btn.setGeometry(QtCore.QRect(50, 5, 30, 30))
        self.SaveFile_btn.setText("")
        self.SaveFile_btn.setFlat(True)
        self.SaveFile_btn.setObjectName("SaveFile_btn")
        self.OpenFile_btn = QtWidgets.QPushButton(MainWindow)
        self.OpenFile_btn.setGeometry(QtCore.QRect(10, 5, 30, 30))
        self.OpenFile_btn.setText("")
        self.OpenFile_btn.setFlat(True)
        self.OpenFile_btn.setObjectName("OpenFile_btn")
        self.Settings_btn = QtWidgets.QPushButton(MainWindow)
        self.Settings_btn.setGeometry(QtCore.QRect(90, 5, 30, 30))
        self.Settings_btn.setText("")
        self.Settings_btn.setFlat(True)
        self.Settings_btn.setObjectName("Settings_btn")
        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(5, 40, 850, 430))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Editor_page = QtWidgets.QWidget()
        self.Editor_page.setObjectName("Editor_page")
        self.CodeEditor_plainTextEdit = QtWidgets.QPlainTextEdit(self.Editor_page)
        self.CodeEditor_plainTextEdit.setGeometry(QtCore.QRect(0, 0, 850, 430))
        font.setPointSize(10)
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
        self.AutoIndent_checkBox.setGeometry(QtCore.QRect(1, 100, 130, 20))
        font.setPointSize(10)
        self.AutoIndent_checkBox.setFont(font)
        self.AutoIndent_checkBox.setObjectName("AutoIndent_checkBox")
        self.label_4 = QtWidgets.QLabel(self.Settings_page)
        self.label_4.setGeometry(QtCore.QRect(5, 340, 130, 20))
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.LanguagePathlineEdit = QtWidgets.QLineEdit(self.Settings_page)
        self.LanguagePathlineEdit.setGeometry(QtCore.QRect(5, 360, 350, 20))
        self.LanguagePathlineEdit.setObjectName("LanguagePathlineEdit")
        self.GetPythonLocation_btn = QtWidgets.QPushButton(self.Settings_page)
        self.GetPythonLocation_btn.setGeometry(QtCore.QRect(360, 355, 30, 30))
        self.GetPythonLocation_btn.setAutoFillBackground(False)
        self.GetPythonLocation_btn.setText("")
        self.GetPythonLocation_btn.setFlat(True)
        self.GetPythonLocation_btn.setObjectName("GetPythonLocation_btn")
        self.label_5 = QtWidgets.QLabel(self.Settings_page)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 150, 20))
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dockWidget = QtWidgets.QDockWidget(self.Settings_page)
        self.dockWidget.setGeometry(QtCore.QRect(340, 200, 500, 180))
        self.dockWidget.setMinimumSize(QtCore.QSize(185, 180))
        self.dockWidget.setMaximumSize(QtCore.QSize(185, 180))
        self.dockWidget.setFloating(True)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidget.setWindowTitle("color Picker")
        self.dockWidget.setWindowIcon(QIcon(current_dir+"/res/ico.ico"))
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        # hide Syntax color changing window on start
        self.dockWidget.hide()
        #
        self.label_15 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 110, 20))
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(0, 30, 110, 20))
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_18.setGeometry(QtCore.QRect(0, 120, 110, 20))
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_19.setGeometry(QtCore.QRect(100, 90, 110, 20))
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_20.setGeometry(QtCore.QRect(0, 90, 110, 20))
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_21.setGeometry(QtCore.QRect(100, 60, 110, 20))
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_22.setGeometry(QtCore.QRect(0, 60, 110, 20))
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_23.setGeometry(QtCore.QRect(100, 30, 110, 20))
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.KeywordColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.KeywordColorChnage_btn.setGeometry(QtCore.QRect(70, 0, 20, 20))
        self.KeywordColorChnage_btn.setText("")
        self.KeywordColorChnage_btn.setObjectName("KeywordColorChnage_btn")
        self.OperatorColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.OperatorColorChnage_btn.setGeometry(QtCore.QRect(160, 0, 20, 20))
        self.OperatorColorChnage_btn.setText("")
        self.OperatorColorChnage_btn.setObjectName("OperatorColorChnage_btn")
        self.BraceColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.BraceColorChnage_btn.setGeometry(QtCore.QRect(70, 30, 20, 20))
        self.BraceColorChnage_btn.setText("")
        self.BraceColorChnage_btn.setObjectName("BraceColorChnage_btn")
        self.DefClassColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.DefClassColorChnage_btn.setGeometry(QtCore.QRect(160, 30, 20, 20))
        self.DefClassColorChnage_btn.setText("")
        self.DefClassColorChnage_btn.setObjectName("DefClassColorChnage_btn")
        self.StringColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.StringColorChnage_btn.setGeometry(QtCore.QRect(70, 60, 20, 20))
        self.StringColorChnage_btn.setText("")
        self.StringColorChnage_btn.setObjectName("StringColorChnage_btn")
        self.String2ColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.String2ColorChnage_btn.setGeometry(QtCore.QRect(160, 60, 20, 20))
        self.String2ColorChnage_btn.setText("")
        self.String2ColorChnage_btn.setObjectName("String2ColorChnage_btn")
        self.CommentColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.CommentColorChnage_btn.setGeometry(QtCore.QRect(70, 90, 20, 20))
        self.CommentColorChnage_btn.setText("")
        self.CommentColorChnage_btn.setObjectName("CommentColorChnage_btn")
        self.SelfColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.SelfColorChnage_btn.setGeometry(QtCore.QRect(160, 90, 20, 20))
        self.SelfColorChnage_btn.setText("")
        self.SelfColorChnage_btn.setObjectName("SelfColorChnage_btn")
        self.NummbersColorChnage_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.NummbersColorChnage_btn.setGeometry(QtCore.QRect(70, 120, 20, 20))
        self.NummbersColorChnage_btn.setText("")
        self.NummbersColorChnage_btn.setObjectName("NummbersColorChnage_btn")
        self.label_24 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_24.setGeometry(QtCore.QRect(100, 0, 80, 20))
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.Reset_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.Reset_btn.setGeometry(QtCore.QRect(0, 150, 90, 30))
        self.Reset_btn.setObjectName("Reset_btn")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.ChangeSyntaxHighlightingColor = QtWidgets.QPushButton(self.Settings_page)
        self.ChangeSyntaxHighlightingColor.setGeometry(QtCore.QRect(5, 130, 20, 20))
        self.ChangeSyntaxHighlightingColor.setText("")
        self.ChangeSyntaxHighlightingColor.setFlat(True)
        self.ChangeSyntaxHighlightingColor.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.Settings_page)
        self.Run_btn = QtWidgets.QPushButton(MainWindow)
        self.Run_btn.setGeometry(QtCore.QRect(825, 5, 30, 30))
        self.Run_btn.setText("")
        self.Run_btn.setFlat(True)
        self.Run_btn.setObjectName("Run_btn")
        # icon paths
        ChangeSyntaxHighlightingColor = QIcon(current_dir+"/res/edit.png")
        find_Python  = QIcon(current_dir+"/res/open_file.png")
        save_file = QIcon(current_dir+"/res/save_file.png")
        open_file = QIcon(current_dir+"/res/open_file.png")
        settings  = QIcon(current_dir+"/res/settings.png")
        run_code = QIcon(current_dir+"/res/run.png")


        # apply icons to buttons
        self.ChangeSyntaxHighlightingColor.setIcon(ChangeSyntaxHighlightingColor)
        self.GetPythonLocation_btn.setIcon(find_Python)
        self.OpenFile_btn.setIcon(open_file)
        self.SaveFile_btn.setIcon(save_file)
        self.Settings_btn.setIcon(settings)
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
        languages = ["Python","Java","Lua"]
        for language in languages:
            self.CodeLanguage_comboBox.addItem(language)
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
            ##### show Syntax Color Changing Window
            self.ChangeSyntaxHighlightingColor.clicked.connect(lambda: ShowHide_dockWidget(MainWindow,self))
            ##### syntax color reset button
            self.Reset_btn.clicked.connect(lambda: ResetSyntaxColor(MainWindow,self))
            # get Python.exe buttom
            self.GetPythonLocation_btn.clicked.connect(lambda: GetCompilerLocation(MainWindow, self))
            # run code button
            self.Run_btn.clicked.connect(lambda: RunCode(MainWindow, self))   
            ## button color
            self.KeywordColorChnage_btn.clicked.connect(lambda: SelectColor(self,"KeywordColorChnage_btn")) 
            self.OperatorColorChnage_btn.clicked.connect(lambda: SelectColor(self,"OperatorColorChnage_btn")) 
            self.BraceColorChnage_btn.clicked.connect(lambda: SelectColor(self,"BraceColorChnage_btn")) 
            self.DefClassColorChnage_btn.clicked.connect(lambda: SelectColor(self,"DefClassColorChnage_btn")) 
            self.StringColorChnage_btn.clicked.connect(lambda: SelectColor(self,"StringColorChnage_btn")) 
            self.String2ColorChnage_btn.clicked.connect(lambda: SelectColor(self,"String2ColorChnage_btn")) 
            self.CommentColorChnage_btn.clicked.connect(lambda: SelectColor(self,"CommentColorChnage_btn"))
            self.SelfColorChnage_btn.clicked.connect(lambda: SelectColor(self,"SelfColorChnage_btn")) 
            self.NummbersColorChnage_btn.clicked.connect(lambda: SelectColor(self,"NummbersColorChnage_btn"))

     

    # Ui text
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.CodeEditor_plainTextEdit.setPlaceholderText(_translate("MainWindow", example_codePY))
        self.label_5.setText(_translate("MainWindow", "Syntax Highlighting color"))
        self.AutoIndent_checkBox.setText(_translate("MainWindow", "Auto indent"))
        self.label_3.setText(_translate("MainWindow", "Editor Code Language:"))
        self.label.setText(_translate("MainWindow", "Editor Theme:"))
        self.Save_btn.setText(_translate("MainWindow", "Save"))
        self.Back_btn.setText(_translate("MainWindow", "Back"))
        self.Reset_btn.setText(_translate("MainWindow", "Reset"))
        #####
        self.label_15.setText(_translate("MainWindow", "keyword"))
        self.label_24.setText(_translate("MainWindow", "operator"))
        self.label_17.setText(_translate("MainWindow", "brace"))
        self.label_18.setText(_translate("MainWindow", "nummbers"))
        self.label_19.setText(_translate("MainWindow", "self"))
        self.label_20.setText(_translate("MainWindow", "comment"))
        self.label_21.setText(_translate("MainWindow", "string2"))
        self.label_22.setText(_translate("MainWindow", "string"))
        self.label_23.setText(_translate("MainWindow", "defclass"))

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
