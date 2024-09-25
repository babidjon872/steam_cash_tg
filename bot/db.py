import sqlite3
import datetime as dt


con = sqlite3.connect("./databases/users.db")
cur = con.cursor()


def new_user(id: int, username: str) -> None:
    cur.execute(f"""INSERT INTO user VALUES({id}, '{username}', 
                '{dt.datetime.now().strftime("%d.%m.%Y|%H:%M:%S")}')""")
    con.commit()


def new_payment(id: int, username: str, login: str, amount: float, method: str) -> None:
    cur.execute(f"""INSERT INTO operations VALUES({id}, 
                '{dt.datetime.now().strftime("%d.%m.%Y|%H:%M:%S")}',
                '{login}', '{method}', {amount})""")
    con.commit()


def get_logins(id: int) -> list[str, ]:
    data = cur.execute(f"""SELECT steamLogin FROM 
                       operations WHERE tgId={id}""").fetchall()
    return [item[0] for item in data]


def get_history(id: int) -> list:
    data = cur.execute(f"""SELECT steamLogin, amount, type, date FROM operations 
                WHERE tgId={id}""").fetchall()
    return data

