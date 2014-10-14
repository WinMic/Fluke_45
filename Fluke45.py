# -*- coding: utf-8 -*-
"""
Created on Tue Sep 02 08:48:12 2014

@author: Michael W.
"""
#Informationen
#Das Fluke45 sendet bei eingeschaltetem Echo Mode den gesendeten Befehl zurück
#Jede gesendete Zeile des Messgerätes endet mit einem CR und LF
#CR = Carriage Return, LF = Line Feed

######################    
#       MACROS       #
######################


#mit Baud 9600 können übertragungen länger dauern, als die Prüfung auf einen
#gefüllten Eingangspuffer. In diesem Fall wird nichts empfangen. 
USE_BAUD_DELAY = False  






#######################
#       IMPORTS       #
#######################    
import serial
import sys
import time


#Imports für die Gui

#TODO: Werden alle Imports benötigt?
from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import QMainWindow, QWidget, QVBoxLayout,QHBoxLayout,\
      QApplication,QComboBox, QPushButton, QLineEdit, QGridLayout, QLabel, \
      QLCDNumber, QColor, QPalette, QFrame, qApp, QIcon



#Importiere mir von Fluke45_GUI.py die Klasse Ui_Fluke45_GUI und wir nennen
#diese Klasse im anschluss nurnoch F45Gui
from Fluke45_GUI import Ui_Fluke45_GUI

#==============================================================================
# Erstellt die Gui
#==============================================================================
class makeGui(QtGui.QMainWindow, Ui_Fluke45_GUI): 
   
    
    def __init__(self): 
        """
        __init__ erstellt die Gui und verbindet die GUI-Elemente mit den
        Einzelnen Funktionen des Programmes
        
        Parameters
        ----------
        
        Self
        """
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
        #suche nach verfügbaren Comports und liste diese auf
        ValidComPorts = self.serialScan()
        for i in range(len(ValidComPorts)):
            self.comboBox_COM.addItem(ValidComPorts[i][1])
        
        #verbinde die Guielemente mit den Funktionen
        self.comboBox_COM.activated.connect(self.serialPort)
        self.pushButton_EXIT.clicked.connect(self.exitApp)
        self.pushButton_IDN.clicked.connect(lambda: self.serialSend("*IDN?\n"))
        self.pushButton_VAL.clicked.connect(lambda: self.serialSend("VAL?\n"))
        self.pushButton_RESET.clicked.connect(lambda: self.serialSend("*RST\n"))
        self.pushButton_USERINPUT.clicked.connect(lambda: self.serialSend(str(self.lineEdit_USERINPUT.text())+"\n"))
    
    def settext(self, Outputdata):
        """
        Schreibt die übergebenen Daten in das Textfeld der GUI
        
        Parameters
        ----------
        Self        
        
        """
        self.textBrowser_Output.append(str(Outputdata))



    def serialPort(self):
        """
        serialPort öffnet den COM-Port zum Fluke mit den standard RS-232 Einstellungen
        
        Parameters
        ----------
        self
        """
        self.Debug_Msg("Serialport")

        com = self.comboBox_COM.currentText()
        self.ser = serial.Serial(
                                 port=str(com),
                                 baudrate=9600,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS,
                                 timeout = 1
                                 )
        
        if(self.ser.isOpen() == False):
            self.Debug_Msg("COM ist nicht offen")
            try:
                self.ser.open()
                self.Debug_Msg("versuche COM zu oeffnen")
            except serial.SerialException:
                self.Debug_Msg("COM konnte nicht geoeffnet werden")
                self.settext("Ausgewaelter Port konnte nicht geoefnet werden")

    def serialScan(self):
        """
        Sucht nach verfügbaren Com-Ports und gibt diese in einer Liste zurück
        
        Parameters
        ----------
        self
        """

        ports = []
        for i in range(256):
            try:
                
    #Wenn der serielle Port NICHT geöfnet werden kann, wird eine Exception
    #"serial.SerialException" geschmissen. Diese wird abgefangen und die for-Schleife
    #läuft weiter OHNE dabei den nicht erreichbaren Port in die ports-Liste einzutragen            
                self.ser = serial.Serial(i)
                
    #Befülle dir Portliste mit den Com-Ports die geöfnet werden konnten
                ports.append([i, self.ser.portstr])
                self.ser.close()
            except serial.SerialException:
                pass
        return ports





###############################################################################
    def serialReadLine(self):
        """
        serialReadLine liest alle gesendeten Zeilen des Fluke45 solange bis das
        Messgerät den Sendebetrieb einstellt. Der Sendebetrieb ist vorbei, sobald
        das Messgerät ein Steuerzeichen ('=>' oder '?>' oder '!>') gefolgt von einem
        CR und LF (CR = Carriage Return, LF = Line Feed)
        
        Parameters
        ----------
        self
        """
        Value = []
        i=0
        while (i == 0):
            if (self.ser.inWaiting > 0):
                
                #Lese die nächste Zeile und füge die an die Liste "Value"
                #hinten an
                Value.append(self.ser.readline())
            
            #Ist das "Macro" USE_BAUD_DELAY True, dann lasse dir Zeit beim
            #überprüfen des Inputbuffers. 
            elif(USE_BAUD_DELAY):  
                
                #Da die Baud 9600 sehr langsam ist, muss gewartet werden ob 
                #doch etwas im Eingangspuffer liegt
                time.sleep(0.0625)   
                if (self.ser.inWaiting > 0):
                    
                    #Lese die nächste Zeile und füge die an die Liste "Value"
                    #hinten an
                    Value.append(self.ser.readline())

            #Prüfe ob das letzte Element in der "Value" Liste ein vom Fluke45
            #gesendetes Steuerzeichen ist.        
            if (Value != 0):
                
                #"=>\r\n" Steuerzeichen für Befehl verstanden, ausgeführt
                #und bereit für einen neuen Befehl
                if (Value[-1] == "=>\r\n"):
           
                    i = 1
                    self.Debug_Msg("Fluke45 hat Befehl verstanden u. ausgefuehrt")
                #"?>\r\n" Steuerzeichen für Befehlsfehler
                #Befehl wurde nicht verstanden.
                elif (Value[-1] == '?>\r\n'):
                    i = 2
                    self.Debug_Msg("Befehl wurde vom Fluke45 nicht verstanden!")
                #!>\r\n Steuerzeichen für Syntaxfehler
                # Befehl wurde verstanden doch ist nicht ausführbar
                # Siehe Fluke45 Handbuch Seite 5-5!
                elif (Value[-1] == '!>\r\n'):
                    i = 3
                    self.Debug_Msg("Befehl verstanden, aber vom Fluke45 nicht ausfuehrbar")
                
        return Value

                                       
                 
###############################################################################        
    def serialSend(self, SendMsg):
        """
        SerialSend sendet den übergebenen SendMsg-String an das Messgerät und
        ruft anschließend die Funktion serialReadLine auf, um die Antwort des
        Messgerätes zu erhalten.
        Die Antwort des Messgerätes wird z.Z. nur auf der Console und dem
        Textbrouser dargestellt.
        
        Parameters
        ---------        
        Self : 
        
        SendMsg : Der String der an das Messgerät gesendet werden soll.
        
        ReturnValue : None
        
        """
        self.Debug_Msg("serialSend Befehl: "+SendMsg[:-1])
        self.ser.write(SendMsg)
        hutzelbrutzel = self.serialReadLine()
        self.settext(hutzelbrutzel)
        self.Debug_Msg("#####")
        
        
        
    def exitApp(self):
        """
        exitApp schließt die Serieleschnitstelle und beendet anschließend das
        Programm
        
        Parameters
        ----------
        self
        """
        if(self.ser.isOpen() == True):
            self.ser.close()
        qApp.exit()

        
    def Debug_Msg(self, DebugMsg):
        """
        Debug_Msg ist eine Hilfsfunktion welche Debuginformationen zur verfügung
        stellt.
        Die Funktion prüft, ob in der GUI der DebugnachrichtenOutput aktiviert 
        ist, wenn ja werden die Ihr übergebenen Nachrichten in den TextBrouser
        der GUI und in die PythonConsole geschrieben.
        
        Parameters
        ----------
        
        self : 
        
        DebugMsg: String welcher die Debugnachricht enthällt und bei Aktivierter
        checkBox_DEBUG ausgegeben wird
        """
        if(self.checkBox_DEBUG.isChecked()):
            self.settext(DebugMsg)
            print(DebugMsg)
            
    def Fluke_Selbsttest(self):
        self.serialSend("*TST?\n")
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = makeGui()  
    form.show()
    app.exec_()