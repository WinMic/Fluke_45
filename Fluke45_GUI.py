# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fluke45_GUI.ui'
#
# Created: Sat Oct 11 12:04:46 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Fluke45_GUI(object):
    def setupUi(self, Fluke45_GUI):
        Fluke45_GUI.setObjectName(_fromUtf8("Fluke45_GUI"))
        Fluke45_GUI.resize(698, 626)
        self.centralwidget = QtGui.QWidget(Fluke45_GUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_Output = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Output.setObjectName(_fromUtf8("groupBox_Output"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_Output)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textBrowser_Output = QtGui.QTextBrowser(self.groupBox_Output)
        self.textBrowser_Output.setEnabled(True)
        self.textBrowser_Output.setReadOnly(True)
        self.textBrowser_Output.setObjectName(_fromUtf8("textBrowser_Output"))
        self.horizontalLayout_2.addWidget(self.textBrowser_Output)
        self.gridLayout_3.addWidget(self.groupBox_Output, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_DEBUG = QtGui.QLabel(self.groupBox)
        self.label_DEBUG.setObjectName(_fromUtf8("label_DEBUG"))
        self.gridLayout_2.addWidget(self.label_DEBUG, 1, 0, 1, 1)
        self.checkBox_DEBUG = QtGui.QCheckBox(self.groupBox)
        self.checkBox_DEBUG.setText(_fromUtf8(""))
        self.checkBox_DEBUG.setObjectName(_fromUtf8("checkBox_DEBUG"))
        self.gridLayout_2.addWidget(self.checkBox_DEBUG, 1, 1, 1, 1)
        self.label_COM = QtGui.QLabel(self.groupBox)
        self.label_COM.setObjectName(_fromUtf8("label_COM"))
        self.gridLayout_2.addWidget(self.label_COM, 0, 0, 1, 1)
        self.comboBox_COM = QtGui.QComboBox(self.groupBox)
        self.comboBox_COM.setObjectName(_fromUtf8("comboBox_COM"))
        self.gridLayout_2.addWidget(self.comboBox_COM, 0, 1, 1, 1)
        self.pushButton_RESET = QtGui.QPushButton(self.groupBox)
        self.pushButton_RESET.setObjectName(_fromUtf8("pushButton_RESET"))
        self.gridLayout_2.addWidget(self.pushButton_RESET, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.pushButton_EXIT = QtGui.QPushButton(self.groupBox)
        self.pushButton_EXIT.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pushButton_EXIT.setObjectName(_fromUtf8("pushButton_EXIT"))
        self.gridLayout_2.addWidget(self.pushButton_EXIT, 4, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_Input = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Input.setObjectName(_fromUtf8("groupBox_Input"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_Input)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_VAL = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_VAL.setObjectName(_fromUtf8("pushButton_VAL"))
        self.gridLayout.addWidget(self.pushButton_VAL, 1, 0, 1, 1)
        self.pushButton_USERINPUT = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_USERINPUT.setObjectName(_fromUtf8("pushButton_USERINPUT"))
        self.gridLayout.addWidget(self.pushButton_USERINPUT, 3, 0, 1, 1)
        self.lineEdit_USERINPUT = QtGui.QLineEdit(self.groupBox_Input)
        self.lineEdit_USERINPUT.setEnabled(True)
        self.lineEdit_USERINPUT.setObjectName(_fromUtf8("lineEdit_USERINPUT"))
        self.gridLayout.addWidget(self.lineEdit_USERINPUT, 3, 2, 1, 1)
        self.pushButton_IDN = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_IDN.setObjectName(_fromUtf8("pushButton_IDN"))
        self.gridLayout.addWidget(self.pushButton_IDN, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_Input, 1, 0, 1, 1)
        Fluke45_GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Fluke45_GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Fluke45_GUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Fluke45_GUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Fluke45_GUI.setStatusBar(self.statusbar)

        self.retranslateUi(Fluke45_GUI)
        QtCore.QMetaObject.connectSlotsByName(Fluke45_GUI)

    def retranslateUi(self, Fluke45_GUI):
        Fluke45_GUI.setWindowTitle(_translate("Fluke45_GUI", "MainWindow", None))
        self.groupBox_Output.setTitle(_translate("Fluke45_GUI", "Output", None))
        self.groupBox.setTitle(_translate("Fluke45_GUI", "Einstellungen", None))
        self.label_DEBUG.setText(_translate("Fluke45_GUI", "Debug Nachrichten", None))
        self.label_COM.setText(_translate("Fluke45_GUI", "COM-Port", None))
        self.pushButton_RESET.setText(_translate("Fluke45_GUI", "Reset Fluke", None))
        self.label.setText(_translate("Fluke45_GUI", "Reset Fluke45", None))
        self.pushButton_EXIT.setText(_translate("Fluke45_GUI", "Beenden", None))
        self.groupBox_Input.setTitle(_translate("Fluke45_GUI", "Input", None))
        self.pushButton_VAL.setText(_translate("Fluke45_GUI", "Value", None))
        self.pushButton_USERINPUT.setText(_translate("Fluke45_GUI", "BenutzerEingabe", None))
        self.pushButton_IDN.setText(_translate("Fluke45_GUI", "Identify", None))

