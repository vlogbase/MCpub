# Gunicorn configuration file
import multiprocessing

# Bind to 0.0.0.0:5000
bind = "0.0.0.0:5000"

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Use sync worker class
worker_class = "sync"

# Set timeout to 60 seconds
timeout = 60

# Enable access logging
accesslog = "-"

# Enable error logging
errorlog = "-"

# Set log level
loglevel = "debug"

# Disable daemonize
daemon = False
