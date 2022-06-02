import sys
from PyQt5 import QtWidgets
from _radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.radio_turkey.setChecked(True)
        self.ui.radio_university.setChecked(True)

        self.ui.radio_turkey.toggled.connect(self.onClickedCountry)
        self.ui.radio_italy.toggled.connect(self.onClickedCountry)
        self.ui.radio_germany.toggled.connect(self.onClickedCountry)
        self.ui.radio_hungary.toggled.connect(self.onClickedCountry)

        self.ui.radio_highschool.toggled.connect(self.onClickedEducation)
        self.ui.radio_university.toggled.connect(self.onClickedEducation)
        self.ui.radio_masterdegree.toggled.connect(self.onClickedEducation)
        self.ui.radio_middleschool.toggled.connect(self.onClickedEducation)

        self.ui.btn_country.clicked.connect(self.getSelectedCountry)
        self.ui.btn_education.clicked.connect(self.getSelectedEducation)

    def onClickedCountry(self):
        rb = self.sender()
        if rb.isChecked() == True:
            print('Chosen Country: ' + rb.text())
    def onClickedEducation(self):
        rb = self.sender()
        if rb.isChecked() == True:
            print('Chosen Education: ' + rb.text())
    def getSelectedCountry(self):
        items = self.ui.group_country.findChildren(QtWidgets.QRadioButton)
        for item in items:
            if item.isChecked() == True:
                self.ui.lbl_country.setText(item.text())
    def getSelectedEducation(self):
        items = self.ui.group_education.findChildren(QtWidgets.QRadioButton)
        for item in items:
            if item.isChecked() == True:
                self.ui.lbl_education.setText(item.text())
app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())