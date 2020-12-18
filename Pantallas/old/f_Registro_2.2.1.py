# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f_Registro.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(260, 400))
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
        self.L4.setGeometry(QtCore.QRect(10, 240, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(14)
        self.L4.setFont(font)
        self.L4.setObjectName("L4")
        self.D_psw = QtWidgets.QLineEdit(self.centralwidget)
        self.D_psw.setGeometry(QtCore.QRect(100, 240, 150, 20))
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
        self.D_psw.setFocusPolicy(QtCore.Qt.StrongFocus)
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
        self.b_Cancelar.setGeometry(QtCore.QRect(150, 350, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Cancelar.setFont(font)
        self.b_Cancelar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Cancelar.setObjectName("b_Cancelar")
        self.L3 = QtWidgets.QLabel(self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(10, 150, 80, 20))
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
        self.D_usuario.setGeometry(QtCore.QRect(100, 150, 150, 20))
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
        self.b_Registrar = QtWidgets.QPushButton(self.centralwidget)
        self.b_Registrar.setGeometry(QtCore.QRect(10, 350, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(12)
        self.b_Registrar.setFont(font)
        self.b_Registrar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_Registrar.setObjectName("b_Registrar")
        self.L6 = QtWidgets.QLabel(self.centralwidget)
        self.L6.setGeometry(QtCore.QRect(200, 380, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.L6.setFont(font)
        self.L6.setAlignment(QtCore.Qt.AlignCenter)
        self.L6.setObjectName("L6")
        self.D_psw_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.D_psw_2.setGeometry(QtCore.QRect(100, 270, 150, 20))
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
        self.D_psw_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.D_psw_2.setFont(font)
        self.D_psw_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.D_psw_2.setMaxLength(10)
        self.D_psw_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.D_psw_2.setObjectName("D_psw_2")
        self.L5 = QtWidgets.QLabel(self.centralwidget)
        self.L5.setGeometry(QtCore.QRect(10, 270, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(14)
        self.L5.setFont(font)
        self.L5.setObjectName("L5")
        self.fr_Nivel = QtWidgets.QFrame(self.centralwidget)
        self.fr_Nivel.setGeometry(QtCore.QRect(9, 300, 241, 40))
        self.fr_Nivel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Nivel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Nivel.setObjectName("fr_Nivel")
        self.b_emp = QtWidgets.QRadioButton(self.fr_Nivel)
        self.b_emp.setGeometry(QtCore.QRect(10, 10, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b_emp.setFont(font)
        self.b_emp.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_emp.setChecked(True)
        self.b_emp.setObjectName("b_emp")
        self.b_adm = QtWidgets.QRadioButton(self.fr_Nivel)
        self.b_adm.setGeometry(QtCore.QRect(120, 10, 115, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b_adm.setFont(font)
        self.b_adm.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_adm.setObjectName("b_adm")
        self.fr_Accion = QtWidgets.QFrame(self.centralwidget)
        self.fr_Accion.setGeometry(QtCore.QRect(4, 60, 251, 40))
        self.fr_Accion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Accion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Accion.setObjectName("fr_Accion")
        self.b_nuevo = QtWidgets.QRadioButton(self.fr_Accion)
        self.b_nuevo.setGeometry(QtCore.QRect(10, 10, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b_nuevo.setFont(font)
        self.b_nuevo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_nuevo.setChecked(True)
        self.b_nuevo.setObjectName("b_nuevo")
        self.b_eliminar = QtWidgets.QRadioButton(self.fr_Accion)
        self.b_eliminar.setGeometry(QtCore.QRect(170, 10, 80, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b_eliminar.setFont(font)
        self.b_eliminar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_eliminar.setObjectName("b_eliminar")
        self.b_actualizar = QtWidgets.QRadioButton(self.fr_Accion)
        self.b_actualizar.setGeometry(QtCore.QRect(80, 10, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b_actualizar.setFont(font)
        self.b_actualizar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b_actualizar.setChecked(False)
        self.b_actualizar.setObjectName("b_actualizar")
        self.L7 = QtWidgets.QLabel(self.centralwidget)
        self.L7.setGeometry(QtCore.QRect(10, 210, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(14)
        self.L7.setFont(font)
        self.L7.setObjectName("L7")
        self.D_psw_old = QtWidgets.QLineEdit(self.centralwidget)
        self.D_psw_old.setGeometry(QtCore.QRect(100, 210, 150, 20))
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
        self.D_psw_old.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.D_psw_old.setFont(font)
        self.D_psw_old.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.D_psw_old.setMaxLength(10)
        self.D_psw_old.setEchoMode(QtWidgets.QLineEdit.Password)
        self.D_psw_old.setObjectName("D_psw_old")
        self.L8 = QtWidgets.QLabel(self.centralwidget)
        self.L8.setGeometry(QtCore.QRect(10, 180, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(14)
        self.L8.setFont(font)
        self.L8.setObjectName("L8")
        self.D_usuario_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.D_usuario_2.setGeometry(QtCore.QRect(100, 180, 150, 20))
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
        self.D_usuario_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.D_usuario_2.setFont(font)
        self.D_usuario_2.setText("")
        self.D_usuario_2.setMaxLength(10)
        self.D_usuario_2.setObjectName("D_usuario_2")
        self.fr_Actualizacion = QtWidgets.QFrame(self.centralwidget)
        self.fr_Actualizacion.setGeometry(QtCore.QRect(4, 100, 251, 40))
        self.fr_Actualizacion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Actualizacion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Actualizacion.setObjectName("fr_Actualizacion")
        self.ch_Usuario = QtWidgets.QCheckBox(self.fr_Actualizacion)
        self.ch_Usuario.setGeometry(QtCore.QRect(12, 10, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ch_Usuario.setFont(font)
        self.ch_Usuario.setObjectName("ch_Usuario")
        self.ch_psw = QtWidgets.QCheckBox(self.fr_Actualizacion)
        self.ch_psw.setGeometry(QtCore.QRect(90, 10, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ch_psw.setFont(font)
        self.ch_psw.setObjectName("ch_psw")
        self.ch_Nivel = QtWidgets.QCheckBox(self.fr_Actualizacion)
        self.ch_Nivel.setGeometry(QtCore.QRect(190, 10, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ch_Nivel.setFont(font)
        self.ch_Nivel.setObjectName("ch_Nivel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.b_nuevo, self.b_actualizar)
        MainWindow.setTabOrder(self.b_actualizar, self.b_eliminar)
        MainWindow.setTabOrder(self.b_eliminar, self.ch_Usuario)
        MainWindow.setTabOrder(self.ch_Usuario, self.ch_psw)
        MainWindow.setTabOrder(self.ch_psw, self.ch_Nivel)
        MainWindow.setTabOrder(self.ch_Nivel, self.D_usuario)
        MainWindow.setTabOrder(self.D_usuario, self.D_usuario_2)
        MainWindow.setTabOrder(self.D_usuario_2, self.D_psw_old)
        MainWindow.setTabOrder(self.D_psw_old, self.D_psw)
        MainWindow.setTabOrder(self.D_psw, self.D_psw_2)
        MainWindow.setTabOrder(self.D_psw_2, self.b_emp)
        MainWindow.setTabOrder(self.b_emp, self.b_adm)
        MainWindow.setTabOrder(self.b_adm, self.b_Registrar)
        MainWindow.setTabOrder(self.b_Registrar, self.b_Cancelar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestion de Usuarios"))
        self.L4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Contraseña</span></p></body></html>"))
        self.L2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Gestión de Usuarios</span></p></body></html>"))
        self.b_Cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.L3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Usuario</span></p></body></html>"))
        self.L1.setText(_translate("MainWindow", "Dan1"))
        self.b_Registrar.setText(_translate("MainWindow", "Registrar"))
        self.L6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aaaaaa;\">v 2.2.1</span></p></body></html>"))
        self.L5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Confirmar</span></p></body></html>"))
        self.b_emp.setText(_translate("MainWindow", "Empleado"))
        self.b_adm.setText(_translate("MainWindow", "Administrador"))
        self.b_nuevo.setText(_translate("MainWindow", "Nuevo"))
        self.b_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.b_actualizar.setText(_translate("MainWindow", "Actualizar"))
        self.L7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Anterior</span></p></body></html>"))
        self.L8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">Nvo. Usuario</span></p></body></html>"))
        self.ch_Usuario.setText(_translate("MainWindow", "Usuario"))
        self.ch_psw.setText(_translate("MainWindow", "Contraseña"))
        self.ch_Nivel.setText(_translate("MainWindow", "Nivel"))
