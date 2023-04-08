import sqlite3

DB_CREAS = {'database': "example.db"}


class DBAccesor:
    def __int__(self, db_creds: dict):
        self.__db_creds = db_creds
        self.__connection = None
        self.__cursor = None

    def __enter__(self):
        print("Connection openning!")
        if self.__connection is None:
            self.__connection = sqlite3.connect(**self.__db_creds)
        self.__cursor = self.__connection.cursor()
        return self.__cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.commit()
        self.__connection.close()
        print("Connection closing!")

def main():
    with DBAccessor(DBD_CRES) as cUrsor:
        for row in cursor.execute("SELECT * FROM user"):
            print(row)
    """Чтобы не дублировать эти строчки были реализованы функции сверху!"""
    # connection = sqlite3.connect(**DB_CREDS)
    # cursor = connection.cursor()
    # for row in cursor.execute("SELECT * FROM user"):
    #     print(row)
    # connection.commit()
    # connection.close()
