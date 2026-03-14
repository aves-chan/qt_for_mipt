from PySide6.QtWidgets import QDialog, QMessageBox
from ui.new_transaction_ui import Ui_dialog

class NewTransactionDialog(QDialog):
    def __init__(self, db, parent):
        super().__init__(parent=parent)
        self.db = db

        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.ui.comboBox.addItems(["Доход", "Расход"])

        self.ui.pushButton.clicked.connect(self.save_transaction)

    def save_transaction(self):
        name = self.ui.lineEdit.text().strip()
        value = self.ui.lineEdit_2.text().strip()
        date = self.ui.dateEdit.date().toString("dd-MM-yyyy")
        operation = self.ui.comboBox.currentText()

        if not name or not value or not operation:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заолнены")
            return

        try:
            value = float(value)
            if operation == "Расход":
                value *= -1
        except:
            QMessageBox.warning(self, "Ошибка", "Неправильно ввели число")
            return

        self.db.new_transaction(name, date, value)

        self.accept()
