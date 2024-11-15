# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audio rep.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 642)
        MainWindow.setStyleSheet("background-color: rgb(185, 185, 185);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tab_box = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_box.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(148, 146, 146);\n"
"selection-color: rgb(255, 208, 97);")
        self.tab_box.setObjectName("tab_box")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.audio_e_submit = QtWidgets.QPushButton(self.tab_3)
        self.audio_e_submit.setGeometry(QtCore.QRect(150, 410, 271, 51))
        self.audio_e_submit.setObjectName("audio_e_submit")
        self.PU_choice_AE = QtWidgets.QComboBox(self.tab_3)
        self.PU_choice_AE.setGeometry(QtCore.QRect(150, 320, 271, 22))
        self.PU_choice_AE.setObjectName("PU_choice_AE")
        self.PU_choice_AE.addItem("")
        self.PU_choice_AE.addItem("")
        self.aud_e_inp_box = QtWidgets.QLineEdit(self.tab_3)
        self.aud_e_inp_box.setGeometry(QtCore.QRect(40, 250, 561, 20))
        self.aud_e_inp_box.setStyleSheet("selection-color: rgb(255, 170, 0);")
        self.aud_e_inp_box.setObjectName("aud_e_inp_box")
        self.aud_e_outbox = QtWidgets.QLineEdit(self.tab_3)
        self.aud_e_outbox.setGeometry(QtCore.QRect(40, 280, 561, 20))
        self.aud_e_outbox.setObjectName("aud_e_outbox")
        self.browse_AE = QtWidgets.QPushButton(self.tab_3)
        self.browse_AE.setGeometry(QtCore.QRect(150, 360, 271, 41))
        self.browse_AE.setObjectName("browse_AE")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.PU_choice_AE.raise_()
        self.audio_e_submit.raise_()
        self.aud_e_inp_box.raise_()
        self.aud_e_outbox.raise_()
        self.browse_AE.raise_()
        self.label_5.raise_()
        self.tab_box.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.aud_rep_submit = QtWidgets.QPushButton(self.tab_4)
        self.aud_rep_submit.setGeometry(QtCore.QRect(140, 430, 271, 51))
        self.aud_rep_submit.setObjectName("aud_rep_submit")
        self.PU_choice_AR = QtWidgets.QComboBox(self.tab_4)
        self.PU_choice_AR.setGeometry(QtCore.QRect(140, 350, 271, 22))
        self.PU_choice_AR.setObjectName("PU_choice_AR")
        self.PU_choice_AR.addItem("")
        self.PU_choice_AR.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.outbox_AR = QtWidgets.QLineEdit(self.tab_4)
        self.outbox_AR.setGeometry(QtCore.QRect(20, 310, 561, 20))
        self.outbox_AR.setObjectName("outbox_AR")
        self.video_pathAR = QtWidgets.QLineEdit(self.tab_4)
        self.video_pathAR.setGeometry(QtCore.QRect(20, 250, 561, 20))
        self.video_pathAR.setObjectName("video_pathAR")
        self.audio_pathAR = QtWidgets.QLineEdit(self.tab_4)
        self.audio_pathAR.setGeometry(QtCore.QRect(20, 280, 561, 20))
        self.audio_pathAR.setObjectName("audio_pathAR")
        self.browse_AR = QtWidgets.QPushButton(self.tab_4)
        self.browse_AR.setGeometry(QtCore.QRect(140, 380, 271, 41))
        self.browse_AR.setObjectName("browse_AR")
        self.tab_box.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tab_box, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_box.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.audio_e_submit.setText(_translate("MainWindow", "Submit"))
        self.PU_choice_AE.setItemText(0, _translate("MainWindow", "Use GPU"))
        self.PU_choice_AE.setItemText(1, _translate("MainWindow", "Use CPU"))
        self.aud_e_inp_box.setText(_translate("MainWindow", "Input box"))
        self.aud_e_outbox.setText(_translate("MainWindow", "Output box"))
        self.browse_AE.setText(_translate("MainWindow", "Browse"))
        self.label_5.setText(_translate("MainWindow", "Audio Extractor"))
        self.tab_box.setTabText(self.tab_box.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.aud_rep_submit.setText(_translate("MainWindow", "Submit"))
        self.PU_choice_AR.setItemText(0, _translate("MainWindow", "Use GPU"))
        self.PU_choice_AR.setItemText(1, _translate("MainWindow", "Use CPU"))
        self.label_4.setText(_translate("MainWindow", "Audio Replacer"))
        self.outbox_AR.setText(_translate("MainWindow", "Output path"))
        self.video_pathAR.setText(_translate("MainWindow", "Video path"))
        self.audio_pathAR.setText(_translate("MainWindow", "Cleaned audio path"))
        self.browse_AR.setText(_translate("MainWindow", "Browse"))
        self.tab_box.setTabText(self.tab_box.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
