import multiprocessing

# Bind to a Unix socket for better performance
bind = 'unix:/home/cafalchio/Projects/coinluxe/coinluxe.sock'

# Number of worker processes (adjust based on CPU cores)
workers = multiprocessing.cpu_count()

# Worker class for asynchronous handling
#worker_class = 'gevent'

# Use a high timeout to avoid worker restarts for long-running requests
timeout = 60

# Maximum number of requests a worker will process before restarting
max_requests = 1000

# Disable access logging to reduce I/O operations
accesslog = None

# Enable Gevent monkey patching for better concurrency
#import gevent.monkey
#gevent.monkey.patch_all()

# Additional settings to consider based on your application:
preload_app = True  # Preload application code for faster startup
limit_request_line = 4094  # Limit request line size to optimize memory usage
limit_request_fields = 100  # Limit number of request headers
keepalive = 2  # Number of requests allowed per connection

# Uncomment and configure logging if needed
# import logging
# errorlog = '-'  # Log to stdout
# loglevel = logging.INFO
# access_log_format = '%(t)s %(h)s "%(r)s" %(s)s %(L)s %(b)s "%(f)s" "%(a)s"'
