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
        heart_rate              INTEGER NOT NULL,
        date                    TEXT NOT NULL
        )   
    ''')
    conn.commit()

@ensure_connection
def add_message_to_db(conn, systolic_pressure: int, diastolic_pressure: int, user_id: int, heart_rate: int):
    c = conn.cursor()
    c.execute('INSERT INTO user_message (systolic_pressure,diastolic_pressure, user_id, date, heart_rate) VALUES (?,?,?,datetime("now","localtime"),?)', (systolic_pressure, diastolic_pressure, user_id, heart_rate))
    conn.commit()

@ensure_connection
def monthly_statistic_query(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT date, systolic_pressure, diastolic_pressure, heart_rate FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-30 days\')', (user_id,))
    return c.fetchall()

#счетчик уникальный значений id в БД за последние 30 дней
@ensure_connection
def unique_id_counter(conn,):
    c = conn.cursor()
    c.execute('SELECT COUNT(user_id) FROM user_message GROUP BY user_id')
    return c.fetchall()

#счетчик уникальный значений id в БД, которые за последние 10 дней сделали минимум 3 записи
@ensure_connection
def unique_id_counter2(conn,):
    c = conn.cursor()
    c.execute('SELECT count(distinct user_id) FROM user_message WHERE date > date(\'now\',\'-10 days\') GROUP BY user_id HAVING COUNT(user_id) >= 3')
    return c.fetchall()

@ensure_connection
def del_last_insert(conn, user_id: int):
    c = conn.cursor()
    c.execute('DELETE FROM user_message WHERE id = (SELECT id from user_message WHERE id NOT NULL AND user_id=? ORDER BY date DESC LIMIT 1 )', (user_id,))
    return c.fetchall()

@ensure_connection
def user_id_exists_in_db(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT DISTINCT CASE WHEN user_id THEN 1 ELSE 0 END user_id from user_message WHERE user_id=?', (user_id,))
    return c.fetchall()

#
#ВЫБОРКА ИЗ БАЗЫ СРЕДНИХ ЗНАЧЕНИЙ ДАВЛЕНИЯ БЕЗ ПУЛЬСА
#
@ensure_connection
def last_day_average_query_without_heart_rate(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-24 hours\')', (user_id,))
    return c.fetchall()

@ensure_connection
def seven_days_average_query_without_heart_rate(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-7 days\')', (user_id,))
    return c.fetchall()

@ensure_connection
def fourteen_days_average_query_without_heart_rate(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-14 days\')', (user_id,))
    return c.fetchall()


@ensure_connection
def thirty_days_average_query_without_heart_rate(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-30 days\')', (user_id,))
    return c.fetchall()

#
#ВЫБОРКА ИЗ БАЗЫ СРЕДНИХ ЗНАЧЕНИЙ ДАВЛЕНИЯ С УКАЗАНИЕМ ПУЛЬСА
#
@ensure_connection
def last_day_average_query_with_heart_rate(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure), AVG(heart_rate) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-24 hours\')', (user_id,))
    return c.fetchall()

@ensure_connection
def seven_day_average_query_with_heart_rate(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure), AVG(heart_rate) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-7 days\')', (user_id,))
    return c.fetchall()


@ensure_connection
def fourteen_day_average_query_with_heart_rate(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure), AVG(heart_rate) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-14 days\')', (user_id,))
    return c.fetchall()

@ensure_connection
def thirty_day_average_query_with_heart_rate(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT AVG(systolic_pressure), AVG(diastolic_pressure), AVG(heart_rate) FROM user_message WHERE user_id = ? AND date > date(\'now\',\'-30 days\')', (user_id,))
    return c.fetchall()

# if __name__ == '__main__':
#     init_db()
# # # #
#     add_message_to_db(user_id=136090387, systolic_pressure=int('122'), diastolic_pressure=int("122"), heart_rate='90', date='2020-04-26 06:28:47')
# # # #     # #
# # #     r = days_statistic_query(user_id=136090387)
# # #     # print(r[0][0], r[0][1])
# #     print(len(r))
#
# #     # print(round(r[0][0]), round(r[0][1]))
