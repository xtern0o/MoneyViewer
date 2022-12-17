import sqlite3


class Db:
    """Класс для работы с базой данных database/buy_database.sqlite3"""
    """Hello, Viktor Latkin, Alexander Duryagin and other humen!"""
    """это все мое если что я честно не скопировал с перого попавшегося репозитория честно"""

    def __init__(self):
        self.con = sqlite3.connect("source/database/buy_database.sqlite3")
        self.cur = self.con.cursor()

    def add_user(self, username: str, password: str, remember: bool) -> None:
        """New user registration"""
        self.cur.execute("""
        INSERT INTO users(username, password, remember)
        VALUES (?, ?, ?)
        """, (username, password, remember))

    def get_userid_if_correct_pwd(self, login: str, password: str) -> int:
        """Returns user_id if pwd is correct else return 0"""

        data = self.cur.execute("""
        SELECT * FROM users
        WHERE username = ?
        """, (login,)).fetchone()
        if data:
            if password == str(data[2]):
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

        return self.cur.execute("""SELECT * FROM users WHERE username = ?""", (username, )).fetchone() is not None

    def get_username(self, userid):
        """Returns username by getting userid lol!"""

        return self.cur.execute("""SELECT username FROM users WHERE id = ?""", (userid, )).fetchone()[0]

    def add_new_payment(self, userid, pname, category, cost, date) -> bool:
        """Add new row to the purchases database"""

        try:
            category_id = self.cur.execute("""
            SELECT id FROM categories
            WHERE category_name = ?
            """, (category, )).fetchone()[0]
        except TypeError:
            return False # категории не существует
        self.cur.execute("""
        INSERT INTO payments(user_id, name, category_id, cost, date) 
        VALUES (?, ?, ?, ?, ?)
        """, (userid, pname, category_id, cost, date))
        self.con.commit()
        return True

    def get_exist_categories(self) -> list:
        """Returns list of categories which are exist at this moment"""

        return [row[0] for row in self.cur.execute("""SELECT category_name, essential FROM categories""").fetchall()]

    def add_new_category(self, category_name, essential):
        """Adds new category to the categoy table"""

        if category_name not in [row[0] for row in self.cur.execute("SELECT category_name FROM categories").fetchall()]:
            self.cur.execute("""
            INSERT INTO categories(category_name, essential)
            VALUES (?, ?)
            """, (category_name, essential))
            self.con.commit()

    def get_all_payments_from_this_user(self, userid):
        """returns all user's payments"""

        return self.cur.execute("""
        SELECT * FROM payments
        WHERE user_id = ?
        """, (userid, ))


