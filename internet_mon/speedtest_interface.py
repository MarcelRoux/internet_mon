import speedtest as ookla_speedtest


servers = []
threads = None


def speedtest(status_updates=False):

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

    # print(results_dict)
    return results_dict
