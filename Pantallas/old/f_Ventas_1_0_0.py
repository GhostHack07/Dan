# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f_Ventas.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
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
        self.L1 = QtWidgets.QLabel(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(-1, 0, 841, 30))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.L1.setFont(font)
        self.L1.setAlignment(QtCore.Qt.AlignCenter)
        self.L1.setObjectName("L1")
        self.L2 = QtWidgets.QLabel(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(-1, 30, 841, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(18)
        self.L2.setFont(font)
        self.L2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.L2.setMidLineWidth(0)
        self.L2.setAlignment(QtCore.Qt.AlignCenter)
        self.L2.setObjectName("L2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 61, 831, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(134)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(134)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(850, 60, 151, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.b_Registrar = QtWidgets.QPushButton(self.frame)
        self.b_Registrar.setGeometry(QtCore.QRect(10, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar.setFont(font)
        self.b_Registrar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar.setStyleSheet("background-color: rgb(170, 200, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: navy;\n"
"border-radius: 14px;")
        self.b_Registrar.setAutoDefault(True)
        self.b_Registrar.setObjectName("b_Registrar")
        self.b_Registrar_2 = QtWidgets.QPushButton(self.frame)
        self.b_Registrar_2.setGeometry(QtCore.QRect(10, 50, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar_2.setFont(font)
        self.b_Registrar_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar_2.setStyleSheet("background-color: rgb(255, 230, 150);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: orange;\n"
"border-radius: 14px;")
        self.b_Registrar_2.setAutoDefault(True)
        self.b_Registrar_2.setObjectName("b_Registrar_2")
        self.b_Registrar_3 = QtWidgets.QPushButton(self.frame)
        self.b_Registrar_3.setGeometry(QtCore.QRect(10, 100, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar_3.setFont(font)
        self.b_Registrar_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar_3.setStyleSheet("background-color: rgb(250, 200, 170);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: darkred;\n"
"border-radius: 14px;")
        self.b_Registrar_3.setAutoDefault(True)
        self.b_Registrar_3.setObjectName("b_Registrar_3")
        self.b_Registrar_4 = QtWidgets.QPushButton(self.frame)
        self.b_Registrar_4.setGeometry(QtCore.QRect(10, 150, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar_4.setFont(font)
        self.b_Registrar_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar_4.setStyleSheet("background-color: rgb(135, 250, 120);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: green;\n"
"border-radius: 14px;")
        self.b_Registrar_4.setAutoDefault(True)
        self.b_Registrar_4.setObjectName("b_Registrar_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 520, 831, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.b_Registrar_5 = QtWidgets.QPushButton(self.frame_2)
        self.b_Registrar_5.setGeometry(QtCore.QRect(10, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar_5.setFont(font)
        self.b_Registrar_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar_5.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: gray;\n"
"border-radius: 14px;")
        self.b_Registrar_5.setAutoDefault(True)
        self.b_Registrar_5.setObjectName("b_Registrar_5")
        self.b_Registrar_6 = QtWidgets.QPushButton(self.frame_2)
        self.b_Registrar_6.setGeometry(QtCore.QRect(180, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar_6.setFont(font)
        self.b_Registrar_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar_6.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: gray;\n"
"border-radius: 14px;")
        self.b_Registrar_6.setAutoDefault(True)
        self.b_Registrar_6.setObjectName("b_Registrar_6")
        self.b_Registrar_7 = QtWidgets.QPushButton(self.frame_2)
        self.b_Registrar_7.setGeometry(QtCore.QRect(350, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar_7.setFont(font)
        self.b_Registrar_7.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar_7.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: gray;\n"
"border-radius: 14px;")
        self.b_Registrar_7.setAutoDefault(True)
        self.b_Registrar_7.setObjectName("b_Registrar_7")
        self.b_Registrar_8 = QtWidgets.QPushButton(self.frame_2)
        self.b_Registrar_8.setGeometry(QtCore.QRect(520, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar_8.setFont(font)
        self.b_Registrar_8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar_8.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: gray;\n"
"border-radius: 14px;")
        self.b_Registrar_8.setAutoDefault(True)
        self.b_Registrar_8.setObjectName("b_Registrar_8")
        self.b_Registrar_13 = QtWidgets.QPushButton(self.frame_2)
        self.b_Registrar_13.setGeometry(QtCore.QRect(690, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar_13.setFont(font)
        self.b_Registrar_13.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar_13.setStyleSheet("background-color: rgb(250, 200, 170);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: darkred;\n"
"border-radius: 14px;")
        self.b_Registrar_13.setAutoDefault(True)
        self.b_Registrar_13.setObjectName("b_Registrar_13")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(850, 270, 151, 301))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 70, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 130, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 190, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 260, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.L6 = QtWidgets.QLabel(self.centralwidget)
        self.L6.setGeometry(QtCore.QRect(940, 570, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L6.setFont(font)
        self.L6.setAlignment(QtCore.Qt.AlignCenter)
        self.L6.setObjectName("L6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(850, 0, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(850, 20, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(850, 40, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(930, 20, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(930, 0, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(930, 40, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.L1.setText(_translate("MainWindow", "Dan1"))
        self.L2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Registro de Ventas</span></p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SKU"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio Unitario"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Descuento"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Importe"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.b_Registrar.setText(_translate("MainWindow", "Actualizar"))
        self.b_Registrar_2.setText(_translate("MainWindow", "Eliminar"))
        self.b_Registrar_3.setText(_translate("MainWindow", "Cancelar"))
        self.b_Registrar_4.setText(_translate("MainWindow", "Cobrar"))
        self.b_Registrar_5.setText(_translate("MainWindow", "Usuarios"))
        self.b_Registrar_6.setText(_translate("MainWindow", "Cupón"))
        self.b_Registrar_7.setText(_translate("MainWindow", "Inventario"))
        self.b_Registrar_8.setText(_translate("MainWindow", "Ticket"))
        self.b_Registrar_13.setText(_translate("MainWindow", "Cerrar Sesión"))
        self.lineEdit.setText(_translate("MainWindow", "Ticket #0000"))
        self.lineEdit_2.setText(_translate("MainWindow", "$ 0.00"))
        self.label_2.setText(_translate("MainWindow", "Importe"))
        self.lineEdit_3.setText(_translate("MainWindow", "$ 0.00"))
        self.label_3.setText(_translate("MainWindow", "Descuento"))
        self.lineEdit_4.setText(_translate("MainWindow", "$ 0.00"))
        self.label_4.setText(_translate("MainWindow", "IVA"))
        self.lineEdit_5.setText(_translate("MainWindow", "$ 0.00"))
        self.label_5.setText(_translate("MainWindow", "TOTAL"))
        self.L6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aaaaaa;\">v 1.0.0</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Usuario:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Fecha:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Hora:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">F</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">U</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">H</span></p></body></html>"))