# pyuic5 calculator_design_app.ui -o calculator_design.py design ı (ui dosyası) py a çevirmek için gereken script

from PyQt5 import QtWidgets
import sys
from calculator_design import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_sum.clicked.connect(self.calculate)
        self.ui.btn_sub.clicked.connect(self.calculate)
        self.ui.btn_mult.clicked.connect(self.calculate)
        self.ui.btn_div.clicked.connect(self.calculate)
    def calculate(self):
        sender = self.sender().text()
        result = 0
        if sender == "Summary":
            result = int(self.ui.txt_num1.text()) + int(self.ui.txt_num2.text())
        elif sender == "Substraction":
            result = int(self.ui.txt_num1.text()) - int(self.ui.txt_num2.text())
        elif sender == "Multiplication":
            result = int(self.ui.txt_num1.text()) * int(self.ui.txt_num2.text())
        elif sender == "Divide":
            result = int(self.ui.txt_num1.text()) / int(self.ui.txt_num2.text())
        self.ui.lbl_result.setText("Result: " + str(result))
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
app()