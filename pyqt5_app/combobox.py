import sys
from PyQt5 import QtWidgets
from _comboboxForm import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.cbCities

        combo.addItem('Ankara')
        combo.addItem('Bursa')
        combo.addItem('Aydın')
        self.ui.btnLoadItems.clicked.connect(self.loadItems)
        self.ui.btnGetItems.clicked.connect(self.getItem)
        self.ui.btn_clear.clicked.connect(self.clearItem)
    def loadItems(self):
        cities = ['Adana', 'İzmir', 'Eskişehir']
        self.ui.cbCities.addItems(cities)
    def getItem(self):
        print(f'Chosen {self.ui.cbCities.currentIndex()} index city!')
        print(f'There are {self.ui.cbCities.count()} cities!')
        self.ui.lblResult.setText(self.ui.cbCities.currentText())

    def clearItem(self):
        self.ui.cbCities.clear()
app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())