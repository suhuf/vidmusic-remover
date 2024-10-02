# WIP
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import os
import shutil



text_o = "This ai is that ai i these ais ar e those ais are one ai is one ai is not"


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
        self.outputbox = QtWidgets.QLineEdit(self.centralwidget)
        self.outputbox.setGeometry(QtCore.QRect(130, 190, 431, 20))
        self.outputbox.setText("")
        self.outputbox.setClearButtonEnabled(False)
        self.outputbox.setObjectName("outputbox")
        self.inputbox = QtWidgets.QLineEdit(self.centralwidget)
        self.inputbox.setGeometry(QtCore.QRect(130, 150, 431, 20))
        self.inputbox.setText("")
        self.inputbox.setClearButtonEnabled(False)
        self.inputbox.setObjectName("inputbox")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        # UI Functionalities

        self.About_button.clicked.connect(self.about_page)  # About models page 

        self.checkBox.clicked.connect(self.overwrite_checker) # Overwite check box


        self.comboBox.currentIndexChanged.connect(self.model_choice) # Models chooser


        self.browse_button.clicked.connect(self.openfile_dial)  # File selector

        self.submit_button.clicked.connect(self.submit) 


    # Ui Functionalities definitions

    

    def submit(self):
        
        msg = QMessageBox()

        msg.setWindowTitle("Warning")

        tupled_dir = os.path.split(self.out_path)
        dir_cont = os.listdir(tupled_dir[0])

        tuple_name = os.path.split(self.out_path)

        f_name = tuple_name[1]
        print(f_name)

        if  self.checkBox.isChecked() and f_name in dir_cont:

            msg.setText("There is already an existing file with the same name present, \n Are you sure you want to overwrite the existing file?")

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)

            reply = msg.exec_()

            if reply == QMessageBox.Ok:
                
                print("loading screen or something")

            #temp
    
        elif f_name in dir_cont:  # use os.split for this. 
            print("There is already a file with this name in this directory, unable to proceed. ")
    
        

    def openfile_dial(self):

        options = QFileDialog.Options()
        
        file_path, _ = QFileDialog.getOpenFileName(None, "Select mp3 file", "", "Mp3 files (*.txt)", options=options)
        
        if file_path:

            print(file_path)
            
            self.inputbox.setText(file_path)

            base_name, ext = os.path.splitext(os.path.basename(file_path))

            input_dir = os.path.split(file_path)

            output_Fname = f"CHANGED_{base_name}{ext}"

            self.out_path = os.path.join(input_dir[0], output_Fname)

            self.outputbox.setText(self.out_path)

            self.submit_button.setEnabled(True)

            return file_path, self.out_path


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
        
        self.browse_button.setText(_translate("mainWindow", "Choose video file"))
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
