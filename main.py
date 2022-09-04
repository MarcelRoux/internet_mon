from internet_mon.speedtest_interface import speedtest
from internet_mon.utils import flatten_json
from internet_mon.db import insert_data
from internet_mon.config import DB_NAME, SQL_CREATE_SCRIPT, SPEEDTEST_UPDATES


def main():
    r = speedtest(status_updates=SPEEDTEST_UPDATES)

    data = flatten_json(r)

    if (data):
        insert_data(DB_NAME, SQL_CREATE_SCRIPT, data)
    else:
        print('No data to log.')


if __name__ == '__main__':
    main()
