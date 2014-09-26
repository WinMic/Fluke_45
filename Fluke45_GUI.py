# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fluke45_GUI.ui'
#
# Created: Fri Sep 26 16:27:59 2014
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
        Fluke45_GUI.resize(588, 546)
        self.centralwidget = QtGui.QWidget(Fluke45_GUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.groupBox_Input = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Input.setObjectName(_fromUtf8("groupBox_Input"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_Input)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_IDN = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_IDN.setObjectName(_fromUtf8("pushButton_IDN"))
        self.gridLayout.addWidget(self.pushButton_IDN, 0, 0, 1, 1)
        self.pushButton_VAL = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_VAL.setObjectName(_fromUtf8("pushButton_VAL"))
        self.gridLayout.addWidget(self.pushButton_VAL, 1, 0, 1, 1)
        self.pushButton_exit = QtGui.QPushButton(self.groupBox_Input)
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.gridLayout.addWidget(self.pushButton_exit, 2, 0, 1, 1)
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.groupBox_Input)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_COM = QtGui.QComboBox(self.groupBox)
        self.comboBox_COM.setObjectName(_fromUtf8("comboBox_COM"))
        self.horizontalLayout.addWidget(self.comboBox_COM)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.groupBox)
        self.groupBox_Output = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Output.setObjectName(_fromUtf8("groupBox_Output"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_Output)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textBrowser_Output = QtGui.QTextBrowser(self.groupBox_Output)
        self.textBrowser_Output.setObjectName(_fromUtf8("textBrowser_Output"))
        self.horizontalLayout_2.addWidget(self.textBrowser_Output)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.groupBox_Output)
        Fluke45_GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Fluke45_GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 18))
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
        self.groupBox.setTitle(_translate("Fluke45_GUI", "Einstellungen", None))
        self.label.setText(_translate("Fluke45_GUI", "COM-Port", None))
        self.groupBox_Output.setTitle(_translate("Fluke45_GUI", "Output", None))

