import sqlite3


class Db:
    """Класс для работы с базой данных database/buy_database.sqlite3"""
    def __init__(self):
        self.con = sqlite3.connect("database/buy_database.sqlite3")
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



