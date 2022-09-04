import speedtest as ookla_speedtest


servers = []
threads = None


def speedtest(status_updates=False, retries=3):

    results_dict = None

    for attempt in range(retries):
        try:
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
            continue

        else:
            break

    return results_dict
