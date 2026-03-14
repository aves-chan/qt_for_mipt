# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(295, 174)
        self.verticalLayout = QVBoxLayout(dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.dateEdit = QDateEdit(dialog)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout.addWidget(self.dateEdit)

        self.lineEdit = QLineEdit(dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.comboBox = QComboBox(dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("dialog", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("dialog", u"\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

