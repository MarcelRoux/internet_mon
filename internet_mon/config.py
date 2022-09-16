import os
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv('DB_NAME')
SQL_CREATE_SCRIPT = os.getenv('SQL_CREATE_SCRIPT')
SPEEDTEST_UPDATES = os.getenv('SPEEDTEST_UPDATES').lower() == 'true'
SPEEDTEST_RETRIES = int(os.getenv('SPEEDTEST_RETRIES', '3'))
SPEEDTEST_RETRY_UPDATES = os.getenv('SPEEDTEST_RETRY_UPDATES').lower() == 'true'
