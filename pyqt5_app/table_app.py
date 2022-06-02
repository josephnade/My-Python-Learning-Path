import sys
from PyQt5 import QtWidgets
from _tableForm import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem

products = [{'name': 'Samsung S5', 'price': '2000'},
            {'name': 'Samsung S6', 'price': '3000'},
            {'name': 'Samsung S7', 'price': '4000'},
            {'name': 'Samsung S8', 'price': '5000'}, ]


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)

    def doubleClick(self):
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(), item.column(), item.text())

    def loadProducts(self):

        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(('Name', 'Price'))
        self.ui.tableProducts.setColumnWidth(0, 200)
        self.ui.tableProducts.setColumnWidth(1, 100)
        rowIndex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex, 0, QTableWidgetItem(product['name']))
            self.ui.tableProducts.setItem(rowIndex, 1, QTableWidgetItem(product['price']))
            rowIndex += 1

    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()
        if name and price is not None:
            products.append({'name': name, 'price': price})
        self.loadProducts()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


app()
