# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fakepath'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QGridLayout, QSizePolicy
import os
import time


import demucs.separate


text_o = "Placeholder"


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):


        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(130, 260, 181, 71))
        self.browse_button.setAutoDefault(False)
        self.browse_button.setDefault(False)
        self.browse_button.setObjectName("browse_button")

        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(340, 260, 181, 71))
        self.submit_button.setAutoDefault(False)
        self.submit_button.setDefault(False)
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setEnabled(False)


        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(250, 400, 251, 101))
        self.checkBox.setObjectName("checkBox")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(130, 130, 471, 111))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.About_button = QtWidgets.QToolButton(self.centralwidget)
        self.About_button.setGeometry(QtCore.QRect(630, 20, 151, 41))
        self.About_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.About_button.setObjectName("About_button")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 370, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        #Outut box
        self.outputbox = QtWidgets.QLineEdit(self.centralwidget)
        self.outputbox.setGeometry(QtCore.QRect(130, 190, 431, 20))
        self.outputbox.setText("")
        self.outputbox.setClearButtonEnabled(False)
        self.outputbox.setObjectName("outputbox")

        # Inputbox
        self.inputbox = QtWidgets.QLineEdit(self.centralwidget)
        self.inputbox.setGeometry(QtCore.QRect(130, 150, 431, 20))
        self.inputbox.setText("")
        self.inputbox.setClearButtonEnabled(False)
        self.inputbox.setObjectName("inputbox")
        self.inputbox.setReadOnly(True)


        mainWindow.setCentralWidget(self.centralwidget)

        # ????
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        # UI Functionalities (mostly defunct)

        self.About_button.clicked.connect(self.about_page)  # About models page 

        self.checkBox.clicked.connect(self.overwrite_checker) # Overwite check box

        self.comboBox.currentIndexChanged.connect(self.model_choice) # Models chooser


        self.browse_button.clicked.connect(self.openfile_dial)  # File selector

        self.submit_button.clicked.connect(self.submit) 

    



    # Ui Functionalities definitions

    

    def vr2(self):
        
        try: demucs.separate.main(["--mp3", "--two-stems", "vocals", str(self.file_path) ,"-o", str(self.outputdir) ])

        except Exception as e: 
                msg = QMessageBox()
                QMessageBox()
                msg.setWindowTitle("ERROR")
                #msg.setWindowFlag
                msg.setText(str(e))


    def submit(self):
        
        self.outputdir = self.outputbox.text()

        print(self.outputdir)

        msg = QMessageBox()

        msg.setWindowTitle("Warning")

        tupled_dir = os.path.split(self.out_path)
        dir_cont = os.listdir(tupled_dir[0])

        tuple_name = os.path.split(self.out_path)

        f_name = tuple_name[1]
        print(f_name)

        if  self.checkBox.isChecked() and self.outputdir == self.out_path:

            msg.setText("There is already an existing file with the same name present, \n Are you sure you want to overwrite the existing file?")

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)

            reply = msg.exec_()

            if reply == QMessageBox.Ok:

                self.vr2()
                
                print("loading screen or something")

            #temp


        elif self.outputdir == self.out_path:  # use os.split for this. 
            
            msg = QMessageBox()

            msg.setWindowTitle("Overwrite Error")
            msg.setIcon(QMessageBox.Warning)

            msg.setText("There is already a folder with the same name in this directory, unable to proceed.")

            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)

            x = msg.exec_()

        if self.outputdir != self.out_path:

            self.vr2()

    
    def openfile_dial(self):

        options = QFileDialog.Options()
        
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Select audio file", "", "Mp3 files (*.mp3)", options=options)
        
        if self.file_path:

            print(self.file_path)
            
            print(self.file_path)

            self.inputbox.setText(self.file_path)

            base_name, ext = os.path.splitext(os.path.basename(self.file_path))

            input_dir = os.path.split(self.file_path)

            output_Fname = f"CHANGED_{base_name}"  # "{ext}"

            self.out_path = os.path.join(input_dir[0], output_Fname)

            self.outputbox.setText(self.out_path)

            self.submit_button.setEnabled(True)

            return self.file_path, self.out_path


    def overwrite_checker(self):
       
       check = self.checkBox.isChecked()

       print(check)

       return(check)
    

    def model_choice(self, index):

        self.model = self.comboBox.currentText()

        print(self.model)

        return self.model


    def about_page(self):

        msg = QMessageBox()

        msg.setWindowTitle("Models Info")

        msg.setText(text_o)

        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)

        # msg.setDetailedText("errors")

        for i in range (5):
            i = i+1 
            print("about clicked")
        
        x = msg.exec_()


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Music Remover"))
        
        self.browse_button.setText(_translate("mainWindow", "Choose .MP3 Audio file"))
        self.submit_button.setText(_translate("mainWindow", "Submit"))

        self.checkBox.setText(_translate("mainWindow", "Overwrite duplicate file (if present)"))
        self.About_button.setText(_translate("mainWindow", "About Models"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Ai1"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Ai2"))
        self.comboBox.setItemText(2, _translate("mainWindow", "Ai3"))
        self.comboBox.setItemText(3, _translate("mainWindow", "ai4"))
        self.outputbox.setPlaceholderText(_translate("mainWindow", "Output path"))
        self.inputbox.setPlaceholderText(_translate("mainWindow", "Input path/File"))

    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
