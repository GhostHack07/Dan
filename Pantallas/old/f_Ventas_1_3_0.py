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
        self.t_Ventas = QtWidgets.QTableWidget(self.centralwidget)
        self.t_Ventas.setGeometry(QtCore.QRect(10, 61, 831, 441))
        self.t_Ventas.setObjectName("t_Ventas")
        self.t_Ventas.setColumnCount(6)
        self.t_Ventas.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        item.setFont(font)
        self.t_Ventas.setVerticalHeaderItem(0, item)
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
        self.t_Ventas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_Ventas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_Ventas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_Ventas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_Ventas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_Ventas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.t_Ventas.setItem(0, 0, item)
        self.t_Ventas.horizontalHeader().setVisible(True)
        self.t_Ventas.horizontalHeader().setCascadingSectionResizes(False)
        self.t_Ventas.horizontalHeader().setDefaultSectionSize(134)
        self.t_Ventas.horizontalHeader().setMinimumSectionSize(134)
        self.t_Ventas.verticalHeader().setDefaultSectionSize(20)
        self.fr_Ventas = QtWidgets.QFrame(self.centralwidget)
        self.fr_Ventas.setGeometry(QtCore.QRect(850, 60, 151, 191))
        self.fr_Ventas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Ventas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Ventas.setObjectName("fr_Ventas")
        self.b_Actualizar = QtWidgets.QPushButton(self.fr_Ventas)
        self.b_Actualizar.setGeometry(QtCore.QRect(10, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Actualizar.setFont(font)
        self.b_Actualizar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Actualizar.setStyleSheet("background-color: rgb(170, 200, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: navy;\n"
"border-radius: 14px;")
        self.b_Actualizar.setAutoDefault(True)
        self.b_Actualizar.setObjectName("b_Actualizar")
        self.b_Eliminar = QtWidgets.QPushButton(self.fr_Ventas)
        self.b_Eliminar.setGeometry(QtCore.QRect(10, 50, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Eliminar.setFont(font)
        self.b_Eliminar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Eliminar.setStyleSheet("background-color: rgb(255, 230, 150);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: orange;\n"
"border-radius: 14px;")
        self.b_Eliminar.setAutoDefault(True)
        self.b_Eliminar.setObjectName("b_Eliminar")
        self.b_Cancelar = QtWidgets.QPushButton(self.fr_Ventas)
        self.b_Cancelar.setGeometry(QtCore.QRect(10, 100, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cancelar.setFont(font)
        self.b_Cancelar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Cancelar.setStyleSheet("background-color: rgb(250, 200, 170);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: darkred;\n"
"border-radius: 14px;")
        self.b_Cancelar.setAutoDefault(True)
        self.b_Cancelar.setObjectName("b_Cancelar")
        self.b_Cobrar = QtWidgets.QPushButton(self.fr_Ventas)
        self.b_Cobrar.setGeometry(QtCore.QRect(10, 150, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cobrar.setFont(font)
        self.b_Cobrar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Cobrar.setStyleSheet("background-color: rgb(135, 250, 120);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: green;\n"
"border-radius: 14px;")
        self.b_Cobrar.setAutoDefault(True)
        self.b_Cobrar.setObjectName("b_Cobrar")
        self.fr_botones = QtWidgets.QFrame(self.centralwidget)
        self.fr_botones.setGeometry(QtCore.QRect(10, 520, 831, 51))
        self.fr_botones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_botones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_botones.setObjectName("fr_botones")
        self.b_Usuarios = QtWidgets.QPushButton(self.fr_botones)
        self.b_Usuarios.setGeometry(QtCore.QRect(10, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Usuarios.setFont(font)
        self.b_Usuarios.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Usuarios.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: gray;\n"
"border-radius: 14px;")
        self.b_Usuarios.setAutoDefault(True)
        self.b_Usuarios.setObjectName("b_Usuarios")
        self.b_Cupon = QtWidgets.QPushButton(self.fr_botones)
        self.b_Cupon.setGeometry(QtCore.QRect(180, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cupon.setFont(font)
        self.b_Cupon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Cupon.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: gray;\n"
"border-radius: 14px;")
        self.b_Cupon.setAutoDefault(True)
        self.b_Cupon.setObjectName("b_Cupon")
        self.b_Inventario = QtWidgets.QPushButton(self.fr_botones)
        self.b_Inventario.setGeometry(QtCore.QRect(350, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Inventario.setFont(font)
        self.b_Inventario.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Inventario.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: gray;\n"
"border-radius: 14px;")
        self.b_Inventario.setAutoDefault(True)
        self.b_Inventario.setObjectName("b_Inventario")
        self.b_Ticket = QtWidgets.QPushButton(self.fr_botones)
        self.b_Ticket.setGeometry(QtCore.QRect(520, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Ticket.setFont(font)
        self.b_Ticket.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Ticket.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: gray;\n"
"border-radius: 14px;")
        self.b_Ticket.setAutoDefault(True)
        self.b_Ticket.setObjectName("b_Ticket")
        self.b_Cerrar = QtWidgets.QPushButton(self.fr_botones)
        self.b_Cerrar.setGeometry(QtCore.QRect(690, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cerrar.setFont(font)
        self.b_Cerrar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Cerrar.setStyleSheet("background-color: rgb(250, 200, 170);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: darkred;\n"
"border-radius: 14px;")
        self.b_Cerrar.setAutoDefault(True)
        self.b_Cerrar.setObjectName("b_Cerrar")
        self.fr_total = QtWidgets.QFrame(self.centralwidget)
        self.fr_total.setGeometry(QtCore.QRect(850, 270, 151, 301))
        self.fr_total.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_total.setObjectName("fr_total")
        self.t_Ticket = QtWidgets.QLineEdit(self.fr_total)
        self.t_Ticket.setGeometry(QtCore.QRect(10, 10, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.t_Ticket.setFont(font)
        self.t_Ticket.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.t_Ticket.setAlignment(QtCore.Qt.AlignCenter)
        self.t_Ticket.setObjectName("t_Ticket")
        self.t_Importe = QtWidgets.QLineEdit(self.fr_total)
        self.t_Importe.setGeometry(QtCore.QRect(10, 70, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.t_Importe.setFont(font)
        self.t_Importe.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.t_Importe.setAlignment(QtCore.Qt.AlignCenter)
        self.t_Importe.setObjectName("t_Importe")
        self.label_2 = QtWidgets.QLabel(self.fr_total)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.t_Descuento = QtWidgets.QLineEdit(self.fr_total)
        self.t_Descuento.setGeometry(QtCore.QRect(10, 130, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.t_Descuento.setFont(font)
        self.t_Descuento.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.t_Descuento.setAlignment(QtCore.Qt.AlignCenter)
        self.t_Descuento.setObjectName("t_Descuento")
        self.label_3 = QtWidgets.QLabel(self.fr_total)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.t_IVA = QtWidgets.QLineEdit(self.fr_total)
        self.t_IVA.setGeometry(QtCore.QRect(10, 190, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.t_IVA.setFont(font)
        self.t_IVA.setStyleSheet("QLineEdit {\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
" }")
        self.t_IVA.setAlignment(QtCore.Qt.AlignCenter)
        self.t_IVA.setObjectName("t_IVA")
        self.label_4 = QtWidgets.QLabel(self.fr_total)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.t_Total = QtWidgets.QLineEdit(self.fr_total)
        self.t_Total.setGeometry(QtCore.QRect(10, 260, 130, 30))
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
        self.label_5 = QtWidgets.QLabel(self.fr_total)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.L9 = QtWidgets.QLabel(self.centralwidget)
        self.L9.setGeometry(QtCore.QRect(940, 570, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L9.setFont(font)
        self.L9.setAlignment(QtCore.Qt.AlignCenter)
        self.L9.setObjectName("L9")
        self.L3 = QtWidgets.QLabel(self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(850, 0, 50, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L3.setFont(font)
        self.L3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L3.setObjectName("L3")
        self.L4 = QtWidgets.QLabel(self.centralwidget)
        self.L4.setGeometry(QtCore.QRect(850, 20, 50, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L4.setFont(font)
        self.L4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L4.setObjectName("L4")
        self.L6 = QtWidgets.QLabel(self.centralwidget)
        self.L6.setGeometry(QtCore.QRect(910, 20, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L6.setFont(font)
        self.L6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L6.setObjectName("L6")
        self.L5 = QtWidgets.QLabel(self.centralwidget)
        self.L5.setGeometry(QtCore.QRect(910, 0, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L5.setFont(font)
        self.L5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L5.setObjectName("L5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.L1.setText(_translate("MainWindow", "Dan1"))
        self.L2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Registro de Ventas</span></p></body></html>"))
        item = self.t_Ventas.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.t_Ventas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SKU"))
        item = self.t_Ventas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.t_Ventas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.t_Ventas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio Unitario"))
        item = self.t_Ventas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Descuento"))
        item = self.t_Ventas.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Importe"))
        __sortingEnabled = self.t_Ventas.isSortingEnabled()
        self.t_Ventas.setSortingEnabled(False)
        self.t_Ventas.setSortingEnabled(__sortingEnabled)
        self.b_Actualizar.setText(_translate("MainWindow", "Actualizar"))
        self.b_Eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.b_Cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.b_Cobrar.setText(_translate("MainWindow", "Cobrar"))
        self.b_Usuarios.setText(_translate("MainWindow", "Usuarios"))
        self.b_Cupon.setText(_translate("MainWindow", "Cupón"))
        self.b_Inventario.setText(_translate("MainWindow", "Inventario"))
        self.b_Ticket.setText(_translate("MainWindow", "Ticket"))
        self.b_Cerrar.setText(_translate("MainWindow", "Cerrar Sesión"))
        self.t_Ticket.setText(_translate("MainWindow", "Ticket #0000"))
        self.t_Importe.setText(_translate("MainWindow", "$ 0.00"))
        self.label_2.setText(_translate("MainWindow", "Importe"))
        self.t_Descuento.setText(_translate("MainWindow", "$ 0.00"))
        self.label_3.setText(_translate("MainWindow", "Descuento"))
        self.t_IVA.setText(_translate("MainWindow", "$ 0.00"))
        self.label_4.setText(_translate("MainWindow", "IVA"))
        self.t_Total.setText(_translate("MainWindow", "$ 0.00"))
        self.label_5.setText(_translate("MainWindow", "TOTAL"))
        self.L9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aaaaaa;\">v 1.3.0</span></p></body></html>"))
        self.L3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#aaaaaa;\">Usuario:</span></p></body></html>"))
        self.L4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#aaaaaa;\">Nivel:</span></p></body></html>"))
        self.L6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#aaaaaa;\">N</span></p></body></html>"))
        self.L5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#aaaaaa;\">U</span></p></body></html>"))
