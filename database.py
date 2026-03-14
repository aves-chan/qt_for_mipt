from PySide6.QtSql import QSqlDatabase, QSqlQuery

DB_NAME = "transactions.db"
TABLE_NAME = "transactions"

class Transactions:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(DB_NAME)
        self.db.open()

        query = QSqlQuery()
        query.exec(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        value REAL
        );
        """)

    def new_transaction(self, name, date, value):
        query = QSqlQuery()
        query.exec(f"""
        INSERT INTO {TABLE_NAME} (name, date, value) VALUES ('{name}', '{date}', {value});
        """)

    def remove_transaction(self, id):
        query = QSqlQuery()
        query.exec(f"""
        DELETE FROM {TABLE_NAME} WHERE id == {id}; 
        """)

