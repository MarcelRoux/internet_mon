import speedtest as ookla_speedtest


servers = []
threads = None


def speedtest(status_updates=False, retries=3, retry_updates=False):

    results_dict = None

    for attempt in range(1, retries + 1):
        try:
            if (retry_updates):
                print(f'Attempt {attempt}...', end=' ')

            if (attempt < 3):
                raise ValueError('Sample error for testing.')

            if (status_updates):
                print('Configuring test.')

            s = ookla_speedtest.Speedtest()

            if (status_updates):
                print('Testing for best server.')
            s.get_servers(servers)
            s.get_best_server()

            if (status_updates):
                print('Download test.')
            s.download(threads=threads)

            if (status_updates):
                print('Upload test.')
            s.upload(threads=threads)

            if (status_updates):
                print('Done.')
            results_dict = s.results.dict()

        except:
            # perhaps reconnect, etc.
            if (retry_updates):
                print('failed.')
            continue

        else:
            if (retry_updates):
                print('successful.')
            break

    return results_dict
