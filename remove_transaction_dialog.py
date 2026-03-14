from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QMessageBox, QDialog
from ui.remove_transaction_ui import Ui_Dialog
from database import TABLE_NAME

class RemoveTransactionDialog(QDialog):
    def __init__(self, db, parent):
        super().__init__(parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.db = db

        self.model = QSqlTableModel(self)
        self.model.setTable(TABLE_NAME)
        self.model.select()

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.hideColumn(0)

        self.ui.pushButton.clicked.connect(self.remove_transaction)

    def remove_transaction(self):
        index = self.ui.tableView.currentIndex()

        if not index.isValid():
            QMessageBox.warning(self, "Ошибка", "Нужно выбрать операцию")
            return
        id = self.model.data(self.model.index(index.row(), 0))
        self.db.remove_transaction(id)

        self.accept()



