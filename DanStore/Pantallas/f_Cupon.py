# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f_Cupon.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 210)
        MainWindow.setMinimumSize(QtCore.QSize(260, 210))
        MainWindow.setMaximumSize(QtCore.QSize(260, 210))
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.L1 = QtWidgets.QLabel(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(0, 0, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.L1.setFont(font)
        self.L1.setAlignment(QtCore.Qt.AlignCenter)
        self.L1.setObjectName("L1")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 60, 261, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.D_Cupon = QtWidgets.QLineEdit(self.frame)
        self.D_Cupon.setGeometry(QtCore.QRect(100, 15, 150, 30))
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
        self.D_Cupon.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.D_Cupon.setFont(font)
        self.D_Cupon.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.D_Cupon.setText("")
        self.D_Cupon.setAlignment(QtCore.Qt.AlignCenter)
        self.D_Cupon.setClearButtonEnabled(True)
        self.D_Cupon.setObjectName("D_Cupon")
        self.L_Cupon = QtWidgets.QLabel(self.frame)
        self.L_Cupon.setGeometry(QtCore.QRect(10, 20, 80, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.L_Cupon.setFont(font)
        self.L_Cupon.setStyleSheet("")
        self.L_Cupon.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Cupon.setObjectName("L_Cupon")
        self.b_Aplicar = QtWidgets.QPushButton(self.centralwidget)
        self.b_Aplicar.setGeometry(QtCore.QRect(10, 130, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Aplicar.setFont(font)
        self.b_Aplicar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Aplicar.setAutoDefault(True)
        self.b_Aplicar.setObjectName("b_Aplicar")
        self.b_Cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.b_Cancelar.setGeometry(QtCore.QRect(150, 130, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cancelar.setFont(font)
        self.b_Cancelar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Cancelar.setAutoDefault(True)
        self.b_Cancelar.setObjectName("b_Cancelar")
        self.L3 = QtWidgets.QLabel(self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(210, 190, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L3.setFont(font)
        self.L3.setAlignment(QtCore.Qt.AlignCenter)
        self.L3.setObjectName("L3")
        self.b_Administrar = QtWidgets.QPushButton(self.centralwidget)
        self.b_Administrar.setGeometry(QtCore.QRect(80, 170, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Administrar.setFont(font)
        self.b_Administrar.setAutoDefault(True)
        self.b_Administrar.setObjectName("b_Administrar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cupones"))
        self.L2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Cupones</span></p></body></html>"))
        self.L1.setText(_translate("MainWindow", "DanStore"))
        self.D_Cupon.setPlaceholderText(_translate("MainWindow", "XDF150"))
        self.L_Cupon.setText(_translate("MainWindow", "CÓDIGO"))
        self.b_Aplicar.setText(_translate("MainWindow", "Aplicar"))
        self.b_Cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.L3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aaaaaa;\">v 1.2.0</span></p></body></html>"))
        self.b_Administrar.setText(_translate("MainWindow", "Administrar"))
