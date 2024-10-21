import multiprocessing

# Gunicorn configuration file
bind = "0.0.0.0:5000"
workers = 2  # Adjust based on Replit's available CPU cores
threads = 4  # Increase if necessary
worker_class = "gthread"
timeout = 120
