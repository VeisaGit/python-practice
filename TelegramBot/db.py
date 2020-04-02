import sqlite3

def ensure_connection(func):

    def inner(*args, **kwargs):
        with sqlite3.connect('data.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res

    return inner


@ensure_connection
def init_db(conn, force: bool = False):

    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_message (
        id                      INTEGER PRIMARY KEY,
        user_id                 INTEGER NOT NULL,
        systolic_pressure       INTEGER NOT NULL,
        diastolic_pressure      INTEGER NOT NULL,
        date                    TEXT NOT NULL
        )   
    ''')
    conn.commit()

@ensure_connection
def add_message_to_db(conn, systolic_pressure: int, diastolic_pressure: int, user_id: int, date: str):
    c = conn.cursor()
    c.execute('INSERT INTO user_message (systolic_pressure,diastolic_pressure, user_id, date) VALUES (?,?,?,?)', (systolic_pressure, diastolic_pressure, user_id, date))
    conn.commit()

@ensure_connection
def count_messages(conn, user_id: int ):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_message WHERE user_id =?', (user_id,))
    (res, ) = c.fetchone()
    return res

@ensure_connection
def list_messages(conn, user_id: int, limit: int=3):
    c = conn.cursor()
    c.execute('SELECT id, text FROM user_message WHERE user_id =? ORDER BY id LIMIT? ', (user_id, limit))
    return c.fetchall()


# if __name__ == '__main__':
#     init_db()
#     add_message_to_db(user_id=123, systolic_pressure='110',diastolic_pressure="70", date='01.04.20')

    # r = list_messages(user_id=123)
    # for i in r:
    #     print(i)


