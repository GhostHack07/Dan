# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(280, 260))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.L4 = QtWidgets.QLabel(self.centralwidget)
        self.L4.setGeometry(QtCore.QRect(10, 110, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L4.setFont(font)
        self.L4.setObjectName("L4")
        self.T4 = QtWidgets.QLineEdit(self.centralwidget)
        self.T4.setGeometry(QtCore.QRect(120, 110, 150, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 160, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 160, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.T4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.T4.setFont(font)
        self.T4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.T4.setObjectName("T4")
        self.L2 = QtWidgets.QLabel(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(0, 30, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(18)
        self.L2.setFont(font)
        self.L2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.L2.setMidLineWidth(0)
        self.L2.setAlignment(QtCore.Qt.AlignCenter)
        self.L2.setObjectName("L2")
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(170, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.B2.setFont(font)
        self.B2.setObjectName("B2")
        self.L3 = QtWidgets.QLabel(self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(10, 80, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L3.setFont(font)
        self.L3.setObjectName("L3")
        self.L1 = QtWidgets.QLabel(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(0, 0, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.L1.setFont(font)
        self.L1.setAlignment(QtCore.Qt.AlignCenter)
        self.L1.setObjectName("L1")
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(120, 80, 150, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 160, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 160, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.T3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.T3.setFont(font)
        self.T3.setText("")
        self.T3.setMaxLength(10)
        self.T3.setObjectName("T3")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(10, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.B1.setFont(font)
        self.B1.setObjectName("B1")
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(90, 190, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.B3.setFont(font)
        self.B3.setObjectName("B3")
        self.L5 = QtWidgets.QLabel(self.centralwidget)
        self.L5.setGeometry(QtCore.QRect(230, 220, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L5.setFont(font)
        self.L5.setAlignment(QtCore.Qt.AlignCenter)
        self.L5.setObjectName("L5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.L4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Contraseña</span></p></body></html>"))
        self.L2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Login</span></p></body></html>"))
        self.B2.setText(_translate("MainWindow", "Cancelar"))
        self.L3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Usuario</span></p></body></html>"))
        self.L1.setText(_translate("MainWindow", "Dan1"))
        self.B1.setText(_translate("MainWindow", "Entrar"))
        self.B3.setText(_translate("MainWindow", "Registrar"))
        self.L5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aaaaaa;\">v 1.0.0</span></p></body></html>"))
