from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
class MySQL(Database):
    def connect(self):
        return "MySQL Connected"
class PostgreSQL(Database):
    def connect(self):
        return "PostgreSQL Connected"
class MongoDB(Database):
    def connect(self):
        return "MongoDB Connected"
def get_database_connection(db: Database):
    return db.connect()
# Example usage:
if __name__ == "__main__":
    mysql_db = MySQL()
    postgres_db = PostgreSQL()
    mongo_db = MongoDB()

    print(get_database_connection(mysql_db))      # Output: MySQL Connected
    print(get_database_connection(postgres_db))   # Output: PostgreSQL Connected
    print(get_database_connection(mongo_db))      # Output: MongoDB Connected