#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD
#
# SCRIPT: AmaDic
# AUTHOR: Mohammed Raji // github.com/MohammedRaji /twitter/@mohammedraji6
# REV:    1.0.0.T (Valid are A, B, T and P)
#         (For Alpha, Beta, Test and Production)
#
# PLATFORM: (SPECIFY: all linux distros)
#
#
# PURPOSE: Make a offline amazigh-arabic dictionary for linux   
#                 
#          
##########################################################
=======

>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b
from PySide import QtGui,QtCore
import sys
from PySide import *
import sqlite3

class amawal(QtGui.QWidget):
        """docstring for amawal"""
        def __init__(self):
                super(amawal, self).__init__()

                self.line = QtGui.QLineEdit()
                self.line.returnPressed.connect(self.translate)
                self.line.textChanged.connect(self.translate)
                self.button = QtGui.QPushButton("ⵙⵖⵓⵍ".decode('utf-8'))
                self.button.clicked.connect(self.translate)
                
                self.radio1 = QtGui.QRadioButton("ⵜⴰⵎⴰⵣⵉⵖⵜ".decode('utf-8'))
                self.radio2 = QtGui.QRadioButton("ⵜⴰⵄⵔⴰⴱⵜ".decode('utf-8'))
                self.radio1.setChecked(True)

<<<<<<< HEAD
                vbox = QtGui.QHBoxLayout()
=======
                vbox = QtGui.QVBoxLayout()
>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b
                vbox.addWidget(self.radio1)
                vbox.addWidget(self.radio2)
                
                hbox = QtGui.QHBoxLayout()
                hbox.addWidget(self.line)
                hbox.addWidget(self.button)
<<<<<<< HEAD
        
=======
                ########
                self.setStyleSheet("QWidget {border:none;border-radius:3px;color :black;font-weight:500; font-size: 10pt}QPushButton{color:#099000;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}QLineEdit{background-color:white; color:black}QTextEdit{background-color:#ffffff; color:#000000}")
                #########
                
>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b

                self.table = QtGui.QTableWidget(0,2)
                self.table.setHorizontalHeaderLabels(["ⵜⴰⵎⴰⵣⵉⵖⵜ".decode('utf-8'),"ⵜⴰⵄⵔⴰⴱⵜ".decode('utf-8')])
                header = self.table.horizontalHeader()
                header.setStretchLastSection(True)
                header.setResizeMode(QtGui.QHeaderView.Stretch)
                #bottom
                self.p = QtGui.QPushButton("ⵅⴼ ⵓⵀⵉⵍ".decode('utf-8'))
                self.p.clicked.connect(self.about)
                
<<<<<<< HEAD
                
                
=======
>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b


                hbox2 = QtGui.QVBoxLayout()
                hbox2.addLayout(hbox)
                hbox2.addLayout(vbox)
                hbox2.addWidget(self.table)
                hbox2.addWidget(self.p)

<<<<<<< HEAD
                self.setWindowTitle("AmaDic".decode("utf-8"))
                self.setWindowIcon(QtGui.QIcon("ico.png"))
=======
                self.setWindowTitle("ⴰⵎⴰⵡⴰⵍ".decode("utf-8"))
                self.setWindowIcon(QtGui.QIcon("dict.png"))
>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b
                self.setGeometry(0,20,450,600)
                self.setLayout(hbox2)
                self.show() 

        def about(self):
<<<<<<< HEAD
            QtGui.QMessageBox.about(self, "About AmaDic",
                "<b>AmaDic</b> is a simple dictionary created by Python Language"
                " \n Copyleft 2014.")
            
=======
            self.about=ab()
>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b


        def translate(self):
            con = sqlite3.connect("amawal")
<<<<<<< HEAD
=======
            #amawal is sqlite database
>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b
            cur = con.cursor()

            if self.radio1.isChecked():
                sql = "select count(*) from animal where tmz like '%%%s%%'" % self.line.text()
            else:
                sql = "select count(*) from animal where ar like '%%%s%%'" % self.line.text()


            cur.execute(sql)
            compare = cur.fetchone()[0]
            counts = 0
            x = 0
            if compare >= 50:
                counts = 50
            else:
                counts = compare

            if self.radio1.isChecked():
                sql = "select * from animal where tmz like '%%%s%%' limit 50" % self.line.text()
            else:
                sql = "select * from animal where ar like '%%%s%%' limit 50" % self.line.text()

            cur.execute(sql)

            self.table.setRowCount(counts)
            rows = cur.fetchall()

            for i in rows:
                print i[1].encode("utf-8")
                self.en = QtGui.QTableWidgetItem(i[1])
                self.ar = QtGui.QTableWidgetItem(i[2])
                self.table.setItem(x,0,self.en)
                self.table.setItem(x,1,self.ar)
                x += 1
<<<<<<< HEAD
=======

class ab(QtGui.QWidget):
    """docstring for about""" 
    def __init__(self):
        super(ab,self).__init__()
        self.setWindowTitle("About AmaDic")
        self.tab=QtGui.QTabWidget()
        

        self.show() 
        

>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b
        
        
    
def main():

    app = QtGui.QApplication(sys.argv)
<<<<<<< HEAD
    QtGui.QSystemTrayIcon(QtGui.QIcon("ico.png"),app).show()
=======
    app.setStyle(QtGui.QStyleFactory.create("plastique"))
    QtGui.QSystemTrayIcon(QtGui.QIcon("dict.png"),app).show()
>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b
    dict = amawal()
    sys.exit(app.exec_())

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 020af627cdf625eddac0b46ddd4352fa0be90c0b
