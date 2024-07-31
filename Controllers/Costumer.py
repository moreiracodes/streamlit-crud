from Service.Database import Database
from Models.Costumer import Costumer as CostumerModel


class Costumer(Database):
    def __init__(self):
        self.connection = super().__init__()
        self.__create_table()

    def __create_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                    IF NOT EXISTS (SELECT *
                            FROM sysobjects
                            WHERE NAME='costumers'
                            AND XTYPE='U')
                        CREATE TABLE costumers (
                            id INT IDENTITY(1,1) NOT NULL,
                            name VARCHAR(100) NOT NULL,
                            age INT NOT NULL,
                            email VARCHAR(100) NOT NULL
                        )
                """
            )
            cursor.commit()
            cursor.close()
            return True
        except Exception as err:
            print(f"Create table {__name__} error: {err}")
            return False

    def get_all(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""SELECT * FROM costumers ORDER BY id ASC""")
            costumer_list = []
            for row in cursor.fetchall():
                costumer_list.append(
                    CostumerModel(row[1], row[2], row[3], id=row[0])
                )
            cursor.close()
            return costumer_list
        except Exception as err:
            print(f"List all error: {err}")
            return False

    def get_by_id(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""SELECT * FROM costumers WHERE id=?""", id)
            row = cursor.fetchone()
            result = CostumerModel(row[1], row[2], row[3], id=row[0])
            cursor.close()
            return result
        except Exception as err:
            print(f"Get costumer by id error: {err}")
            return False

    def create(self, cliente):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                    INSERT INTO costumers (name, age, email)
                    VALUES (?, ?, ?);
                """,
                cliente.name,
                cliente.age,
                cliente.email,
            )
            cursor.commit()
            cursor.close()
            return True
        except Exception as err:
            print(f"Insert error: {err}")
            return False

    def update(self, cliente):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                    UPDATE costumers
                    SET
                        name=?,
                        age=?,
                        email=?
                    WHERE id=?
                """,
                cliente.name,
                cliente.age,
                cliente.email,
                cliente.id,
            )
            cursor.commit()
            cursor.close()
            return True
        except Exception as err:
            print(f"Update error: {err}")
            return False

    def delete(self, cliente):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                    DELETE FROM costumers WHERE id=?
                """,
                cliente.id,
            )
            cursor.commit()
            cursor.close()
            return True
        except Exception as err:
            print(f"Delete error: {err}")
            return False
