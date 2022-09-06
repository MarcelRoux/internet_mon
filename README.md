# Internet_mon

Internet_mon aims to provide a monitoring layer to internet connectivity in order to provide insight into internet speeds.

## Installation

Installation is simple, use the standard pip install along with the requirements file.

```
pip install -r requirements.txt
```

## Configuration

Configuration is done through the dotenv module and a .env file is required in the root directory of the project.

Configuration variables:
```
DB_NAME=<full path to database location>
SQL_CREATE_SCRIPT=<full path to sql create script>
SPEEDTEST_UPDATES=Boolean
SPEEDTEST_RETRIES=Int
SPEEDTEST_RETRY_UPDATES=Boolean
```
