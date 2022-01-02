# Form implementation generated from reading ui file 'Leaderboard2.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import menu
from management_database import ManagementGeneralLeaderboard


class Ui_Form11(object):

    def back_to_menu(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = menu.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(347, 725)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(347, 725))
        Form.setMaximumSize(QtCore.QSize(347, 725))
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        Form.setStyleSheet("background-color:\"green\"\n"
                           "")
        self.ladelabel = QtWidgets.QLabel(Form)
        self.ladelabel.setGeometry(QtCore.QRect(130, 0, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ladelabel.setFont(font)
        self.ladelabel.setObjectName("ladelabel")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 291, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.namelabel_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_12.setObjectName("namelabel_12")
        self.gridLayout.addWidget(self.namelabel_12, 11, 0, 1, 1)
        self.scorelabel_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_1.setObjectName("scorelabel_1")
        self.gridLayout.addWidget(self.scorelabel_1, 0, 1, 1, 1)
        self.namelabel_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_7.setObjectName("namelabel_7")
        self.gridLayout.addWidget(self.namelabel_7, 6, 0, 1, 1)
        self.namelabel_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_9.setObjectName("namelabel_9")
        self.gridLayout.addWidget(self.namelabel_9, 8, 0, 1, 1)
        self.namelabel_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_14.setObjectName("namelabel_14")
        self.gridLayout.addWidget(self.namelabel_14, 13, 0, 1, 1)
        self.scorelabel_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_9.setObjectName("scorelabel_9")
        self.gridLayout.addWidget(self.scorelabel_9, 8, 1, 1, 1)
        self.namelabel_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_1.setObjectName("namelabel_1")
        self.gridLayout.addWidget(self.namelabel_1, 0, 0, 1, 1)
        self.namelabel_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_11.setObjectName("namelabel_11")
        self.gridLayout.addWidget(self.namelabel_11, 10, 0, 1, 1)
        self.namelabel_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_8.setObjectName("namelabel_8")
        self.gridLayout.addWidget(self.namelabel_8, 7, 0, 1, 1)
        self.scorelabel_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_4.setObjectName("scorelabel_4")
        self.gridLayout.addWidget(self.scorelabel_4, 3, 1, 1, 1)
        self.namelabel_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_4.setObjectName("namelabel_4")
        self.gridLayout.addWidget(self.namelabel_4, 3, 0, 1, 1)
        self.scorelabel_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_7.setObjectName("scorelabel_7")
        self.gridLayout.addWidget(self.scorelabel_7, 6, 1, 1, 1)
        self.namelabel_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_10.setObjectName("namelabel_10")
        self.gridLayout.addWidget(self.namelabel_10, 9, 0, 1, 1)
        self.scorelabel_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_2.setObjectName("scorelabel_2")
        self.gridLayout.addWidget(self.scorelabel_2, 1, 1, 1, 1)
        self.namelabel_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_5.setObjectName("namelabel_5")
        self.gridLayout.addWidget(self.namelabel_5, 4, 0, 1, 1)
        self.namelabel_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_13.setObjectName("namelabel_13")
        self.gridLayout.addWidget(self.namelabel_13, 12, 0, 1, 1)
        self.scorelabel_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_6.setObjectName("scorelabel_6")
        self.gridLayout.addWidget(self.scorelabel_6, 5, 1, 1, 1)
        self.namelabel_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_2.setObjectName("namelabel_2")
        self.gridLayout.addWidget(self.namelabel_2, 1, 0, 1, 1)
        self.scorelabel_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_5.setObjectName("scorelabel_5")
        self.gridLayout.addWidget(self.scorelabel_5, 4, 1, 1, 1)
        self.namelabel_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_6.setObjectName("namelabel_6")
        self.gridLayout.addWidget(self.namelabel_6, 5, 0, 1, 1)
        self.namelabel_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_3.setObjectName("namelabel_3")
        self.gridLayout.addWidget(self.namelabel_3, 2, 0, 1, 1)
        self.scorelabel_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_8.setObjectName("scorelabel_8")
        self.gridLayout.addWidget(self.scorelabel_8, 7, 1, 1, 1)
        self.scorelabel_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_3.setObjectName("scorelabel_3")
        self.gridLayout.addWidget(self.scorelabel_3, 2, 1, 1, 1)
        self.namelabel_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel_15.setObjectName("namelabel_15")
        self.gridLayout.addWidget(self.namelabel_15, 14, 0, 1, 1)
        self.scorelabel_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_10.setObjectName("scorelabel_10")
        self.gridLayout.addWidget(self.scorelabel_10, 9, 1, 1, 1)
        self.scorelabel_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_11.setObjectName("scorelabel_11")
        self.gridLayout.addWidget(self.scorelabel_11, 10, 1, 1, 1)
        self.scorelabel_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_12.setObjectName("scorelabel_12")
        self.gridLayout.addWidget(self.scorelabel_12, 11, 1, 1, 1)
        self.scorelabel_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_13.setObjectName("scorelabel_13")
        self.gridLayout.addWidget(self.scorelabel_13, 12, 1, 1, 1)
        self.scorelabel_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_14.setObjectName("scorelabel_14")
        self.gridLayout.addWidget(self.scorelabel_14, 13, 1, 1, 1)
        self.scorelabel_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scorelabel_15.setObjectName("scorelabel_15")
        self.gridLayout.addWidget(self.scorelabel_15, 14, 1, 1, 1)
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(60, 670, 230, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QtCore.QSize(230, 35))
        self.backButton.setMaximumSize(QtCore.QSize(230, 35))
        self.backButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.backButton.setStyleSheet("background-color:\"lightblue\"\n"
                                      "")
        self.backButton.setAutoDefault(False)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.back_to_menu)
        self.backButton.clicked.connect(Form.close)

        self.manage_db = ManagementGeneralLeaderboard()

        self.list_to_leaderboard = self.manage_db.get_general_leaderboard()

        print(self.list_to_leaderboard)

        for index, row in enumerate(self.list_to_leaderboard, start=1):
            if index < 16:
                eval("self.namelabel_" + str(index)).setText(row[0])
                eval("self.scorelabel_" + str(index)).setText(str(row[1]))

            else:
                break

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scrabble"))
        self.ladelabel.setText(_translate("Form", "Leaderboard"))
        self.backButton.setText(_translate("Form", "Back to menu"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form11()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())