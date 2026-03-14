from PySide6.QtWidgets import QApplication, QMainWindow, QListView
from PySide6.QtSql import QSqlTableModel

from remove_transaction_dialog import RemoveTransactionDialog
from ui import main_ui
import new_transaction_dialog
import database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = database.Transactions()

        self.ui.pushButton_new.clicked.connect(self.new_transaction)
        self.ui.pushButton_remove.clicked.connect(self.remove_transaction)

        self.model = QSqlTableModel(self)
        self.model.setTable(database.TABLE_NAME)
        self.model.select()

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.hideColumn(0)


    def new_transaction(self):
        dialog = new_transaction_dialog.NewTransactionDialog(self.db, self)
        dialog.exec()
        self.model.select()

    def remove_transaction(self):
        dialog = RemoveTransactionDialog(self.db, self)
        dialog.exec()
        self.model.select()



def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()