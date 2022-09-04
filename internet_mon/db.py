import sqlite3
import json


def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    return conn, cursor


def create_table(conn, cursor, sql_create_script_loc):
    with open(sql_create_script_loc, 'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)

    conn.commit()

    table = sql_script.split(' (')[0].split(' ')[-1]
    return table


def insert(table_name: str, data: dict, conn, cur):
    cols = f'{", ".join(data.keys())}'
    named_parameters = f'{", ".join([f":{k}" for k in data.keys()])}'

    query = f"INSERT INTO {table_name} ({cols}) VALUES ({named_parameters});"
    # print('SQL insert:')
    # print(query)
    cur.execute(query, data)
    conn.commit()


def insert_data(db_name, sql_create_script_loc, data):
    conn, cursor = connect_db(db_name)
    table = create_table(conn, cursor, sql_create_script_loc)
    insert(table, data, conn, cursor)

    conn.close()


def main():
    with open('data/sample_data.json', 'r') as data_file:
        DATA = json.loads(data_file.read())

    insert_data('data/log.db', DATA)


if __name__ == '__main__':
    main()
