import os
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv('DB_NAME_BASE')
SQL_CREATE_SCRIPT = os.getenv('SQL_CREATE_SCRIPT')
