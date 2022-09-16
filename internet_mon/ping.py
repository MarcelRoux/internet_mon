from ping3 import ping as ping3ping


SERVER = 'google.com'


def ping(address):
    ping = ping3ping(address, timeout=1)
    if (ping is False):
        ping = None

    return {
        'address_dest': address,
        'address_source': '127.0.0.1',
        'unit': 's',
        'ping': ping
    }


def main():
    data = ping(SERVER)
    print(data)


if __name__ == '__main__':
    main()
