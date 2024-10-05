import multiprocessing

# Gunicorn configuration file
bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = 4
worker_class = "gevent"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = "info"
