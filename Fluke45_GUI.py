# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fluke45_GUI.ui'
#
# Created: Thu Sep 18 16:01:30 2014
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
        Fluke45_GUI.resize(385, 294)
        self.centralwidget = QtGui.QWidget(Fluke45_GUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_Input = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Input.setObjectName(_fromUtf8("groupBox_Input"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_Input)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_IDN = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_IDN.setObjectName(_fromUtf8("pushButton_IDN"))
        self.verticalLayout.addWidget(self.pushButton_IDN)
        self.pushButton_VAL = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_VAL.setObjectName(_fromUtf8("pushButton_VAL"))
        self.verticalLayout.addWidget(self.pushButton_VAL)
        self.pushButton_exit = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.verticalLayout.addWidget(self.pushButton_exit)
        self.horizontalLayout.addWidget(self.groupBox_Input)
        self.groupBox_Output = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Output.setObjectName(_fromUtf8("groupBox_Output"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_Output)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textBrowser_Output = QtGui.QTextBrowser(self.groupBox_Output)
        self.textBrowser_Output.setObjectName(_fromUtf8("textBrowser_Output"))
        self.horizontalLayout_2.addWidget(self.textBrowser_Output)
        self.horizontalLayout.addWidget(self.groupBox_Output)
        Fluke45_GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Fluke45_GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 385, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Fluke45_GUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Fluke45_GUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Fluke45_GUI.setStatusBar(self.statusbar)

        self.retranslateUi(Fluke45_GUI)
        QtCore.QMetaObject.connectSlotsByName(Fluke45_GUI)

    def retranslateUi(self, Fluke45_GUI):
        Fluke45_GUI.setWindowTitle(_translate("Fluke45_GUI", "MainWindow", None))
        self.groupBox_Input.setTitle(_translate("Fluke45_GUI", "Input", None))
        self.pushButton_IDN.setText(_translate("Fluke45_GUI", "Identify", None))
        self.pushButton_VAL.setText(_translate("Fluke45_GUI", "Value", None))
        self.pushButton_exit.setText(_translate("Fluke45_GUI", "Beenden", None))
        self.groupBox_Output.setTitle(_translate("Fluke45_GUI", "Output", None))

