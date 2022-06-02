import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _msgboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_exit.clicked.connect(self.showDialog)

    def showDialog(self):
        msg = QMessageBox()
        result = QMessageBox.question(self, 'Close Application', 'Are you sure ? ', QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore,
                                      QMessageBox.Ok )
        if result == QMessageBox.Ok:
            print('Bye Bye!')
            QtWidgets.qApp.quit()
    #     msg.setWindowTitle('Close Application')
    #     msg.setText('Are you sure ? ')
    #     msg.setIcon(QMessageBox.Warning)
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
    #     msg.setDefaultButton(QMessageBox.Ok)
    #     msg.setDetailedText('Details...')
    #     msg.buttonClicked.connect(self.popup_button)
    #
    #     x = msg.exec_()
    #     print(x)
    # def popup_button(self,i):
    #     print(i.text())
    #     if i.text() == 'OK':
    #         QtWidgets.qApp.quit()
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()