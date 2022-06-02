import sys
from PyQt5 import QtWidgets
from _datetimeForm import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_calculate.clicked.connect(self.calculate)

    def calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        result = f'Total days {start.daysTo(end)}'
        self.ui.lbl_result.setText(result)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


app()
