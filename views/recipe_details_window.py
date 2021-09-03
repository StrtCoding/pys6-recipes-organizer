# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_details_window.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class DetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(769, 488)
        DetailWindow.setStyleSheet(u"border-radius: 5px")
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(245, 240, 225);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.background_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: #1e3d59;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(113, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.recipe_pic_label = QLabel(self.frame)
        self.recipe_pic_label.setObjectName(u"recipe_pic_label")
        self.recipe_pic_label.setMinimumSize(QSize(0, 0))
        self.recipe_pic_label.setMaximumSize(QSize(170, 170))

        self.horizontalLayout.addWidget(self.recipe_pic_label)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.recipe_title_label = QLabel(self.frame_3)
        self.recipe_title_label.setObjectName(u"recipe_title_label")
        self.recipe_title_label.setGeometry(QRect(20, 10, 341, 16))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.recipe_title_label.setFont(font1)
        self.recipe_title_label.setStyleSheet(u"color: #6b7b8c;")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 71, 16))
        font2 = QFont()
        font2.setBold(True)
        self.label.setFont(font2)
        self.recipe_category_label = QLabel(self.frame_3)
        self.recipe_category_label.setObjectName(u"recipe_category_label")
        self.recipe_category_label.setGeometry(QRect(100, 40, 311, 16))
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 71, 16))
        self.label_2.setFont(font2)
        self.recipe_url_label = QLabel(self.frame_3)
        self.recipe_url_label.setObjectName(u"recipe_url_label")
        self.recipe_url_label.setGeometry(QRect(100, 60, 311, 16))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 71, 16))
        self.label_3.setFont(font2)
        self.recipe_budget_label = QLabel(self.frame_3)
        self.recipe_budget_label.setObjectName(u"recipe_budget_label")
        self.recipe_budget_label.setGeometry(QRect(100, 80, 311, 16))

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.recipe_title_label_2 = QLabel(self.frame_2)
        self.recipe_title_label_2.setObjectName(u"recipe_title_label_2")
        self.recipe_title_label_2.setFont(font1)
        self.recipe_title_label_2.setStyleSheet(u"color: #6b7b8c;")

        self.verticalLayout_4.addWidget(self.recipe_title_label_2)

        self.ingredients_text_edit = QPlainTextEdit(self.frame_2)
        self.ingredients_text_edit.setObjectName(u"ingredients_text_edit")

        self.verticalLayout_4.addWidget(self.ingredients_text_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.recipe_title_label_3 = QLabel(self.frame_2)
        self.recipe_title_label_3.setObjectName(u"recipe_title_label_3")
        self.recipe_title_label_3.setFont(font1)
        self.recipe_title_label_3.setStyleSheet(u"color: #6b7b8c;")

        self.verticalLayout_5.addWidget(self.recipe_title_label_3)

        self.directions_text_edit = QPlainTextEdit(self.frame_2)
        self.directions_text_edit.setObjectName(u"directions_text_edit")

        self.verticalLayout_5.addWidget(self.directions_text_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("DetailWindow", u"Recipes Organizer", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.recipe_pic_label.setText("")
        self.recipe_title_label.setText(QCoreApplication.translate("DetailWindow", u"Titulo", None))
        self.label.setText(QCoreApplication.translate("DetailWindow", u"Categoria:", None))
        self.recipe_category_label.setText(QCoreApplication.translate("DetailWindow", u"Categoria", None))
        self.label_2.setText(QCoreApplication.translate("DetailWindow", u"URL:", None))
        self.recipe_url_label.setText(QCoreApplication.translate("DetailWindow", u"URL", None))
        self.label_3.setText(QCoreApplication.translate("DetailWindow", u"Presupuesto", None))
        self.recipe_budget_label.setText(QCoreApplication.translate("DetailWindow", u"Presupuesto", None))
        self.recipe_title_label_2.setText(QCoreApplication.translate("DetailWindow", u"Ingredientes", None))
        self.recipe_title_label_3.setText(QCoreApplication.translate("DetailWindow", u"Proceso de realizacion", None))
    # retranslateUi

