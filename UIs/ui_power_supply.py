# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_supplyprPLlR.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_powerSupply(object):
    def setupUi(self, powerSupply):
        if not powerSupply.objectName():
            powerSupply.setObjectName(u"powerSupply")
        powerSupply.resize(551, 328)
        self.horizontalLayout = QHBoxLayout(powerSupply)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_7 = QFrame(powerSupply)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(260, 0))
        self.frame_7.setMaximumSize(QSize(260, 16777215))
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 40))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.comboBox = QComboBox(self.frame_6)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lineEdit)

        self.parameters = QWidget(self.frame_7)
        self.parameters.setObjectName(u"parameters")
        self.parameters.setMinimumSize(QSize(250, 210))
        self.parameters.setMaximumSize(QSize(250, 210))
        self.horizontalLayout_4 = QHBoxLayout(self.parameters)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.parameters)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.step = QDoubleSpinBox(self.frame_5)
        self.step.setObjectName(u"step")

        self.gridLayout_2.addWidget(self.step, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.stop = QDoubleSpinBox(self.frame_5)
        self.stop.setObjectName(u"stop")

        self.gridLayout_2.addWidget(self.stop, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.start = QDoubleSpinBox(self.frame_5)
        self.start.setObjectName(u"start")

        self.gridLayout_2.addWidget(self.start, 0, 1, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.parameters)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.items = QListWidget(self.frame_4)
        self.items.setObjectName(u"items")

        self.verticalLayout_5.addWidget(self.items)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add = QPushButton(self.frame_3)
        self.add.setObjectName(u"add")

        self.horizontalLayout_3.addWidget(self.add)

        self.clear = QPushButton(self.frame_3)
        self.clear.setObjectName(u"clear")

        self.horizontalLayout_3.addWidget(self.clear)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.parameters)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(powerSupply)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(200, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.Box)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.checkBox = QCheckBox(self.frame_8)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_7.addWidget(self.checkBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.checkBox_2 = QCheckBox(self.frame_8)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_6.addWidget(self.checkBox_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 315, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(powerSupply)

        QMetaObject.connectSlotsByName(powerSupply)
    # setupUi

    def retranslateUi(self, powerSupply):
        powerSupply.setWindowTitle(QCoreApplication.translate("powerSupply", u"Form", None))
        self.label_11.setText(QCoreApplication.translate("powerSupply", u"address", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("powerSupply", u"select address", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("powerSupply", u"enter measurement name", None))
        self.label_10.setText(QCoreApplication.translate("powerSupply", u"step", None))
        self.label_8.setText(QCoreApplication.translate("powerSupply", u"start", None))
        self.label_9.setText(QCoreApplication.translate("powerSupply", u"stop", None))
        self.add.setText(QCoreApplication.translate("powerSupply", u"add", None))
        self.clear.setText(QCoreApplication.translate("powerSupply", u"clear", None))
        self.label_14.setText(QCoreApplication.translate("powerSupply", u"Idenify", None))
        self.checkBox.setText(QCoreApplication.translate("powerSupply", u"idenify", None))
        self.label_12.setText(QCoreApplication.translate("powerSupply", u"TextLabel", None))
        self.checkBox_2.setText(QCoreApplication.translate("powerSupply", u"output", None))
    # retranslateUi
