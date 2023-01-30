# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(416, 618)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.topLevelLayout = QHBoxLayout(Dialog)
        self.topLevelLayout.setObjectName(u"topLevelLayout")
        self.topLevelLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.mainctrlVerticalLayout = QVBoxLayout()
        self.mainctrlVerticalLayout.setObjectName(u"mainctrlVerticalLayout")
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.selectImgBtn = QPushButton(self.groupBox_3)
        self.selectImgBtn.setObjectName(u"selectImgBtn")

        self.horizontalLayout_3.addWidget(self.selectImgBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(2)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(4)
        self.yAxisMaxImgPxX_Lbl = QLabel(self.groupBox)
        self.yAxisMaxImgPxX_Lbl.setObjectName(u"yAxisMaxImgPxX_Lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.yAxisMaxImgPxX_Lbl)

        self.yAxisMaxImgPxX = QLineEdit(self.groupBox)
        self.yAxisMaxImgPxX.setObjectName(u"yAxisMaxImgPxX")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.yAxisMaxImgPxX)

        self.yAxisMaxImgPxY_Lbl = QLabel(self.groupBox)
        self.yAxisMaxImgPxY_Lbl.setObjectName(u"yAxisMaxImgPxY_Lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.yAxisMaxImgPxY_Lbl)

        self.yAxisMaxImgPxY = QLineEdit(self.groupBox)
        self.yAxisMaxImgPxY.setObjectName(u"yAxisMaxImgPxY")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.yAxisMaxImgPxY)

        self.yAxisMaxDataValue_Lbl = QLabel(self.groupBox)
        self.yAxisMaxDataValue_Lbl.setObjectName(u"yAxisMaxDataValue_Lbl")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.yAxisMaxDataValue_Lbl)

        self.yAxisMaxDataValue = QLineEdit(self.groupBox)
        self.yAxisMaxDataValue.setObjectName(u"yAxisMaxDataValue")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.yAxisMaxDataValue)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(4)
        self.yAxisMinImgPxX_Lbl = QLabel(self.groupBox)
        self.yAxisMinImgPxX_Lbl.setObjectName(u"yAxisMinImgPxX_Lbl")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.yAxisMinImgPxX_Lbl)

        self.yAxisMinImgPxX = QLineEdit(self.groupBox)
        self.yAxisMinImgPxX.setObjectName(u"yAxisMinImgPxX")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.yAxisMinImgPxX)

        self.yAxisMinImgPxY_Lbl = QLabel(self.groupBox)
        self.yAxisMinImgPxY_Lbl.setObjectName(u"yAxisMinImgPxY_Lbl")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.yAxisMinImgPxY_Lbl)

        self.yAxisMinImgPxY = QLineEdit(self.groupBox)
        self.yAxisMinImgPxY.setObjectName(u"yAxisMinImgPxY")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.yAxisMinImgPxY)

        self.yAxisMinDataValue_Lbl = QLabel(self.groupBox)
        self.yAxisMinDataValue_Lbl.setObjectName(u"yAxisMinDataValue_Lbl")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.yAxisMinDataValue_Lbl)

        self.yAxisMinDataValue = QLineEdit(self.groupBox)
        self.yAxisMinDataValue.setObjectName(u"yAxisMinDataValue")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.yAxisMinDataValue)


        self.gridLayout.addLayout(self.formLayout_2, 1, 1, 1, 1)

        self.yAxisMaxBtn = QPushButton(self.groupBox)
        self.yAxisMaxBtn.setObjectName(u"yAxisMaxBtn")

        self.gridLayout.addWidget(self.yAxisMaxBtn, 0, 0, 1, 1)

        self.yAxisMinBtn = QPushButton(self.groupBox)
        self.yAxisMinBtn.setObjectName(u"yAxisMinBtn")

        self.gridLayout.addWidget(self.yAxisMinBtn, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yAxisTypeLbl = QLabel(self.groupBox)
        self.yAxisTypeLbl.setObjectName(u"yAxisTypeLbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.yAxisTypeLbl.sizePolicy().hasHeightForWidth())
        self.yAxisTypeLbl.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.yAxisTypeLbl)

        self.yAxisTypeCombox = QComboBox(self.groupBox)
        self.yAxisTypeCombox.setObjectName(u"yAxisTypeCombox")

        self.horizontalLayout.addWidget(self.yAxisTypeCombox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(8)
        self.gridLayout_2.setVerticalSpacing(2)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(4)
        self.xAxisMaxImgPxX_Lbl = QLabel(self.groupBox_2)
        self.xAxisMaxImgPxX_Lbl.setObjectName(u"xAxisMaxImgPxX_Lbl")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.xAxisMaxImgPxX_Lbl)

        self.xAxisMaxImgPxX = QLineEdit(self.groupBox_2)
        self.xAxisMaxImgPxX.setObjectName(u"xAxisMaxImgPxX")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.xAxisMaxImgPxX)

        self.xAxisMaxImgPxY_Lbl = QLabel(self.groupBox_2)
        self.xAxisMaxImgPxY_Lbl.setObjectName(u"xAxisMaxImgPxY_Lbl")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.xAxisMaxImgPxY_Lbl)

        self.xAxisMaxImgPxY = QLineEdit(self.groupBox_2)
        self.xAxisMaxImgPxY.setObjectName(u"xAxisMaxImgPxY")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.xAxisMaxImgPxY)

        self.xAxisMaxDataValue_Lbl = QLabel(self.groupBox_2)
        self.xAxisMaxDataValue_Lbl.setObjectName(u"xAxisMaxDataValue_Lbl")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.xAxisMaxDataValue_Lbl)

        self.xAxisMaxDataValue = QLineEdit(self.groupBox_2)
        self.xAxisMaxDataValue.setObjectName(u"xAxisMaxDataValue")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.xAxisMaxDataValue)


        self.gridLayout_2.addLayout(self.formLayout_3, 1, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(4)
        self.xAxisMinImgPxX_Lbl = QLabel(self.groupBox_2)
        self.xAxisMinImgPxX_Lbl.setObjectName(u"xAxisMinImgPxX_Lbl")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.xAxisMinImgPxX_Lbl)

        self.xAxisMinImgPxX = QLineEdit(self.groupBox_2)
        self.xAxisMinImgPxX.setObjectName(u"xAxisMinImgPxX")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.xAxisMinImgPxX)

        self.xAxisMinImgPxY_Lbl = QLabel(self.groupBox_2)
        self.xAxisMinImgPxY_Lbl.setObjectName(u"xAxisMinImgPxY_Lbl")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.xAxisMinImgPxY_Lbl)

        self.xAxisMinImgPxY = QLineEdit(self.groupBox_2)
        self.xAxisMinImgPxY.setObjectName(u"xAxisMinImgPxY")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.xAxisMinImgPxY)

        self.xAxisMinDataValue_Lbl = QLabel(self.groupBox_2)
        self.xAxisMinDataValue_Lbl.setObjectName(u"xAxisMinDataValue_Lbl")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.xAxisMinDataValue_Lbl)

        self.xAxisMinDataValue = QLineEdit(self.groupBox_2)
        self.xAxisMinDataValue.setObjectName(u"xAxisMinDataValue")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.xAxisMinDataValue)


        self.gridLayout_2.addLayout(self.formLayout_4, 1, 1, 1, 1)

        self.xAxisMaxBtn = QPushButton(self.groupBox_2)
        self.xAxisMaxBtn.setObjectName(u"xAxisMaxBtn")

        self.gridLayout_2.addWidget(self.xAxisMaxBtn, 0, 0, 1, 1)

        self.xAxisMinBtn = QPushButton(self.groupBox_2)
        self.xAxisMinBtn.setObjectName(u"xAxisMinBtn")

        self.gridLayout_2.addWidget(self.xAxisMinBtn, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.yAxisTypeLbl_2 = QLabel(self.groupBox_2)
        self.yAxisTypeLbl_2.setObjectName(u"yAxisTypeLbl_2")
        sizePolicy2.setHeightForWidth(self.yAxisTypeLbl_2.sizePolicy().hasHeightForWidth())
        self.yAxisTypeLbl_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.yAxisTypeLbl_2)

        self.yAxisTypeCombox_2 = QComboBox(self.groupBox_2)
        self.yAxisTypeCombox_2.setObjectName(u"yAxisTypeCombox_2")

        self.horizontalLayout_2.addWidget(self.yAxisTypeCombox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_4 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.clearDataBtn = QPushButton(self.groupBox_3)
        self.clearDataBtn.setObjectName(u"clearDataBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.clearDataBtn.sizePolicy().hasHeightForWidth())
        self.clearDataBtn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.clearDataBtn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.mainctrlVerticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy4)
        self.groupBox_4.setMaximumSize(QSize(396, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.clearDataBtn_2 = QPushButton(self.groupBox_4)
        self.clearDataBtn_2.setObjectName(u"clearDataBtn_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.clearDataBtn_2.sizePolicy().hasHeightForWidth())
        self.clearDataBtn_2.setSizePolicy(sizePolicy5)

        self.verticalLayout_7.addWidget(self.clearDataBtn_2)

        self.clearDataBtn_3 = QPushButton(self.groupBox_4)
        self.clearDataBtn_3.setObjectName(u"clearDataBtn_3")
        sizePolicy5.setHeightForWidth(self.clearDataBtn_3.sizePolicy().hasHeightForWidth())
        self.clearDataBtn_3.setSizePolicy(sizePolicy5)

        self.verticalLayout_7.addWidget(self.clearDataBtn_3)

        self.clearDataBtn_4 = QPushButton(self.groupBox_4)
        self.clearDataBtn_4.setObjectName(u"clearDataBtn_4")
        sizePolicy5.setHeightForWidth(self.clearDataBtn_4.sizePolicy().hasHeightForWidth())
        self.clearDataBtn_4.setSizePolicy(sizePolicy5)

        self.verticalLayout_7.addWidget(self.clearDataBtn_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.selectedPtsNumLbl = QLabel(self.groupBox_4)
        self.selectedPtsNumLbl.setObjectName(u"selectedPtsNumLbl")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.selectedPtsNumLbl.sizePolicy().hasHeightForWidth())
        self.selectedPtsNumLbl.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.selectedPtsNumLbl)

        self.selectedPtsNumDispLbl = QLabel(self.groupBox_4)
        self.selectedPtsNumDispLbl.setObjectName(u"selectedPtsNumDispLbl")
        sizePolicy4.setHeightForWidth(self.selectedPtsNumDispLbl.sizePolicy().hasHeightForWidth())
        self.selectedPtsNumDispLbl.setSizePolicy(sizePolicy4)
        self.selectedPtsNumDispLbl.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_7.addWidget(self.selectedPtsNumDispLbl)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.polyIdxLbl = QLabel(self.groupBox_4)
        self.polyIdxLbl.setObjectName(u"polyIdxLbl")
        sizePolicy6.setHeightForWidth(self.polyIdxLbl.sizePolicy().hasHeightForWidth())
        self.polyIdxLbl.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.polyIdxLbl)

        self.polyIdxEdit = QLineEdit(self.groupBox_4)
        self.polyIdxEdit.setObjectName(u"polyIdxEdit")
        sizePolicy5.setHeightForWidth(self.polyIdxEdit.sizePolicy().hasHeightForWidth())
        self.polyIdxEdit.setSizePolicy(sizePolicy5)
        self.polyIdxEdit.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_6.addWidget(self.polyIdxEdit)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_5 = QSpacerItem(101, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)

        self.verticalLayout_5.addWidget(self.label)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.axisDataSetLbl_17 = QLabel(self.groupBox_4)
        self.axisDataSetLbl_17.setObjectName(u"axisDataSetLbl_17")
        sizePolicy3.setHeightForWidth(self.axisDataSetLbl_17.sizePolicy().hasHeightForWidth())
        self.axisDataSetLbl_17.setSizePolicy(sizePolicy3)
        self.axisDataSetLbl_17.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.axisDataSetLbl_17)

        self.count_x_Edit = QLineEdit(self.groupBox_4)
        self.count_x_Edit.setObjectName(u"count_x_Edit")
        sizePolicy5.setHeightForWidth(self.count_x_Edit.sizePolicy().hasHeightForWidth())
        self.count_x_Edit.setSizePolicy(sizePolicy5)
        self.count_x_Edit.setMaximumSize(QSize(80, 16777215))

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.count_x_Edit)

        self.axisDataSetLbl_18 = QLabel(self.groupBox_4)
        self.axisDataSetLbl_18.setObjectName(u"axisDataSetLbl_18")
        sizePolicy3.setHeightForWidth(self.axisDataSetLbl_18.sizePolicy().hasHeightForWidth())
        self.axisDataSetLbl_18.setSizePolicy(sizePolicy3)
        self.axisDataSetLbl_18.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.axisDataSetLbl_18)

        self.counted_y_Edit = QLineEdit(self.groupBox_4)
        self.counted_y_Edit.setObjectName(u"counted_y_Edit")
        self.counted_y_Edit.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.counted_y_Edit.sizePolicy().hasHeightForWidth())
        self.counted_y_Edit.setSizePolicy(sizePolicy5)
        self.counted_y_Edit.setMaximumSize(QSize(80, 16777215))
        self.counted_y_Edit.setReadOnly(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.counted_y_Edit)


        self.verticalLayout_5.addLayout(self.formLayout_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)


        self.mainctrlVerticalLayout.addWidget(self.groupBox_4)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainctrlVerticalLayout.addItem(self.verticalSpacer_2)


        self.topLevelLayout.addLayout(self.mainctrlVerticalLayout)


        self.retranslateUi(Dialog)
        self.selectImgBtn.clicked.connect(Dialog.select_img_btn_clicked)
        self.xAxisMinBtn.clicked.connect(Dialog.x_axis_min_btn_clicked)
        self.yAxisMaxBtn.clicked.connect(Dialog.y_axis_max_btn_clicked)
        self.yAxisMinBtn.clicked.connect(Dialog.y_axis_min_btn_clicked)
        self.xAxisMaxBtn.clicked.connect(Dialog.x_axis_max_btn_clicked)
        self.xAxisMinImgPxX.editingFinished.connect(Dialog.x_axis_min_pxX_finished)
        self.xAxisMinImgPxY.editingFinished.connect(Dialog.x_axis_min_pxY_finished)
        self.xAxisMinDataValue.editingFinished.connect(Dialog.x_axis_min_dv_finished)
        self.xAxisMaxImgPxX.editingFinished.connect(Dialog.x_axis_max_pxX_finished)
        self.xAxisMaxImgPxY.editingFinished.connect(Dialog.x_axis_max_pxY_finished)
        self.xAxisMaxDataValue.editingFinished.connect(Dialog.x_axis_max_dv_finished)
        self.yAxisMaxImgPxX.editingFinished.connect(Dialog.y_axis_max_pxX_finished)
        self.yAxisMaxImgPxY.editingFinished.connect(Dialog.y_axis_max_pxY_finished)
        self.yAxisMaxDataValue.editingFinished.connect(Dialog.y_axis_max_dv_finished)
        self.yAxisMinImgPxX.editingFinished.connect(Dialog.y_axis_min_pxX_finished)
        self.yAxisMinImgPxY.editingFinished.connect(Dialog.y_axis_min_pxY_finished)
        self.yAxisMinDataValue.editingFinished.connect(Dialog.y_axis_min_dv_finished)
        self.clearDataBtn_2.clicked.connect(Dialog.save_selected_points)
        self.clearDataBtn_4.clicked.connect(Dialog.fitting_btn_clicked)
        self.count_x_Edit.returnPressed.connect(Dialog.count_data_accord_fitting)
        self.clearDataBtn.clicked.connect(Dialog.clear_axis_datum)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u539f\u59cb\u56fe\u50cf\u53c2\u6570", None))
        self.selectImgBtn.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u56fe\u7247", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"y\u8f74\u8bbe\u7f6e", None))
        self.yAxisMaxImgPxX_Lbl.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cfx\u5750\u6807", None))
        self.yAxisMaxImgPxY_Lbl.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cfy\u5750\u6807", None))
        self.yAxisMaxDataValue_Lbl.setText(QCoreApplication.translate("Dialog", u"\u5b9e\u9645\u6570\u503c", None))
        self.yAxisMinImgPxX_Lbl.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cfx\u5750\u6807", None))
        self.yAxisMinImgPxY_Lbl.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cfy\u5750\u6807", None))
        self.yAxisMinDataValue_Lbl.setText(QCoreApplication.translate("Dialog", u"\u5b9e\u9645\u6570\u503c", None))
        self.yAxisMaxBtn.setText(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6ey\u8f74\u6700\u5927\u503c", None))
        self.yAxisMinBtn.setText(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6ey\u8f74\u6700\u5c0f\u503c", None))
        self.yAxisTypeLbl.setText(QCoreApplication.translate("Dialog", u"y\u8f74\u7c7b\u578b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"x\u8f74\u8bbe\u7f6e", None))
        self.xAxisMaxImgPxX_Lbl.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cfx\u5750\u6807", None))
        self.xAxisMaxImgPxY_Lbl.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cfy\u5750\u6807", None))
        self.xAxisMaxDataValue_Lbl.setText(QCoreApplication.translate("Dialog", u"\u5b9e\u9645\u6570\u503c", None))
        self.xAxisMinImgPxX_Lbl.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cfx\u5750\u6807", None))
        self.xAxisMinImgPxY_Lbl.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cfy\u5750\u6807", None))
        self.xAxisMinDataValue_Lbl.setText(QCoreApplication.translate("Dialog", u"\u5b9e\u9645\u6570\u503c", None))
        self.xAxisMaxBtn.setText(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6ex\u8f74\u6700\u5927\u503c", None))
        self.xAxisMinBtn.setText(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6ex\u8f74\u6700\u5c0f\u503c", None))
        self.yAxisTypeLbl_2.setText(QCoreApplication.translate("Dialog", u"x\u8f74\u7c7b\u578b", None))
        self.clearDataBtn.setText(QCoreApplication.translate("Dialog", u"\u6e05\u9664\u8bbe\u7f6e", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u6837\u70b9\u5904\u7406", None))
        self.clearDataBtn_2.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u6837\u70b9\u6570\u636e", None))
        self.clearDataBtn_3.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u6837\u70b9\u6570\u636e", None))
        self.clearDataBtn_4.setText(QCoreApplication.translate("Dialog", u"\u62df\u5408\u6837\u70b9", None))
        self.selectedPtsNumLbl.setText(QCoreApplication.translate("Dialog", u"\u5df2\u9009\u70b9\u6570\uff1a", None))
        self.selectedPtsNumDispLbl.setText("")
        self.polyIdxLbl.setText(QCoreApplication.translate("Dialog", u"\u591a\u9879\u5f0f\u6b21\u6570", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6839\u636e\u62df\u5408\u51fd\u6570\u6c42\u503c", None))
        self.axisDataSetLbl_17.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.axisDataSetLbl_18.setText(QCoreApplication.translate("Dialog", u"y", None))
    # retranslateUi

