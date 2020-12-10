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
        MainWindow.resize(260, 240)
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
        self.L4.setGeometry(QtCore.QRect(10, 110, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(14)
        self.L4.setFont(font)
        self.L4.setObjectName("L4")
        self.D_psw = QtWidgets.QLineEdit(self.centralwidget)
        self.D_psw.setGeometry(QtCore.QRect(100, 110, 150, 20))
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
        self.D_psw.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.D_psw.setFont(font)
        self.D_psw.setMaxLength(10)
        self.D_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.D_psw.setObjectName("D_psw")
        self.L2 = QtWidgets.QLabel(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(0, 30, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(18)
        self.L2.setFont(font)
        self.L2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.L2.setMidLineWidth(0)
        self.L2.setAlignment(QtCore.Qt.AlignCenter)
        self.L2.setObjectName("L2")
        self.b_Cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.b_Cancelar.setGeometry(QtCore.QRect(150, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cancelar.setFont(font)
        self.b_Cancelar.setAutoDefault(True)
        self.b_Cancelar.setObjectName("b_Cancelar")
        self.L3 = QtWidgets.QLabel(self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(10, 80, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(14)
        self.L3.setFont(font)
        self.L3.setObjectName("L3")
        self.L1 = QtWidgets.QLabel(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(0, 0, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.L1.setFont(font)
        self.L1.setAlignment(QtCore.Qt.AlignCenter)
        self.L1.setObjectName("L1")
        self.D_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.D_usuario.setGeometry(QtCore.QRect(100, 80, 150, 20))
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
        self.D_usuario.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.D_usuario.setFont(font)
        self.D_usuario.setText("")
        self.D_usuario.setMaxLength(10)
        self.D_usuario.setObjectName("D_usuario")
        self.b_Entrar = QtWidgets.QPushButton(self.centralwidget)
        self.b_Entrar.setGeometry(QtCore.QRect(10, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Entrar.setFont(font)
        self.b_Entrar.setAutoDefault(True)
        self.b_Entrar.setObjectName("b_Entrar")
        self.b_Registrar = QtWidgets.QPushButton(self.centralwidget)
        self.b_Registrar.setGeometry(QtCore.QRect(80, 190, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar.setFont(font)
        self.b_Registrar.setAutoDefault(True)
        self.b_Registrar.setObjectName("b_Registrar")
        self.L5 = QtWidgets.QLabel(self.centralwidget)
        self.L5.setGeometry(QtCore.QRect(200, 220, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L5.setFont(font)
        self.L5.setAlignment(QtCore.Qt.AlignCenter)
        self.L5.setObjectName("L5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.D_usuario, self.D_psw)
        MainWindow.setTabOrder(self.D_psw, self.b_Entrar)
        MainWindow.setTabOrder(self.b_Entrar, self.b_Cancelar)
        MainWindow.setTabOrder(self.b_Cancelar, self.b_Registrar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.L4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Contraseña</span></p></body></html>"))
        self.L2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Login</span></p></body></html>"))
        self.b_Cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.L3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Usuario</span></p></body></html>"))
        self.L1.setText(_translate("MainWindow", "Dan1"))
        self.b_Entrar.setText(_translate("MainWindow", "Entrar"))
        self.b_Registrar.setText(_translate("MainWindow", "Registrar"))
        self.L5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aaaaaa;\">v 1.3.0</span></p></body></html>"))
