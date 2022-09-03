import speedtest


servers = []
threads = None

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)

results_dict = s.results.dict()

print(results_dict)