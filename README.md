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
SQL_CREATE_SPEEDTEST_SCRIPT=<full path to sql create script for speedtest>
SPEEDTEST_UPDATES=Boolean
SPEEDTEST_RETRIES=Int
SPEEDTEST_RETRY_UPDATES=Boolean
SQL_CREATE_PING_SCRIPT=<full path to sql create script for ping>
PING_HOSTS_FILE=<full path to ping hosts file>
DEFAULT_PING_HOST=<default ping host>
```

## Errors

HTTP 403 Error - [use secure flag](https://ubuntu-mate.community/t/speedtest-cli-error/25722/4).

This error would show up on the hour and on the half hour, even when using a cron offset of up to 5 minutes.  
This is resolved as indicated in the above resource by specifying the secure option during setup.
