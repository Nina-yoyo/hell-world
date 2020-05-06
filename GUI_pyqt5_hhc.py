# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from gui_zhaoming import Ui_MainWindow

class GUI_Demo(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GUI_Demo,self).__init__()
        self.setupUi(self)
        self.comboBox.setCurrentIndex(0)
        global w1,w2,w3,w4,w5
        w1 = 0.3
        w2 = 0.2
        w3 = 0.25
        w4 = 0.1
        w5 = 0.15
        self.pushButton.clicked.connect(self.bt_action)
        self.lineEdit.editingFinished.connect(self.show_message_Q1)
        self.lineEdit_Q2.editingFinished.connect(self.show_message_Q2)
        self.lineEdit_Q3.editingFinished.connect(self.show_message_Q3)
        self.lineEdit_Q4.editingFinished.connect(self.show_message_Q4)
        self.lineEdit_Q5.editingFinished.connect(self.show_message_Q5)
        
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

    def selectionchange(self,i):
        global w1,w2,w3,w4,w5
        Num_sit = self.comboBox.currentIndex()
        if Num_sit == 0:
            w1 = 0.3
            w2 = 0.2
            w3 = 0.25
            w4 = 0.1
            w5 = 0.15
        elif Num_sit == 1:
            w1 = 0.3
            w2 = 0.25
            w3 = 0.25
            w4 = 0.1
            w5 = 0.1
        elif Num_sit == 2:
            w1 = 0.35
            w2 = 0.2
            w3 = 0.25
            w4 = 0.1
            w5 = 0.1
        elif Num_sit == 3:
            w1 = 0.35
            w2 = 0.25
            w3 = 0.15
            w4 = 0.1
            w5 = 0.15
        elif Num_sit == 4:
            w1 = 0.3
            w2 = 0.3
            w3 = 0.2
            w4 = 0.1
            w5 = 0.1
        elif Num_sit == 5:
            w1 = 0.25
            w2 = 0.3
            w3 = 0.15
            w4 = 0.15
            w5 = 0.15
        else: 
            w1 = 0.2
            w2 = 0.25
            w3 = 0.25
            w4 = 0.15
            w5 = 0.15
        print(w1,w2,w3,w4,w5,i)
        
    def show_message_Q1(self):
        
        x1 = self.lineEdit.text()
        x1 = float(x1)

        if x1<40:
            dialog =QDialog()
            dialog.resize(230,100)
            label = QLabel('输入分数不应该低于40',dialog)
            label.move(25,15)
            button = QPushButton('确定',dialog)
            button.clicked.connect(dialog.close)
            button.move(50,50)
            dialog.setWindowTitle('对话框')
            dialog.setWindowModality(Qt.ApplicationModal)
            
            dialog.exec()
    def show_message_Q2(self):
        
        
        x2 = self.lineEdit_Q2.text()
        x2 = float(x2)

        if x2<40:
            dialog =QDialog()
            dialog.resize(230,100)
            label = QLabel('输入分数不应该低于40',dialog)
            label.move(25,15)
            button = QPushButton('确定',dialog)
            button.clicked.connect(dialog.close)
            button.move(50,50)
            dialog.setWindowTitle('对话框')
            dialog.setWindowModality(Qt.ApplicationModal)
            
            dialog.exec()
    def show_message_Q3(self):
        
        x3 = self.lineEdit_Q3.text()
        x3 = float(x3)

        if x3<40:
            dialog =QDialog()
            dialog.resize(230,100)
            label = QLabel('输入分数不应该低于40',dialog)
            label.move(25,15)
            button = QPushButton('确定',dialog)
            button.clicked.connect(dialog.close)
            button.move(50,50)
            dialog.setWindowTitle('对话框')
            dialog.setWindowModality(Qt.ApplicationModal)
            
            dialog.exec()
    def show_message_Q4(self):       
        
        x4 = self.lineEdit_Q4.text()
        x4 = float(x4)

        if x4<40:
            dialog =QDialog()
            dialog.resize(230,100)
            label = QLabel('输入分数不应该低于40',dialog)
            label.move(25,15)
            button = QPushButton('确定',dialog)
            button.clicked.connect(dialog.close)
            button.move(50,50)
            dialog.setWindowTitle('对话框')
            dialog.setWindowModality(Qt.ApplicationModal)
            
            dialog.exec()      
    def show_message_Q5(self):       
        
        x5 = self.lineEdit_Q5.text()
        x5 = float(x5)

        if x5<40:
            dialog =QDialog()
            dialog.resize(230,100)
            label = QLabel('输入分数不应该低于40',dialog)
            label.move(25,15)
            button = QPushButton('确定',dialog)
            button.clicked.connect(dialog.close)
            button.move(50,50)
            dialog.setWindowTitle('对话框')
            dialog.setWindowModality(Qt.ApplicationModal)
            
            dialog.exec()         
        
    
    def bt_action(self):
        global w1,w2,w3,w4,w5
        x1 = self.lineEdit.text()
        x1 = float(x1)
        x2 = self.lineEdit_Q2.text()
        x2 = float(x2)
        x3 = self.lineEdit_Q3.text()
        x3 = float(x3)
        x4 = self.lineEdit_Q4.text()
        x4 = float(x4)
        x5 = self.lineEdit_Q5.text()
        x5 = float(x5)
        x6 = self.lineEdit_Q6.text()
        x6 = float(x6)
        Pingfen = x1*w1+x2*w2+x3*w3+x4*w4+x5*w5+x6
        Pingfen_i = round(Pingfen,2)
        self.lineEdit_7.setText(str(Pingfen_i))
        if Pingfen>=50 and Pingfen<60:
            self.lineEdit_8.setText('一星')
        elif Pingfen>=60 and Pingfen<80:
            self.lineEdit_8.setText('二星')
        elif Pingfen>=80:
            self.lineEdit_8.setText('三星')
        else:
            self.lineEdit_8.setText('评分过低')
        
if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    #main = QMainWindow()
    #ui = gui_zhaoming.Ui_MainWindow()
    #ui.setupUi(main)
    
    main = GUI_Demo()
    main.show()
    sys.exit(app.exec_())
