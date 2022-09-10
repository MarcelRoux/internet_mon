from internet_mon.speedtest_interface import speedtest
from internet_mon.utils import flatten_json
from internet_mon.db import insert_data
from internet_mon.config import (DB_NAME,
                                 SQL_CREATE_SPEEDTEST_SCRIPT,
                                 SPEEDTEST_UPDATES,
                                 SPEEDTEST_RETRIES,
                                 SPEEDTEST_RETRY_UPDATES,
                                 SQL_CREATE_PING_SCRIPT)
from datetime import datetime, timezone
from internet_mon.ping import ping


def main():

    print('SPEEDTEST')

    data = speedtest(status_updates=SPEEDTEST_UPDATES,
                     retries=SPEEDTEST_RETRIES,
                     retry_updates=SPEEDTEST_RETRY_UPDATES)

    data = flatten_json(data)
    print(f'data.ping: {data.get("ping")}')

    if (data):
        insert_data(DB_NAME, SQL_CREATE_SPEEDTEST_SCRIPT, data)
    else:
        print('No data to log.')

    print('-' * 32)

    print('PING')

    data = ping('google.com')
    print(f'ping: {data}')

    if (data):
        insert_data(DB_NAME, SQL_CREATE_PING_SCRIPT, data)
    else:
        print('No data to log.')

    print('=' * 32)


if __name__ == '__main__':

    print(f'{datetime.now(timezone.utc).isoformat()}')

    main()
