import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = workers*3

# accesslog = '/tmp/accesslog.txt'
# access_log_format = 'Neon (Outbreak News Today) %(h)s %(u)s %(t)s %(m)s Resopnse: %(s)s "%(q)s"'
