import sqlite3
import os
from werkzeug.security import check_password_hash, generate_password_hash


class Db:
    """Класс для работы с базой данных database/buy_database.sqlite3"""

    def __init__(self):
        self.con = sqlite3.connect("source/database/buy_database.sqlite3")
        self.cur = self.con.cursor()

    def create_db(self):
        if not os.path.exists("database/buy_database.sqlite3"):
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR,
            password VARCHAR,
            remember BOOLEAN,
            salary INTEGER
            )
            """)
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS payments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name VARCHAR,
            category_id INTEGER,
            cost INTEGER,
            date DATE
            )
            """)
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name STRING,
            essential BOOLEAN,
            color VARCHAR,
            user_id INTEGER
            )
            """)
            self.con.commit()

    def add_user(self, username: str, password: str, remember: bool) -> None:
        """New user registration"""
        self.cur.execute("""
        INSERT INTO users(username, password, remember)
        VALUES (?, ?, ?)
        """, (username, generate_password_hash(password), remember))

    def get_userid_if_correct_pwd(self, login: str, password: str) -> int:
        """Returns user_id if pwd is correct else return 0"""

        data = self.cur.execute("""
        SELECT * FROM users
        WHERE username = ?
        """, (login,)).fetchone()
        if data:
            if check_password_hash(str(data[2]), password):
                return data[0]  # user id
            else:
                return 0

    def find_remembered_user(self) -> tuple:
        """Finds remembered user and returns tuple-info"""

        data = self.cur.execute("""
        SELECT * FROM users
        WHERE remember = 1
        """).fetchone()
        return data

    def set_remembered(self, user_id: int, remembered: bool) -> None:
        """Changes value of remember"""

        self.cur.execute("""
        UPDATE users
        SET remember = ?
        WHERE id = ?
        """, (remembered, user_id))
        self.con.commit()

    def does_exists_user_with_this_username(self, username: str) -> bool:
        """If exists user with this username returns True"""

        return self.cur.execute("""SELECT * FROM users WHERE username = ?""", (username,)).fetchone() is not None

    def get_username(self, userid):
        """Returns username by getting userid lol!"""

        return self.cur.execute("""SELECT username FROM users WHERE id = ?""", (userid,)).fetchone()[0]

    def add_new_payment(self, userid, pname, category, cost, date) -> bool:
        """Add new row to the purchases database"""

        try:
            category_id = self.cur.execute("""
            SELECT id FROM categories
            WHERE category_name = ?
            """, (category,)).fetchone()[0]
        except TypeError:
            return False  # категории не существует
        self.cur.execute("""
        INSERT INTO payments(user_id, name, category_id, cost, date) 
        VALUES (?, ?, ?, ?, ?)
        """, (userid, pname, category_id, cost, date))
        self.con.commit()
        return True

    def get_exist_categories(self) -> list:
        """Returns list of categories which are exist at this moment"""

        return [row[0] for row in self.cur.execute("""SELECT * FROM categories""").fetchall()]

    def get_categories_from_this_user(self, user_id) -> list:
        """Returns list of categories that were created by this user"""

        return self.cur.execute("""
        SELECT id, category_name, essential, color FROM categories WHERE user_id = ?
        """, (user_id, )).fetchall()

    def get_categories_info(self) -> list:
        """Returns list of categories with essential"""

        return self.cur.execute("""SELECT category_name, essential FROM categories""").fetchall()

    def add_new_category(self, category_name, essential, color, user_id):
        """Adds new category to the category table"""

        if category_name not in [row[0] for row in self.cur.execute("SELECT category_name FROM categories").fetchall()]:
            self.cur.execute("""
            INSERT INTO categories(category_name, essential, color, user_id)
            VALUES (?, ?, ?, ?)
            """, (category_name, essential, color, user_id))
            self.con.commit()

    def get_all_payments_from_this_user(self, userid):
        """returns all user's payments"""

        return self.cur.execute("""
        SELECT * FROM payments
        WHERE user_id = ?
        """, (userid,)).fetchall()

    def get_category_by_id(self, id: int) -> str:
        """returns category by id"""

        return self.cur.execute("""
        SELECT * FROM categories
        WHERE id = ?
        """, (id,)).fetchone()

    def update_category(self, id: int, name: str, color: str, essential):
        """updates category info by id"""

        self.cur.execute("""
        UPDATE categories
        SET category_name = ?, color = ?, essential = ?
        WHERE id = ?
        """, (name, color, bool(essential), id))
        self.con.commit()

    def delete_category(self, id):
        """deletes category by id"""

        self.cur.execute("""
        DELETE FROM categories
        WHERE id = ?
        """, (id, ))
        self.cur.execute("""
        DELETE FROM payments
        WHERE category_id = ?
        """, (id, ))
        self.con.commit()


