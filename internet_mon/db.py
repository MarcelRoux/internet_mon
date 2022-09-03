import sqlite3


def connect_db(db_name_base='data/log.db'):
    conn = sqlite3.connect(db_name_base)
    cursor = conn.cursor()

    return conn, cursor


def create_table(conn, cursor, script_loc='sql/create.sql'):
    with open(script_loc, 'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)

    conn.commit()

    table = sql_script.split(' (')[0].split(' ')[-1]
    return table


conn, cursor = connect_db()
table = create_table(conn, cursor)

conn.close()
