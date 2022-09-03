from internet_mon.speedtest_interface import speedtest
from internet_mon.utils import flatten_json


def main():
    print('Hello, World!')

    print('Running speedtest.')
    r = speedtest(status_updates=True)
    print(r)

    r_flat = flatten_json(r)
    print(f'r_flat: {r_flat}')
    print(sorted(r_flat))
    [print(f'{e}: {r_flat[e]}') for e in sorted(r_flat)]


if __name__ == '__main__':
    main()
