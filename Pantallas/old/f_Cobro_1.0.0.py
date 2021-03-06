# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f_Cobro.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 260)
        MainWindow.setMinimumSize(QtCore.QSize(390, 260))
        MainWindow.setMaximumSize(QtCore.QSize(390, 260))
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
        self.fr_Accion = QtWidgets.QFrame(self.centralwidget)
        self.fr_Accion.setGeometry(QtCore.QRect(0, 60, 390, 40))
        self.fr_Accion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Accion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Accion.setObjectName("fr_Accion")
        self.b_efectivo = QtWidgets.QRadioButton(self.fr_Accion)
        self.b_efectivo.setGeometry(QtCore.QRect(30, 10, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b_efectivo.setFont(font)
        self.b_efectivo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_efectivo.setChecked(True)
        self.b_efectivo.setObjectName("b_efectivo")
        self.b_tarjeta = QtWidgets.QRadioButton(self.fr_Accion)
        self.b_tarjeta.setGeometry(QtCore.QRect(230, 10, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b_tarjeta.setFont(font)
        self.b_tarjeta.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_tarjeta.setChecked(False)
        self.b_tarjeta.setObjectName("b_tarjeta")
        self.L2 = QtWidgets.QLabel(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(0, 30, 391, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(18)
        self.L2.setFont(font)
        self.L2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.L2.setMidLineWidth(0)
        self.L2.setAlignment(QtCore.Qt.AlignCenter)
        self.L2.setObjectName("L2")
        self.L1 = QtWidgets.QLabel(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(0, 0, 391, 30))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.L1.setFont(font)
        self.L1.setAlignment(QtCore.Qt.AlignCenter)
        self.L1.setObjectName("L1")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 110, 391, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.L_Total = QtWidgets.QLabel(self.frame)
        self.L_Total.setGeometry(QtCore.QRect(10, 15, 80, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.L_Total.setFont(font)
        self.L_Total.setStyleSheet("")
        self.L_Total.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L_Total.setObjectName("L_Total")
        self.t_Total = QtWidgets.QLineEdit(self.frame)
        self.t_Total.setGeometry(QtCore.QRect(100, 10, 130, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.t_Total.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.t_Total.setFont(font)
        self.t_Total.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.t_Total.setAlignment(QtCore.Qt.AlignCenter)
        self.t_Total.setObjectName("t_Total")
        self.t_Pago = QtWidgets.QLineEdit(self.frame)
        self.t_Pago.setGeometry(QtCore.QRect(100, 50, 130, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.t_Pago.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.t_Pago.setFont(font)
        self.t_Pago.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.t_Pago.setAlignment(QtCore.Qt.AlignCenter)
        self.t_Pago.setObjectName("t_Pago")
        self.L_Total_2 = QtWidgets.QLabel(self.frame)
        self.L_Total_2.setGeometry(QtCore.QRect(10, 55, 80, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.L_Total_2.setFont(font)
        self.L_Total_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.L_Total_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L_Total_2.setObjectName("L_Total_2")
        self.t_Cambio = QtWidgets.QLineEdit(self.frame)
        self.t_Cambio.setGeometry(QtCore.QRect(100, 90, 130, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.t_Cambio.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.t_Cambio.setFont(font)
        self.t_Cambio.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.t_Cambio.setAlignment(QtCore.Qt.AlignCenter)
        self.t_Cambio.setObjectName("t_Cambio")
        self.L_Total_3 = QtWidgets.QLabel(self.frame)
        self.L_Total_3.setGeometry(QtCore.QRect(10, 95, 80, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.L_Total_3.setFont(font)
        self.L_Total_3.setStyleSheet("")
        self.L_Total_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L_Total_3.setObjectName("L_Total_3")
        self.b_Cobrar = QtWidgets.QPushButton(self.frame)
        self.b_Cobrar.setGeometry(QtCore.QRect(280, 10, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cobrar.setFont(font)
        self.b_Cobrar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Cobrar.setAutoDefault(True)
        self.b_Cobrar.setObjectName("b_Cobrar")
        self.b_Cancelar = QtWidgets.QPushButton(self.frame)
        self.b_Cancelar.setGeometry(QtCore.QRect(280, 90, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cancelar.setFont(font)
        self.b_Cancelar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Cancelar.setAutoDefault(True)
        self.b_Cancelar.setObjectName("b_Cancelar")
        self.L9 = QtWidgets.QLabel(self.centralwidget)
        self.L9.setGeometry(QtCore.QRect(340, 240, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L9.setFont(font)
        self.L9.setAlignment(QtCore.Qt.AlignCenter)
        self.L9.setObjectName("L9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.b_efectivo, self.b_tarjeta)
        MainWindow.setTabOrder(self.b_tarjeta, self.t_Total)
        MainWindow.setTabOrder(self.t_Total, self.t_Pago)
        MainWindow.setTabOrder(self.t_Pago, self.t_Cambio)
        MainWindow.setTabOrder(self.t_Cambio, self.b_Cobrar)
        MainWindow.setTabOrder(self.b_Cobrar, self.b_Cancelar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana de Cobro"))
        self.b_efectivo.setText(_translate("MainWindow", "Pago en Efectivo"))
        self.b_tarjeta.setText(_translate("MainWindow", "Pago con Tarjeta"))
        self.L2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Ventana de Cobro</span></p></body></html>"))
        self.L1.setText(_translate("MainWindow", "DanStore"))
        self.L_Total.setText(_translate("MainWindow", "TOTAL"))
        self.t_Total.setText(_translate("MainWindow", "$ 0.00"))
        self.t_Pago.setText(_translate("MainWindow", "$ 0.00"))
        self.L_Total_2.setText(_translate("MainWindow", "PAGO"))
        self.t_Cambio.setText(_translate("MainWindow", "$ 0.00"))
        self.L_Total_3.setText(_translate("MainWindow", "CAMBIO"))
        self.b_Cobrar.setText(_translate("MainWindow", "Cobrar"))
        self.b_Cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.L9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aaaaaa;\">v 1.0.0</span></p></body></html>"))
