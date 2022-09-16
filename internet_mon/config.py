import os
from dotenv import load_dotenv


load_dotenv()

# Load database config.
DB_NAME = os.getenv('DB_NAME')

# Load speedtest config.
SQL_CREATE_SPEEDTEST_SCRIPT = os.getenv('SQL_CREATE_SPEEDTEST_SCRIPT')
SPEEDTEST_UPDATES = os.getenv('SPEEDTEST_UPDATES').lower() == 'true'
SPEEDTEST_RETRIES = int(os.getenv('SPEEDTEST_RETRIES', '3'))
SPEEDTEST_RETRY_UPDATES = os.getenv('SPEEDTEST_RETRY_UPDATES').lower() == 'true'

# Load ping config.
SQL_CREATE_PING_SCRIPT = os.getenv('SQL_CREATE_PING_SCRIPT')
PING_HOSTS_FILE = os.getenv('PING_HOSTS_FILE')
DEFAULT_PING_HOST = os.getenv('DEFAULT_PING_HOST', 'google.com')
