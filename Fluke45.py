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

#Deaktivieren um die Debuginformation auf der Console zu Deaktivieren
DEBUG = True 



#######################
#       IMPORTS       #
#######################    
import serial
import sys
import time


#Imports für die Gui
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
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
        
        
    def settext(self, Outputdata):
        
        for c in Outputdata:
            self.textBrowser_Output.append(c)
        
        

        
        
        
        

#######################
#       PROGRAM       #
#######################

#Definition des Objektes "Fluke45"
class Fluke45(makeGui):
    

###############################################################################
    def serialPort(self):
        """
        #serialPort öffnet den COM-Port zum Fluke mit den standard RS-232 Einstellungen
        """
        if(DEBUG):
            print ("Serialport")
        
        self.ser = serial.Serial(
                                 port='COM6',
                                 baudrate=9600,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS,
                                 timeout = 1
                                 ) 

    def serialScan(self):
        """
        Sucht nach verfügbaren Com-Ports und gibt diese in einer Liste zurück
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
        #serialReadLine liest alle gesendeten Zeilen des Fluke45 solange bis das
        #Messgerät den Sendebetrieb einstellt. Der Sendebetrieb ist vorbei, sobald
        #das Messgerät ein Steuerzeichen ('=>' oder '?>' oder '!>') gefolgt von einem
        #CR und LF (CR = Carriage Return, LF = Line Feed)
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
                if (Value[(len(Value))-1] == "=>\r\n"):
                    i = 1
                    if(DEBUG):
                        print("Fluke45 hat Befehl verstanden u. ausgefuehrt")
                        
                #"?>\r\n" Steuerzeichen für Befehlsfehler
                #Befehl wurde nicht verstanden.
                elif (Value[(len(Value))-1] == '?>\r\n'):
                    i = 2
                    if(DEBUG):
                        print("Befehl wurde vom Fluke45 nicht verstanden!")
                        
                #!>\r\n Steuerzeichen für Syntaxfehler
                # Befehl wurde verstanden doch ist nicht ausführbar
                # Siehe Fluke45 Handbuch Seite 5-5!
                elif (Value[(len(Value))-1] == '!>\r\n'):
                    i = 3
                    if(DEBUG):
                        print("Befehl verstanden, aber vom Fluke45 nicht ausfuehrbar")
        return Value

                                       
                 
###############################################################################
    def serialSend_VAL(self):
        """
        #serialSend sendet momentan nur den *IDN? Befehl
        # *IDN? vordert das Fluke45 auf sich zu Identifizieren (VersionsNR. etc)  
        
        #TODO: Allgemeingültige Sendefunktion schreiben.
        #TODO: Minimale Syntaxprüfung? (Optional)
        """
        if(DEBUG):
            print("serialSend_IDN")
        self.ser.write("VAL?\n")
        hutzelbrutzel = self.serialReadLine()    
        self.settext(hutzelbrutzel)
        
        
        
        
    def serialSend_IDN(self):
        if(DEBUG):
            print("serialSend_IDN")
        self.ser.write("*IDN?\n")
        hutzelbrutzel = self.serialReadLine()    
        self.settext(hutzelbrutzel)
        
    def exitApp(self):
        self.ser.close()
        qApp.quit()
        
        
        
  
###############################################################################
#Main Funktion
###############################################################################

def main(args=sys.argv[1:]):
    
    
    
    app = QtGui.QApplication(sys.argv) 
    
    
    flu = Fluke45()
    flu.__init__

    ValidComPorts = flu.serialScan()
    for i in range(len(ValidComPorts)):
        flu.comboBox_COM.addItem(ValidComPorts[i][1])
    
    
    

    #TODO: Übergabeparameter klären gegebenenfalls umschreiben mit nur eienr Klasse
    flu.connect(flu.comboBox_COM, QtCore.SIGNAL("activated(QString)"),flu.serialPort)
    flu.connect(flu.pushButton_IDN, QtCore.SIGNAL("clicked()"),flu.serialSend_IDN)
    flu.connect(flu.pushButton_VAL, QtCore.SIGNAL("clicked()"),flu.serialSend_VAL)
    flu.connect(flu.pushButton_exit, QtCore.SIGNAL("clicked()"),flu.exitApp)

    flu.show()
    
        
    
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()