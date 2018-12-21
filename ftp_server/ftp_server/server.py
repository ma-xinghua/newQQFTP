# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Desktop\server.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from get_ip import *
from config_ftp import *

class Ui_Dialog_server(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(443, 484)
        Dialog.setAutoFillBackground(True)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.line_2)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setIconSize(QtCore.QSize(13, 13))
        self.toolButton.setAutoRepeatDelay(300)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolButton.setObjectName("toolButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.toolButton)
        self.toolButton_4 = QtWidgets.QToolButton(Dialog)
        self.toolButton_4.setObjectName("toolButton_4")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.toolButton_4)
        self.toolButton_3 = QtWidgets.QToolButton(Dialog)
        self.toolButton_3.setObjectName("toolButton_3")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.toolButton_3)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setObjectName("toolButton_2")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.toolButton_2)
        self.toolButton_5 = QtWidgets.QToolButton(Dialog)
        self.toolButton_5.setObjectName("toolButton_5")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.toolButton_5)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.append(get_host_ip())
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setObjectName("textBrowser_2")
        port=str(passive_ports)[1:-1]+' 的任意端口'
        port1=port.replace(',',' 到')
        self.textBrowser_2.append(port1)
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.textBrowser_2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label)

        self.retranslateUi(Dialog)
        self.toolButton.clicked.connect(Dialog.newuser)
        self.toolButton_4.clicked.connect(Dialog.changeuser)
        self.toolButton_3.clicked.connect(Dialog.modify)
        self.toolButton_2.clicked.connect(Dialog.start)
        self.toolButton_5.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButton.setText(_translate("Dialog", "添加新用户"))
        self.toolButton_4.setText(_translate("Dialog", "修改账户"))
        self.toolButton_3.setText(_translate("Dialog", "端口配置"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">接下来，您可以：</span></p></body></html>"))
        self.toolButton_2.setText(_translate("Dialog", "开启服务器"))
        self.toolButton_5.setText(_translate("Dialog", "退出程序"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">服务器IP地址：</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">开放的端口号：</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">QQFTP服务器配置</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">欢迎使用QQFTP服务器！</span></p></body></html>"))

