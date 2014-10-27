#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

                vbox = QtGui.QHBoxLayout()
                vbox.addWidget(self.radio1)
                vbox.addWidget(self.radio2)
                
                hbox = QtGui.QHBoxLayout()
                hbox.addWidget(self.line)
                hbox.addWidget(self.button)
        

                self.table = QtGui.QTableWidget(0,2)
                self.table.setHorizontalHeaderLabels(["ⵜⴰⵎⴰⵣⵉⵖⵜ".decode('utf-8'),"ⵜⴰⵄⵔⴰⴱⵜ".decode('utf-8')])
                header = self.table.horizontalHeader()
                header.setStretchLastSection(True)
                header.setResizeMode(QtGui.QHeaderView.Stretch)
                #bottom
                self.p = QtGui.QPushButton("ⵅⴼ ⵓⵀⵉⵍ".decode('utf-8'))
                self.p.clicked.connect(self.about)
                
                
                


                hbox2 = QtGui.QVBoxLayout()
                hbox2.addLayout(hbox)
                hbox2.addLayout(vbox)
                hbox2.addWidget(self.table)
                hbox2.addWidget(self.p)

                self.setWindowTitle("AmaDic".decode("utf-8"))
                self.setWindowIcon(QtGui.QIcon("ico.png"))
                self.setGeometry(0,20,450,600)
                self.setLayout(hbox2)
                self.show() 

        def about(self):
            QtGui.QMessageBox.about(self, "About AmaDic",
                "<b>AmaDic</b> is a simple dictionary created by Python Language"
                " \n Copyleft 2014.")
            


        def translate(self):
            con = sqlite3.connect("amawal")
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
        
        
    
def main():

    app = QtGui.QApplication(sys.argv)
    QtGui.QSystemTrayIcon(QtGui.QIcon("ico.png"),app).show()
    dict = amawal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()