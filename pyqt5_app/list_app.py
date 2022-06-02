import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from _listForm import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # load students
        self.loadStudents()
        # add students
        self.ui.btnAdd.clicked.connect(self.addStudents)
        # edit students
        self.ui.btnEdit.clicked.connect(self.editStudents)
        # delete students
        self.ui.btnRemove.clicked.connect(self.removeStudents)
        # up student
        self.ui.btnUp.clicked.connect(self.upStudent)
        # down student
        self.ui.btnDown.clicked.connect(self.downStudent)
        # sort students
        self.ui.btnSort.clicked.connect(self.sortStudents)
        # exit app
        self.ui.btnExit.clicked.connect(self.closeApp)

    def loadStudents(self):
        students = ['Ali', 'Ahmet', 'Mehmet']
        self.ui.listItems.addItems(students)

    def addStudents(self):
        currentIndex = self.ui.listItems.currentRow()
        text, ok = QInputDialog.getText(self, 'New Student', 'Student Name: ')
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex + 1, text)

    def editStudents(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        if item is not None:
            text, ok = QInputDialog.getText(self, 'Edit Student', 'Student Name: ', QLineEdit.Normal, item.text())
            if text is not None and ok:
                item.setText(text)

    def removeStudents(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        if item is None:
            return
        question = QMessageBox.question(self, 'Remove Student', 'Are you sure?', QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.listItems.currentRow()
        if index > 0:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index - 1, item)
            self.ui.listItems.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count() - 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index + 1, item)
            self.ui.listItems.setCurrentItem(item)

    def sortStudents(self):
        self.ui.listItems.sortItems()

    def closeApp(self):
        quit()
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


app()
