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
def add_message_to_db(conn, systolic_pressure: int, diastolic_pressure: int, user_id: int, ):
    c = conn.cursor()
    c.execute('INSERT INTO user_message (systolic_pressure,diastolic_pressure, user_id, date) VALUES (?,?,?,datetime())',(systolic_pressure, diastolic_pressure, user_id, ))
    conn.commit()

@ensure_connection
def count_messages(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_message WHERE user_id =?', (user_id,))
    (res, ) = c.fetchone()
    return res

@ensure_connection
def monthly_average_query(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-30 days\')', (user_id,))
    return c.fetchall()

@ensure_connection
def monthly_statistic_query(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT date, systolic_pressure, diastolic_pressure FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-30 days\')', (user_id,))
    return c.fetchall()


# if __name__ == '__main__':
#     init_db()
# #
# #     # add_message_to_db(user_id=136090387, systolic_pressure=int('122'), diastolic_pressure=int("122"), date='03-02-2020 02:10')
# #     # #
#     r = monthly_statistic_query(user_id=136090387)
#     # print(r[0][0], r[0][1])
#     print(r)

    # print(round(r[0][0]), round(r[0][1]))

