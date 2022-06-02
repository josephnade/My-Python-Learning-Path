import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 500, 500)
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setToolTip("My Tooltip")
        self.initUI()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText('Number 1: ')
        self.lbl_num1.move(50, 30)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.resize(200, 30)
        self.txt_num1.move(120, 30)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText('Number 2: ')
        self.lbl_num2.move(50, 80)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.resize(200, 30)
        self.txt_num2.move(120, 80)

        self.btn_sum = QtWidgets.QPushButton(self)
        self.btn_sum.setText("Sum")
        self.btn_sum.move(120, 120)
        self.btn_sum.clicked.connect(self.calculate)

        self.btn_sub = QtWidgets.QPushButton(self)
        self.btn_sub.setText("Sub")
        self.btn_sub.move(120, 160)
        self.btn_sub.clicked.connect(self.calculate)

        self.btn_mult = QtWidgets.QPushButton(self)
        self.btn_mult.setText("Mult")
        self.btn_mult.move(120, 200)
        self.btn_mult.clicked.connect(self.calculate)

        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("Div")
        self.btn_div.move(120, 240)
        self.btn_div.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(120, 300)

    def calculate(self):
        sender = self.sender().text()
        result = 0
        if sender == "Sum":
            result = int(self.txt_num1.text()) + int(self.txt_num2.text())
        elif sender == "Sub":
            result = int(self.txt_num1.text()) - int(self.txt_num2.text())
        elif sender == "Mult":
            result = int(self.txt_num1.text()) * int(self.txt_num2.text())
        elif sender == "Div":
            result = int(self.txt_num1.text()) / int(self.txt_num2.text())
        self.lbl_result.setText("Result: " + str(result))


def App():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())


App()
