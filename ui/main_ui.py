# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(726, 228)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setBold(True)
        self.centralwidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_balance = QLabel(self.centralwidget)
        self.label_balance.setObjectName(u"label_balance")

        self.horizontalLayout.addWidget(self.label_balance)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_outcome = QLabel(self.centralwidget)
        self.label_outcome.setObjectName(u"label_outcome")

        self.horizontalLayout_4.addWidget(self.label_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_income = QLabel(self.centralwidget)
        self.label_income.setObjectName(u"label_income")

        self.horizontalLayout_2.addWidget(self.label_income)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_new = QPushButton(self.centralwidget)
        self.pushButton_new.setObjectName(u"pushButton_new")

        self.horizontalLayout_5.addWidget(self.pushButton_new)

        self.pushButton_remove = QPushButton(self.centralwidget)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.horizontalLayout_5.addWidget(self.pushButton_remove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty(u"showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_2.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"expense tracker", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441: ", None))
        self.label_balance.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b: ", None))
        self.label_outcome.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b: ", None))
        self.label_income.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_new.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e", None))
        self.pushButton_remove.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e", None))
    # retranslateUi

