from internet_mon.speedtest_interface import speedtest


def main():
    print('Hello, World!')

    print('Running speedtest.')
    r = speedtest(status_updates=True)
    print(r)


if __name__ == '__main__':
    main()
