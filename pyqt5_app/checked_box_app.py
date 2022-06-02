import sys
from PyQt5 import QtWidgets
from _checked_box_form import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cb_cinema.stateChanged.connect(self.show_state)
        self.ui.cb_read_book.stateChanged.connect(self.show_state)
        self.ui.cb_sport.stateChanged.connect(self.show_state)

        self.ui.btn_save_cb.clicked.connect(self.getAllChecked)

    def show_state(self):
        cb = self.sender()
        print(f"{cb.text()} is {cb.isChecked()}")

    def getAllChecked(self):
        items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)
        result = ''
        for cb in items:
            if cb.isChecked() == True:
                result += cb.text() + '\n'
        self.ui.lbl_result.setText(result)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()
