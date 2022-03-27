from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidgetItem
import phishMail
from PyQt5.QtCore import QMimeData
from email.mime import text

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 357)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.loadall = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.load_all())
        self.loadall.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.loadall.setObjectName("loadall")

        self.sendall = QtWidgets.QPushButton(self.centralwidget)
        self.sendall.setGeometry(QtCore.QRect(140, 50, 141, 31))
        self.sendall.setObjectName("sendall")
        self.sendall.clicked.connect(self.send)
        self.sendall.setEnabled(False)

        self.clearall = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clear_it())
        self.clearall.setGeometry(QtCore.QRect(290, 50, 101, 31))
        self.clearall.setObjectName("clearall")

        self.mylist = QtWidgets.QListWidget(self.centralwidget)
        self.mylist.setGeometry(QtCore.QRect(10, 90, 381, 231))
        self.mylist.setObjectName("listWidget")
        self.mylist.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def load_all(self):
        self.sendall.setEnabled(True)
        self.loadall.setEnabled(False)
        self.emails = phishMail.readEmails()
        self.mylist.addItems(self.emails)

    def send(self):
        self.mylist.selectAll()
        phishMail.main()

        for item in self.mylist.selectedItems():
            item.setText(item.text() + '\t...\tsent')

    def clear_it(self):
        self.loadall.setEnabled(True)
        self.sendall.setEnabled(False)
        self.mylist.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("RecordApp", "phisherman RecordApp"))
        self.loadall.setText(_translate("RecordApp", "Load all"))
        self.sendall.setText(_translate("RecordApp", "Send all"))
        self.clearall.setText(_translate("RecordApp", "Clear The List"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())