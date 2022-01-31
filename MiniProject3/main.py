from ast import Num
from cgitb import text
from contextlib import nullcontext
from distutils import text_file
import sqlite3
import cv2
import numpy as np
from unittest import loader
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QImage,QPixmap
####################################################################################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("login.ui")
        self.ui.show()

        self.ui.setWindowTitle(" LOGIN  ")
        self.ui.label.setStyleSheet("image : url(face_images/icon/login1.png);")

        self.conn = sqlite3.connect("data.db")
        self.my_cursor = self.conn.cursor()

        self.ui.pushButton.clicked.connect(self.employe)


    def employe(self):
        self.ui = Emplo()
        self.user_name = self.ui.lineEdit_3.text()
        self.password = self.ui.lineEdit_4.text()

        self.my_cursor.execute('SELECT * FROM Admin')
        result = self.my_cursor.fetchall()
        if result[0][1]==self.user_name and result[0][2]==self.password:
            self.em()
    #def em(self):
        self.ui = Emplo()
    

#####################################################################################################
class Emplo(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ee = loader.load("empl.ui")
        self.ee.show()

        self.conn = sqlite3.connect("data.db")
        self.my_cursor = self.conn.cursor()
        self.load_data()

        self.ee.setWindowTitle("Employee List")
        self.ee.label.setStyleSheet("image : url(face_images/icon/employee.png);")
        self.ee.add.setStyleSheet("image : url(face_images/icon/add.png); \n background-color: rgb(255, 255, 255); \n border-style: outset; \n border-width: 0px; \n border-radius: 10px; \n font: bold 14px; ")
        self.ee.add.clicked.connect(self.add_employ)
        self.ee.edit.setStyleSheet("image : url(face_images/icon/edit.png); \n background-color: rgb(255, 255, 255); \n border-style: outset; \n border-width: 0px; \n border-radius: 10px; \n font: bold 14px; ")
        self.ee.edit.clicked.connect(self.edit_employ)
        self.ee.delete_2.setStyleSheet("image : url(face_images/icon/delete.png); \n background-color: rgb(255, 255, 255); \n border-style: outset; \n border-width: 0px; \n border-radius: 10px; \n font: bold 14px; ")
        self.ee.delete_2.clicked.connect(self.delete_employ)

    def load_data(self):

        self.my_cursor.execute("SELECT * FROM Employee")
        result = self.my_cursor.fetchall()
        
        for  i , item in enumerate(result):

            self.lab=QLabel()
            self.lab.setStyleSheet(F"image : url(face_images/employee/{i}.jpeg); ")
            self.lab.setText(F"{item[0]} ")

            self.labb=QLabel()
            self.labb.setText(F"{item[1]}\t  {item[2]}\t  {item[3]}\t  {item[4]} ")
            self.ee.verticalLayout_4.addWidget(self.lab)
            self.ee.verticalLayout.addWidget(self.labb)
            
            
    def add_employ(self):
        self.ee = addEmploy()

    def edit_employ(self):
        self.ee = editEmploy()
    
    def delete_employ(self):
        self.ee = deleteEmploy()
##################################################################################################
class editEmploy(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ed = loader.load("Editـemployees.ui")
        self.ed.show()


        self.ed.setWindowTitle("edit Employee")
        self.ed.btn_ok_2.clicked.connect(self.editt)

        self.conn = sqlite3.connect("data.db")
        self.my_cursor = self.conn.cursor()

    def editt(self):
        self.id = self.ed.lineEdit_1.text()
        self.First_name = self.ed.lineEdit_2.text()
        self.Last_name = self.ed.lineEdit_3.text()
        self.National_ID_Number = self.ed.lineEdit_4.text()
        self.Birthday= self.ed.lineEdit_5.text()

        self.my_cursor.execute(f'UPDATE Employee SET id="{self.id}",First_name="{self.First_name}",Last_name="{self.Last_name}",National_ID_Number="{self.National_ID_Number}",Birthday="{self.Birthday}" WHERE id=="{self.id}";')
        self.conn.commit()
        self.ed = MainWindow

###################################################################################################
class deleteEmploy(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.dl = loader.load("DELETEemployee.ui")
        self.dl.show()
        self.dl.setWindowTitle("Delete Employee")
        self.dl.btn_ok.clicked.connect(self.dell)
        self.conn = sqlite3.connect("data.db")
        self.my_cursor = self.conn.cursor()
        
    def dell(self):

        self.id = self.dl.lineEdit.text()
    
        self.my_cursor.execute(f"DELETE FROM Employee WHERE id == \'{self.id}\';")
        self.conn.commit()
        self.dl = MainWindow



######################################################################################################################################################################################################

class addEmploy(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ad = loader.load("ADDemployees.ui")
        self.ad.show()

        self.conn = sqlite3.connect("data.db")
        self.my_cursor = self.conn.cursor()

        self.ad.setWindowTitle("add Employee")
        self.ad.label.setStyleSheet("image : url(face_images/icon/photograph.png);")
        self.ad.label.clicked.connect(self.cammm)        
        #itemText()
        self.id = self.ad.lineEdit_1.text()
        self.First_name = self.ad.lineEdit_2.text()
        self.Last_name = self.ad.lineEdit_3.text()
        self.National_ID_Number = self.ad.lineEdit_4.text()
        self.Birthday= self.ad.lineEdit_5.text()

        #self.my_cursor.execute(f"INSERT INTO Employee(id , First_name , Last_name , National_ID_Number, mobile_number , email) VALUES ('{self.id}' , '{self.name}' ,'{self.family}', '{self.phone_number}','{self.mobile_number}' , '{self.email}'); " )
        #self.conn.commit()


    def cammm(self):
        self.ee = cammera()

###################################################################################################
class cammera(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.cm = loader.load("cammm.ui" , None)
        self.cm.show()

        self.conn = sqlite3.connect("data.db")
        self.my_cursor = self.conn.cursor()

        self.cm.setWindowTitle("  CAMERA !!  ")
        self.cm.pushButton.clicked.connect(self.take_pic)

        face_detector  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0)
        while True:
            ret, self.frame = cap.read()
            if not ret:
                break

            faces = face_detector.detectMultiScale(self.frame,1.3,4)
            self.frame_rgb = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
            self.frame_rgb = cv2.resize(self.frame_rgb,(308,260))
            img = QImage(self.frame_rgb, self.frame_rgb.shape[1], self.frame_rgb.shape[0],QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            self.cm.btn_label.setPixmap(pixmap)
            
            for x,y,w,h in faces:
                self.frame_face = self.frame[y:y+h,x:x+w]
            cv2.waitKey(1)
    

    def take_pic(self):
        self.my_cursor.execute("SELECT * FROM Employee")
        result = self.my_cursor.fetchall()
        x =0
        for  item in result:
            x=+1
        cv2.imwrite(f'face_images/employee/{x}.jpeg', self.frame_face )
        
        self.cm.close()




app = QApplication()
main_window = MainWindow()
app.exec()

